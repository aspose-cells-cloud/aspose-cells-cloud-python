"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class DecomposeUserTaskRequest(RequestOption):
    """AI task decomposition: Convert user objectives to sequential action plans with formatted file export."""

    def __init__(
        self,
        task_description: str,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not task_description:
            raise ValueError("TaskDescription is required")
        self.task_description = task_description
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/ai/task/decompose"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.region:
            params["region"] = self.region
        if self.password:
            params["password"] = self.password
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.task_description

    def get_multipart_form(self) -> Optional[dict]:
        return None
