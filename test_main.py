from unittest.mock import patch

from greeting import greet
from main import main


def test_greet(capsys):
    greet("Alice")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice !\n"


def test_main(capsys):
    with patch("builtins.input", return_value="Bob"):
        main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, Bob !\n"
