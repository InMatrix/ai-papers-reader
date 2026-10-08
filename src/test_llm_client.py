from types import SimpleNamespace
from unittest.mock import MagicMock, Mock, patch

import anthropic
import pytest

import llm_client
from llm_client import (
    _github_actions_identity_token,
    create_client,
    generate_text,
    load_config,
    resolve_model,
    resolve_provider,
)


def claude_message(text="response", stop_reason="end_turn", stop_details=None):
    return SimpleNamespace(
        content=[
            SimpleNamespace(type="thinking", thinking=""),
            SimpleNamespace(type="text", text=text),
        ],
        stop_reason=stop_reason,
        stop_details=stop_details,
        usage=SimpleNamespace(iterations=None),
        model="claude-opus-5-5",
    )


def claude_client(message):
    client = MagicMock()
    stream = client.beta.messages.stream.return_value.__enter__.return_value
    stream.get_final_message.return_value = message
    return client


def test_resolve_provider_defaults_to_gemini(monkeypatch):
    assert resolve_provider(config={}) == "gemini"


def test_resolve_provider_uses_tracked_config():
    assert resolve_provider(config={"provider": "deepseek"}) == "deepseek"


def test_load_config_reads_committed_config():
    config = load_config()
    assert config["provider"] in {"gemini", "deepseek", "claude"}
    assert config["model"]


def test_resolve_provider_rejects_unknown_provider():
    with pytest.raises(ValueError, match="Unsupported LLM provider"):
        resolve_provider("unknown")


def test_resolve_model_uses_deepseek_default():
    assert resolve_model("deepseek", config={}) == "deepseek-v4-flash"


def test_resolve_model_uses_claude_default():
    assert resolve_model("claude", config={}) == "claude-opus-5-5"


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


def test_generate_text_streams_claude_with_fallbacks_and_no_temperature():
    client = claude_client(claude_message("[]"))

    result = generate_text(
        client,
        "prompt",
        provider="claude",
        model="claude-opus-5-5",
        json_output=True,
        temperature=0.7,
    )

    assert result == "[]"
    client.beta.messages.stream.assert_called_once_with(
        model="claude-opus-5-5",
        max_tokens=64000,
        messages=[{"role": "user", "content": "prompt"}],
        output_config={"effort": "medium"},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )


def test_generate_text_omits_fallbacks_for_other_claude_models():
    client = claude_client(claude_message())

    generate_text(client, "prompt", provider="claude", model="claude-haiku-5-5")

    request = client.beta.messages.stream.call_args.kwargs
    assert "fallbacks" not in request
    assert "betas" not in request


@pytest.mark.parametrize(
    ("stop_reason", "stop_details", "message"),
    [
        ("refusal", SimpleNamespace(category="cyber"), "declined.*cyber"),
        ("max_tokens", None, "cut off"),
    ],
)
def test_generate_text_rejects_incomplete_claude_responses(
    stop_reason, stop_details, message
):
    client = claude_client(
        claude_message("partial", stop_reason=stop_reason, stop_details=stop_details)
    )

    with pytest.raises(RuntimeError, match=message):
        generate_text(client, "prompt", provider="claude", model="claude-opus-5-5")


def test_github_actions_identity_token_requests_anthropic_audience(monkeypatch):
    monkeypatch.setenv(
        "ACTIONS_ID_TOKEN_REQUEST_URL", "https://token.example.test/id?api-version=2.0"
    )
    monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN", "request-token")
    response = Mock()
    response.json.return_value = {"value": "github-jwt"}

    with patch("llm_client.requests.get", return_value=response) as get:
        assert _github_actions_identity_token() == "github-jwt"

    get.assert_called_once_with(
        "https://token.example.test/id?api-version=2.0",
        params={"audience": "https://api.anthropic.com"},
        headers={"Authorization": "Bearer request-token"},
        timeout=30,
    )
    response.raise_for_status.assert_called_once_with()


def test_create_client_federates_claude_with_fresh_github_tokens(monkeypatch):
    monkeypatch.setattr(llm_client, "load_config", lambda: {"llm_timeout_seconds": 30})
    monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_URL", "https://token.example.test/id")
    monkeypatch.setenv("ANTHROPIC_FEDERATION_RULE_ID", "fdrl_test")
    monkeypatch.setenv("ANTHROPIC_ORGANIZATION_ID", "org-id")
    monkeypatch.setenv("ANTHROPIC_SERVICE_ACCOUNT_ID", "svac_test")
    monkeypatch.setenv("ANTHROPIC_WORKSPACE_ID", "wrkspc_test")
    credentials_class = Mock()
    client_class = Mock()
    monkeypatch.setattr(anthropic, "WorkloadIdentityCredentials", credentials_class)
    monkeypatch.setattr(anthropic, "Anthropic", client_class)

    assert create_client("claude") is client_class.return_value

    credentials_class.assert_called_once_with(
        identity_token_provider=_github_actions_identity_token,
        federation_rule_id="fdrl_test",
        organization_id="org-id",
        service_account_id="svac_test",
        workspace_id="wrkspc_test",
    )
    client_class.assert_called_once_with(
        credentials=credentials_class.return_value, timeout=30.0
    )


def test_create_client_uses_sdk_credentials_for_claude_outside_github(monkeypatch):
    monkeypatch.setattr(llm_client, "load_config", lambda: {"llm_timeout_seconds": 30})
    monkeypatch.delenv("ACTIONS_ID_TOKEN_REQUEST_URL", raising=False)
    client_class = Mock()
    monkeypatch.setattr(anthropic, "Anthropic", client_class)

    assert create_client("claude") is client_class.return_value

    client_class.assert_called_once_with(timeout=30.0)
