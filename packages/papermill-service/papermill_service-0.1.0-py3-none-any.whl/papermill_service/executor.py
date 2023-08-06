from collections import defaultdict
from typing import Literal, Union, cast
from uuid import UUID

from nbformat import NotebookNode
from papermill import execute_notebook
from pydantic import BaseModel, Field, FilePath


class ExecutionNotFound(BaseModel):
    """An execution status representing jobs which have not yet been started.

    An execution status representing jobs which have not yet been started. Such a
    status is not to be expected in normal operation.
    """

    status: Literal["not_found"]


class ExecutionPending(BaseModel):
    """An execution status representing jobs which are pending.

    An execution status representing jobs which are have been started but are not yet
    complete.
    """

    status: Literal["pending"]


class ExecutionComplete(BaseModel):
    """An execution status representing jobs which been completed.

    An execution status representing jobs which been completed. This status holds the
    resultant notebook output.
    """

    status: Literal["complete"]
    notebook: NotebookNode


class ExecutionStatus(BaseModel):
    """A discriminated union of possible execution statuses."""

    status: Union[ExecutionNotFound, ExecutionPending, ExecutionComplete] = Field(
        discriminator="status"
    )


_EXECUTIONS: dict[UUID, ExecutionStatus] = defaultdict(
    lambda: ExecutionStatus(status=dict(status="not_found"))
)


async def execute_notebook_with_tracking(
    uuid: UUID, notebook_path: FilePath, parameters: dict
) -> None:
    """Runs the hosted notebook, with tracking of the corresponding status.

    Runs the hosted notebook, assigning the corresponding status to "pending" at the
    beginning of execution and "complete" at the end with the corresponding notebook
    output.

    Args:
        uuid: The unique identifier used to track the execution.
        notebook_path: The path to the notebook to be executed.
        parameters: A dictionary of parameters to be assigned to the notebook.
    """
    _EXECUTIONS[uuid] = ExecutionStatus(status=dict(status="pending"))
    notebook = cast(
        NotebookNode,
        execute_notebook(notebook_path, None, parameters=parameters),
    )
    _EXECUTIONS[uuid] = ExecutionStatus(
        status=dict(status="complete", notebook=notebook)
    )


def get_execution_status(uuid: UUID) -> ExecutionStatus:
    """Gets the execution status of the execution corresponding to the provided UUID.

    Args:
        uuid (UUID): The unique identifier used to track the execution.

    Returns:
        ExecutionStatus: The executions status of the requested execution.
    """
    return _EXECUTIONS[uuid]
