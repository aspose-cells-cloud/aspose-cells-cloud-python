"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RemoveCharactersOptions:
    """Class summary: The class features discussing effective communication strategies, developing problem-solving skills, and increasing self-awareness for personal growth."""
    name: Optional[str] = None
    data_source: Optional[DataSource] = None
    file_info: Optional[FileInfo] = None
    scope_options: Optional[ScopeOptions] = None
    remove_characters_by_character: Optional[RemoveCharactersByCharacter] = None
    remove_characters_by_position: Optional[RemoveCharactersByPosition] = None

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
        if self.remove_characters_by_character is not None:
            result["RemoveCharactersByCharacter"] = self.remove_characters_by_character.to_dict()
        if self.remove_characters_by_position is not None:
            result["RemoveCharactersByPosition"] = self.remove_characters_by_position.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
