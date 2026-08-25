"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ResultDestination:
    """Represents result destination."""
    destination_type: Optional[str] = None
    input_file: Optional[str] = None
    output_file: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.destination_type is not None:
            result["DestinationType"] = self.destination_type
        if self.input_file is not None:
            result["InputFile"] = self.input_file
        if self.output_file is not None:
            result["OutputFile"] = self.output_file
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
