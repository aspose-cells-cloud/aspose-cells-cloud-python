"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostRemoveDuplicatesRequest(RequestOption):
    """Efficiently remove duplicate substrings from Excel cells. Select a range, specify delimiters, and apply options to eliminate repeated text segments."""

    def __init__(
        self,
        remove_duplicates_options: RemoveDuplicatesOptions,
    ):
        if remove_duplicates_options is None:
            raise ValueError("removeDuplicatesOptions is required")
        self.remove_duplicates_options = remove_duplicates_options

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/removeduplicates"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.remove_duplicates_options.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
