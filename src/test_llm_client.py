from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from llm_client import generate_text, resolve_model, resolve_provider


def test_resolve_provider_defaults_to_gemini(monkeypatch):
    monkeypatch.delenv("LLM_PROVIDER", raising=False)
    assert resolve_provider() == "gemini"


def test_resolve_provider_rejects_unknown_provider():
    with pytest.raises(ValueError, match="Unsupported LLM provider"):
        resolve_provider("unknown")


def test_resolve_model_uses_deepseek_default(monkeypatch):
    monkeypatch.delenv("LLM_MODEL", raising=False)
    assert resolve_model("deepseek") == "deepseek-v4-flash"


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
