"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class CheckWrokbookExternalReferenceRequest(RequestOption):
    """Export Excel internal elements or the workbook itself to various format files."""

    def __init__(
        self,
        check_external_reference_options: CheckExternalReferenceOptions,
    ):
        if check_external_reference_options is None:
            raise ValueError("checkExternalReferenceOptions is required")
        self.check_external_reference_options = check_external_reference_options

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/checkexternalreference"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.check_external_reference_options.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
