from types import SimpleNamespace

from app import ask as ask_module


def test_ask_prints_input_and_output_token_counts(monkeypatch, capsys):
    captured = {}

    class FakeClient:
        def __init__(self, api_key):
            self.models = self

        def generate_content(self, *, model, contents, config):
            captured["config"] = config
            return SimpleNamespace(
                text="answer",
                usage_metadata=SimpleNamespace(
                    prompt_token_count=12,
                    candidates_token_count=7,
                ),
            )

    monkeypatch.setattr(ask_module.genai, "Client", FakeClient)
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-key")

    assert ask_module.ask("question") == "answer"
    assert captured["config"].temperature == ask_module.DEFAULT_TEMPERATURE
    assert "[usage] input_tokens=12, output_tokens=7" in capsys.readouterr().out


def test_ask_uses_specified_temperature(monkeypatch):
    captured = {}

    class FakeClient:
        def __init__(self, api_key):
            self.models = self

        def generate_content(self, *, model, contents, config):
            captured["config"] = config
            return SimpleNamespace(text="answer", usage_metadata=None)

    monkeypatch.setattr(ask_module.genai, "Client", FakeClient)
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-key")

    ask_module.ask("question", temperature=0.3)

    assert captured["config"].temperature == 0.3