from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch
from uuid import uuid4

import pytest
from nbformat import NotebookNode

from papermill_service.executor import (
    execute_notebook_with_tracking,
    get_execution_status,
)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("notebook_path", "parameters"),
    [(Path("boring.ipynb"), dict()), (Path("replace.ipynb"), dict(some="thing"))],
)
async def test_executor_runs_papermill(notebook_path: Path, parameters: dict[str, Any]):
    with patch("papermill_service.executor.execute_notebook") as mock_executor:
        await execute_notebook_with_tracking(uuid4(), notebook_path, parameters)
        mock_executor.assert_called_with(notebook_path, None, parameters=parameters)


@pytest.mark.asyncio
async def test_exectutor_returns_notebook():
    mock_notebook = dict(value=MagicMock)

    def mock_executor(*args, **kwargs) -> NotebookNode:
        return mock_notebook

    with patch(
        "papermill_service.executor.execute_notebook",
        mock_executor,
    ):
        uuid = uuid4()
        await execute_notebook_with_tracking(uuid, "boring.ipynb", dict())
        assert mock_notebook == get_execution_status(uuid).status.notebook


@pytest.mark.asyncio
async def test_exectutor_sets_execution_status_returns_not_found():
    with patch("papermill_service.executor.execute_notebook"):
        uuid = uuid4()
        assert "not_found" == get_execution_status(uuid).status.status


@pytest.mark.asyncio
async def test_exectutor_sets_execution_status_complete():
    with patch("papermill_service.executor.execute_notebook"):
        uuid = uuid4()
        await execute_notebook_with_tracking(uuid, "boring.ipynb", dict())
        assert "complete" == get_execution_status(uuid).status.status


@pytest.mark.asyncio
async def test_executor_sets_execution_status_pending():
    uuid = uuid4()

    def mock_executor(*args, **kwargs):
        assert "pending" == get_execution_status(uuid).status.status
        return NotebookNode()

    with patch("papermill_service.executor.execute_notebook", mock_executor):
        await execute_notebook_with_tracking(uuid, "boring.ipynb", dict())
