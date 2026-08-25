"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PivotGlobalizationSettings:
    """Represents the globalization settings for pivot tables."""
    pass

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
