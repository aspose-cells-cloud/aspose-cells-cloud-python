"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostBatchLockRequest(RequestOption):
    """Batch locking files that meet specific matching conditions."""

    def __init__(
        self,
        batch_lock_request: BatchLockRequest,
    ):
        if batch_lock_request is None:
            raise ValueError("batchLockRequest is required")
        self.batch_lock_request = batch_lock_request

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/batch/lock"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.batch_lock_request.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
