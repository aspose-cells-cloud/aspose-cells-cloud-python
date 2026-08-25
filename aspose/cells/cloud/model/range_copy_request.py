"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RangeCopyRequest:
    """Indicates range copy request"""
    operate: Optional[str] = None
    source: Optional[Range] = None
    target: Optional[Range] = None
    target_workbook: Optional[str] = None
    paste_options: Optional[PasteOptions] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.operate is not None:
            result["Operate"] = self.operate
        if self.source is not None:
            result["Source"] = self.source.to_dict()
        if self.target is not None:
            result["Target"] = self.target.to_dict()
        if self.target_workbook is not None:
            result["TargetWorkbook"] = self.target_workbook
        if self.paste_options is not None:
            result["PasteOptions"] = self.paste_options.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
