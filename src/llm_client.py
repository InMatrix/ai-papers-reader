"""Provider-neutral helpers for the LLMs used by the paper pipeline."""

import os
from pathlib import Path

from google import genai
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
}


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
    provider = provider or resolve_provider(config=config)
    return model or config.get("model") or DEFAULT_MODELS[provider]


def create_client(provider=None):
    provider = resolve_provider(provider)
    config = load_config()

    if provider == "gemini":
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is not set")
        return genai.Client(api_key=api_key)

    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY environment variable is not set")

    from openai import OpenAI

    timeout = float(config.get("llm_timeout_seconds", 120))
    return OpenAI(
        api_key=api_key,
        base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
        timeout=timeout,
        max_retries=0,
    )


def generate_text(client, prompt, provider, model, json_output=False, temperature=None):
    """Generate text while normalizing the response shape across providers."""
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
