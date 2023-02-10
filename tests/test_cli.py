from pygarth import cli
import pytest

def test_cli_template():
    assert cli.cli() is None
