"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CellsCloudPublicKey:
    """CellsCloudPublicKey."""
    exponent: Optional[str] = None
    modulus: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.exponent is not None:
            result["Exponent"] = self.exponent
        if self.modulus is not None:
            result["Modulus"] = self.modulus
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
