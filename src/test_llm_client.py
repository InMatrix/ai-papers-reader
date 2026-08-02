from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from llm_client import generate_text, load_config, resolve_model, resolve_provider


def test_resolve_provider_defaults_to_gemini(monkeypatch):
    assert resolve_provider(config={}) == "gemini"


def test_resolve_provider_uses_tracked_config():
    assert resolve_provider(config={"provider": "deepseek"}) == "deepseek"


def test_load_config_reads_committed_config():
    config = load_config()
    assert config["provider"] in {"gemini", "deepseek"}
    assert config["model"]


def test_resolve_provider_rejects_unknown_provider():
    with pytest.raises(ValueError, match="Unsupported LLM provider"):
        resolve_provider("unknown")


def test_resolve_model_uses_deepseek_default():
    assert resolve_model("deepseek", config={}) == "deepseek-v4-flash"


def test_resolve_model_uses_tracked_config():
    assert resolve_model(
        "deepseek",
        config={"provider": "deepseek", "model": "deepseek-v4-pro"},
    ) == "deepseek-v4-pro"


def test_resolve_model_uses_selected_provider_default_for_mismatched_config():
    config = {"provider": "deepseek", "model": "deepseek-v4-flash"}

    assert resolve_model("gemini", config=config) == "gemini-flash-latest"


def test_resolve_model_explicit_override_wins_over_configured_provider():
    config = {"provider": "deepseek", "model": "deepseek-v4-flash"}

    assert resolve_model(
        "gemini", model="gemini-2.5-flash", config=config
    ) == "gemini-2.5-flash"


def test_generate_text_uses_deepseek_chat_completions():
    client = Mock()
    client.chat.completions.create.return_value = SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content="response"))]
    )

    result = generate_text(
        client,
        "prompt",
        provider="deepseek",
        model="deepseek-v4-pro",
        temperature=0.7,
    )

    assert result == "response"
    client.chat.completions.create.assert_called_once_with(
        model="deepseek-v4-pro",
        messages=[{"role": "user", "content": "prompt"}],
        stream=False,
        temperature=0.7,
    )
