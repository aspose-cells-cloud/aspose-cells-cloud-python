"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostRemoveCharactersRequest(RequestOption):
    """A comprehensive set of tools for cleaning text content within selected cells. It allows users to remove specific characters, character sets, and substrings, ensuring that the text is standardized and free from unwanted symbols or sequences."""

    def __init__(
        self,
        remove_characters_options: RemoveCharactersOptions,
    ):
        if remove_characters_options is None:
            raise ValueError("removeCharactersOptions is required")
        self.remove_characters_options = remove_characters_options

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/removecharacters"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.remove_characters_options.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
