from functools import lru_cache
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch
from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient

from papermill_service import __version__
from papermill_service.executor import ExecutionStatus, get_execution_status


@pytest.fixture
def client() -> TestClient:
    from papermill_service.app import app
    from papermill_service.config import Settings, get_settings

    @lru_cache
    def get_test_settings():
        return Settings(notebook_path=Path("tests/source.ipynb"))

    app.dependency_overrides[get_settings] = get_test_settings
    return TestClient(app)


def test_version(client: TestClient):
    response = client.get("/version")
    assert 200 == response.status_code
    assert dict(version=__version__) == response.json()


def test_params(client: TestClient):
    response = client.get("/params")
    assert 200 == response.status_code
    assert (
        dict(
            hello=dict(
                name="hello", inferred_type_name="str", default='"world"', help=""
            ),
            answer=dict(name="answer", inferred_type_name="int", default="42", help=""),
        )
        == response.json()
    )


@pytest.mark.parametrize("parameters", [dict(), dict(hello="testing")])
def test_start_runs_notebook_with_params(
    parameters: dict[str, Any], client: TestClient
):
    with patch("papermill_service.app.execute_notebook_with_tracking") as mock_executor:
        response = client.post("/start", json=parameters)
        assert 200 == response.status_code
        task_id = UUID(response.json()["task_id"])
        mock_executor.assert_called_once_with(
            task_id, Path("tests/source.ipynb"), parameters
        )


def test_fetch_gets_execution_status(client: TestClient):
    mock_execution_status = ExecutionStatus(status=dict(status="pending"))

    with patch(
        "papermill_service.app.get_execution_status",
        MagicMock(get_execution_status, return_value=mock_execution_status),
    ):
        response = client.get(f"/fetch/{uuid4()}")
        assert 200 == response.status_code
        assert mock_execution_status.status == response.json()
