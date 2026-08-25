"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RemoveCharactersByPosition:
    """RemoveCharactersByPosition."""
    the_first_n_characters: Optional[int] = None
    the_last_n_characters: Optional[int] = None
    all_characters_before_text: Optional[str] = None
    all_characters_after_text: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.the_first_n_characters is not None:
            result["TheFirstNCharacters"] = self.the_first_n_characters
        if self.the_last_n_characters is not None:
            result["TheLastNCharacters"] = self.the_last_n_characters
        if self.all_characters_before_text is not None:
            result["AllCharactersBeforeText"] = self.all_characters_before_text
        if self.all_characters_after_text is not None:
            result["AllCharactersAfterText"] = self.all_characters_after_text
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
