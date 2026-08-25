"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class GetCellsCloudServiceStatusRequest(RequestOption):
    """Aspose.Cells Cloud service health status check."""

    def __init__(self) -> None:
        pass

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return "/v3.0/cells/status/check"

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
