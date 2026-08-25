"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PasteOptions:
    """Represents the paste special options."""
    only_visible_cells: Optional[bool] = None
    paste_type: Optional[str] = None
    skip_blanks: Optional[bool] = None
    transpose: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.only_visible_cells is not None:
            result["OnlyVisibleCells"] = self.only_visible_cells
        if self.paste_type is not None:
            result["PasteType"] = self.paste_type
        if self.skip_blanks is not None:
            result["SkipBlanks"] = self.skip_blanks
        if self.transpose is not None:
            result["Transpose"] = self.transpose
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
