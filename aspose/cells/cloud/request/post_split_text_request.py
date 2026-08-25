"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostSplitTextRequest(RequestOption):
    """Efficiently divides Excel cell content into columns or rows based on specified delimiters or patterns. Supports Character-based splitting, Custom string splitting, Mask and wildcard splitting for pattern-based division, Line break division, Column or row splitting, Delimiter removal or retention."""

    def __init__(
        self,
        split_text_options: SplitTextOptions,
    ):
        if split_text_options is None:
            raise ValueError("splitTextOptions is required")
        self.split_text_options = split_text_options

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/splittext"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.split_text_options.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
