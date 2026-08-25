"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostRunTaskRequest(RequestOption):
    """Run tasks."""

    def __init__(
        self,
        task_data: TaskData,
    ):
        if task_data is None:
            raise ValueError("TaskData is required")
        self.task_data = task_data

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/task/runtask"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.task_data.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
