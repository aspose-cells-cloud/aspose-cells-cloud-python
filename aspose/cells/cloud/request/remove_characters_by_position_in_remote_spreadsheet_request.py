"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class RemoveCharactersByPositionInRemoteSpreadsheetRequest(RequestOption):
    """Deletes characters from every cell in the target range by position (first/last N, before/after a substring, or between two delimiters) while preserving formulas, formatting and data-validation."""

    def __init__(
        self,
        name: str,
        worksheet: str,
        range_: str,
        the_first_n_characters: Optional[int] = None,
        the_last_n_characters: Optional[int] = None,
        all_characters_before_text: Optional[str] = None,
        all_characters_after_text: Optional[str] = None,
        case_sensitive: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not worksheet:
            raise ValueError("worksheet is required")
        if not range_:
            raise ValueError("range is required")
        self.name = name
        self.worksheet = worksheet
        self.range_ = range_
        self.the_first_n_characters = the_first_n_characters
        self.the_last_n_characters = the_last_n_characters
        self.all_characters_before_text = all_characters_before_text
        self.all_characters_after_text = all_characters_after_text
        self.case_sensitive = case_sensitive
        self.folder = folder
        self.storage_name = storage_name
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v4.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.worksheet, safe="/") +
            "/range/" +
            quote(self.range_, safe="/") +
            "/content/remove/characters-by-position"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.the_first_n_characters is not None:
            params["theFirstNCharacters"] = str(self.the_first_n_characters)
        if self.the_last_n_characters is not None:
            params["theLastNCharacters"] = str(self.the_last_n_characters)
        if self.all_characters_before_text:
            params["allCharactersBeforeText"] = self.all_characters_before_text
        if self.all_characters_after_text:
            params["allCharactersAfterText"] = self.all_characters_after_text
        if self.case_sensitive is not None:
            params["caseSensitive"] = "true" if self.case_sensitive else "false"
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.region:
            params["region"] = self.region
        if self.password:
            params["password"] = self.password
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
