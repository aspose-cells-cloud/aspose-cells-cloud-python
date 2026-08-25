"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostAddTextContentRequest(RequestOption):
    """Adds text content to a specified location within a document. It requires an object that defines the text to be added and the insertion location."""

    def __init__(
        self,
        add_text_options: AddTextOptions,
    ):
        if add_text_options is None:
            raise ValueError("addTextOptions is required")
        self.add_text_options = add_text_options

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/addtext"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.add_text_options.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
