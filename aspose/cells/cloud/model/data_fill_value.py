"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataFillValue:
    """Represents that the data is populated with the specified value."""
    default_boolean: Optional[bool] = None
    default_string: Optional[str] = None
    default_number: Optional[int] = None
    default_double: Optional[float] = None
    default_date: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.default_boolean is not None:
            result["DefaultBoolean"] = self.default_boolean
        if self.default_string is not None:
            result["DefaultString"] = self.default_string
        if self.default_number is not None:
            result["DefaultNumber"] = self.default_number
        if self.default_double is not None:
            result["DefaultDouble"] = self.default_double
        if self.default_date is not None:
            result["DefaultDate"] = self.default_date
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
