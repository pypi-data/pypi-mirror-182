from os import environ
from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import ValidationError

from papermill_service.config import get_settings


def test_notebook_path_raises_if_not_set():
    with pytest.raises(ValidationError):
        get_settings().notebook_path


def test_notebook_path_raises_if_notexistant():
    with patch.dict(
        environ, dict(NOTEBOOK_PATH="tests/nonexistant.ipynb")
    ) and pytest.raises(ValidationError):
        get_settings().notebook_path


def test_notebook_path_from_env_var():
    with patch.dict(environ, dict(NOTEBOOK_PATH="tests/source.ipynb")):
        assert Path("tests/source.ipynb") == get_settings().notebook_path
