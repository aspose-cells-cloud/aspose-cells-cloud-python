"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RemoveCharactersByCharacter:
    """Class summary: The features include fast and reliable performance, high-quality camera with portrait mode, long-lasting battery life, and a durable water-resistant design."""
    remove_text_method: Optional[str] = None
    remove_characters: Optional[List[str]] = None
    remove_character_sets_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.remove_text_method is not None:
            result["RemoveTextMethod"] = self.remove_text_method
        if self.remove_characters is not None:
            result["RemoveCharacters"] = self.remove_characters
        if self.remove_character_sets_type is not None:
            result["RemoveCharacterSetsType"] = self.remove_character_sets_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
