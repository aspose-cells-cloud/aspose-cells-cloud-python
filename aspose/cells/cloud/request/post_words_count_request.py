"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWordsCountRequest(RequestOption):
    """PostWordsCountRequest."""

    def __init__(
        self,
        words_count_options: WordsCountOptions,
    ):
        if words_count_options is None:
            raise ValueError("wordsCountOptions is required")
        self.words_count_options = words_count_options

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/wordscount"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.words_count_options.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
