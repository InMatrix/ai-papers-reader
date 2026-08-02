"""Provider-neutral helpers for the LLMs used by the paper pipeline."""

import os

from google import genai


DEFAULT_MODELS = {
    "gemini": "gemini-flash-latest",
    "deepseek": "deepseek-v4-flash",
}


def resolve_provider(provider=None):
    provider = (provider or os.getenv("LLM_PROVIDER", "gemini")).lower()
    if provider not in DEFAULT_MODELS:
        supported = ", ".join(DEFAULT_MODELS)
        raise ValueError(f"Unsupported LLM provider '{provider}'. Choose one of: {supported}")
    return provider


def resolve_model(provider, model=None):
    return model or os.getenv("LLM_MODEL") or DEFAULT_MODELS[provider]


def create_client(provider=None):
    provider = resolve_provider(provider)

    if provider == "gemini":
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is not set")
        return genai.Client(api_key=api_key)

    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY environment variable is not set")

    from openai import OpenAI

    return OpenAI(
        api_key=api_key,
        base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
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
