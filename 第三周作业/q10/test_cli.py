import pytest
from greetlab.cli import main
import sys

def test_cli_whitespace_name(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "   "])
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 2
