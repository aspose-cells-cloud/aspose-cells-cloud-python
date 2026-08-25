"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ConvertTextOptions:
    """Class summary: The features of the new smartphone include a high-resolution display, multiple camera lenses for versatile photography, a fast processor for seamless performance, and a larger battery for extended usage time."""
    name: Optional[str] = None
    data_source: Optional[DataSource] = None
    file_info: Optional[FileInfo] = None
    scope_options: Optional[ScopeOptions] = None
    convert_text_type: Optional[str] = None
    source_characters: Optional[str] = None
    target_characters: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.file_info is not None:
            result["FileInfo"] = self.file_info.to_dict()
        if self.scope_options is not None:
            result["ScopeOptions"] = self.scope_options.to_dict()
        if self.convert_text_type is not None:
            result["ConvertTextType"] = self.convert_text_type
        if self.source_characters is not None:
            result["SourceCharacters"] = self.source_characters
        if self.target_characters is not None:
            result["TargetCharacters"] = self.target_characters
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
