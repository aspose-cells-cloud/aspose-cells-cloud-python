"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SaveResultTaskParameter:
    """Represents save result task parameter."""
    result_source: Optional[str] = None
    result_destination: Optional[ResultDestination] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.result_source is not None:
            result["ResultSource"] = self.result_source
        if self.result_destination is not None:
            result["ResultDestination"] = self.result_destination.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
