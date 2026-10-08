"""Provider-neutral helpers for the LLMs used by the paper pipeline."""

import os
from pathlib import Path

from google import genai
import requests
import yaml
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "config.yaml"

# Load credentials for local runs without overriding variables supplied by
# GitHub Actions or the caller's shell.
load_dotenv(PROJECT_ROOT / ".env")


DEFAULT_MODELS = {
    "gemini": "gemini-flash-latest",
    "deepseek": "deepseek-v4-flash",
    "claude": "claude-haiku-5-5",
}

# Claude models whose safety-classifier declines the API can rerun on
# Anthropic's recommended fallback model.
CLAUDE_FALLBACK_MODELS = {
    "claude-fable-5-1",
    "claude-opus-5-5",
    "claude-opus-5",
    "claude-sonnet-5-5",
}

GITHUB_OIDC_AUDIENCE = "https://api.anthropic.com"


def load_config(config_path=None):
    """Load the tracked provider/model configuration."""
    path = Path(config_path) if config_path else CONFIG_PATH
    if not path.exists():
        return {}

    with path.open("r") as file:
        config = yaml.safe_load(file) or {}
    if not isinstance(config, dict):
        raise ValueError(f"LLM config must be a YAML mapping: {path}")
    return config


def resolve_provider(provider=None, config=None):
    config = config if config is not None else load_config()
    provider = (provider or config.get("provider", "gemini")).lower()
    if provider not in DEFAULT_MODELS:
        supported = ", ".join(DEFAULT_MODELS)
        raise ValueError(f"Unsupported LLM provider '{provider}'. Choose one of: {supported}")
    return provider


def resolve_model(provider, model=None, config=None):
    config = config if config is not None else load_config()
    provider = resolve_provider(provider, config=config)
    if model:
        return model

    configured_model = config.get("model")
    configured_provider = str(config.get("provider", "")).lower()
    if configured_model and (
        not configured_provider or configured_provider == provider
    ):
        return configured_model
    return DEFAULT_MODELS[provider]


def _github_actions_identity_token():
    """Request a new GitHub Actions OIDC token for one Claude token exchange."""
    response = requests.get(
        os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"],
        params={"audience": GITHUB_OIDC_AUDIENCE},
        headers={
            "Authorization": f"Bearer {os.environ['ACTIONS_ID_TOKEN_REQUEST_TOKEN']}"
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["value"]


def _create_claude_client(timeout):
    import anthropic

    if not (
        os.getenv("ACTIONS_ID_TOKEN_REQUEST_URL")
        and os.getenv("ANTHROPIC_FEDERATION_RULE_ID")
    ):
        # Without GitHub's OIDC endpoint, the SDK resolves ANTHROPIC_API_KEY,
        # an `ant auth login` profile, or the ANTHROPIC_* federation variables.
        return anthropic.Anthropic(timeout=timeout)

    # GitHub OIDC tokens expire about five minutes after issue and Anthropic
    # accepts each one only once, while the SDK re-exchanges before its
    # short-lived access token expires. A token written to a file at job start
    # would fail that refresh mid-run, so fetch a new one for every exchange.
    credentials = anthropic.WorkloadIdentityCredentials(
        identity_token_provider=_github_actions_identity_token,
        federation_rule_id=os.environ["ANTHROPIC_FEDERATION_RULE_ID"],
        organization_id=os.environ["ANTHROPIC_ORGANIZATION_ID"],
        service_account_id=os.getenv("ANTHROPIC_SERVICE_ACCOUNT_ID") or None,
        workspace_id=os.getenv("ANTHROPIC_WORKSPACE_ID") or None,
    )
    return anthropic.Anthropic(credentials=credentials, timeout=timeout)


def create_client(provider=None):
    provider = resolve_provider(provider)
    config = load_config()

    if provider == "gemini":
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is not set")
        return genai.Client(api_key=api_key)

    timeout = float(config.get("llm_timeout_seconds", 120))
    if provider == "claude":
        return _create_claude_client(timeout)

    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY environment variable is not set")

    from openai import OpenAI

    return OpenAI(
        api_key=api_key,
        base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
        timeout=timeout,
        max_retries=0,
    )


def _generate_claude_text(client, content, model):
    """Return Claude's reply to a prompt string or a list of content blocks."""
    # Current Claude models reject sampling parameters such as temperature and
    # have no schema-free JSON mode, so, as with DeepSeek, the prompts
    # themselves ask for raw JSON where the pipeline needs it.
    kwargs = {
        "model": model,
        # Adaptive thinking counts toward max_tokens, so leave ample headroom.
        "max_tokens": 64000,
        "messages": [{"role": "user", "content": content}],
        # Medium is the default on Haiku 5.5 and Opus 5.5; pin it so other
        # Claude models match.
        "output_config": {"effort": "medium"},
    }
    if model in CLAUDE_FALLBACK_MODELS:
        # Safety classifiers can decline benign papers (AI security research,
        # for example); let the API rerun those on its recommended fallback.
        kwargs["betas"] = ["server-side-fallback-2026-07-01"]
        kwargs["fallbacks"] = "default"

    # Streaming applies the client timeout between events rather than to the
    # whole response, which long PDF summaries can exceed.
    with client.beta.messages.stream(**kwargs) as stream:
        message = stream.get_final_message()

    if message.stop_reason == "refusal":
        category = message.stop_details.category if message.stop_details else None
        raise RuntimeError(f"Claude declined the request (category: {category})")
    if message.stop_reason != "end_turn":
        # These requests use no tools or stop sequences, so any other stop
        # reason, such as max_tokens or model_context_window_exceeded, means
        # the reply was cut off.
        raise RuntimeError(
            f"Claude's response is incomplete (stop_reason: {message.stop_reason})"
        )
    if any(
        iteration.type == "fallback_message"
        for iteration in message.usage.iterations or []
    ):
        print(f"Claude fallback model {message.model} completed the request")
    return "".join(block.text for block in message.content if block.type == "text")


def generate_text(client, prompt, provider, model, json_output=False, temperature=None):
    """Generate text while normalizing the response shape across providers."""
    if provider == "claude":
        return _generate_claude_text(client, prompt, model)

    if provider == "gemini":
        config = {}
        if json_output:
            config["response_mime_type"] = "application/json"
        if temperature is not None:
            config["temperature"] = temperature

        kwargs = {"model": model, "contents": prompt}
        if config:
            kwargs["config"] = config
        return client.models.generate_content(**kwargs).text

    kwargs = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }
    if temperature is not None:
        kwargs["temperature"] = temperature

    # DeepSeek's JSON mode currently requires a top-level object, while the
    # report prompt intentionally returns a top-level array. The prompt itself
    # therefore enforces JSON for this pipeline.
    response = client.chat.completions.create(**kwargs)
    return response.choices[0].message.content
