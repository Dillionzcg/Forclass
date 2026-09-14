import pytest
import sys
from greetlab.cli import main


def test_cli_normal_name(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "Alice"])
    main()
    captured = capsys.readouterr()
    assert "Hello, Alice!" in captured.out


def test_cli_whitespace_name(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "   "])
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 2
