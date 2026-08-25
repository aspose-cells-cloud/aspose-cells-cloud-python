"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RangeConvertRequest:
    """Indicates range copy request"""
    source: Optional[Range] = None
    image_type: Optional[str] = None
    image_or_print_options: Optional[ImageOrPrintOptions] = None
    page_setup: Optional[PageSetup] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.source is not None:
            result["Source"] = self.source.to_dict()
        if self.image_type is not None:
            result["ImageType"] = self.image_type
        if self.image_or_print_options is not None:
            result["ImageOrPrintOptions"] = self.image_or_print_options.to_dict()
        if self.page_setup is not None:
            result["PageSetup"] = self.page_setup.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
