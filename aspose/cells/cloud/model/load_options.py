"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class LoadOptions:
    """Represents the options of loading the file."""
    convert_numeric_data: Optional[str] = None
    interrupt_monitor: Optional[str] = None
    language_code: Optional[str] = None
    load_data_options: Optional[str] = None
    load_format: Optional[str] = None
    only_load_document_properties: Optional[str] = None
    parsing_formula_on_open: Optional[str] = None
    password: Optional[str] = None
    region: Optional[str] = None
    standard_font: Optional[str] = None
    standard_font_size: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.convert_numeric_data is not None:
            result["ConvertNumericData"] = self.convert_numeric_data
        if self.interrupt_monitor is not None:
            result["InterruptMonitor"] = self.interrupt_monitor
        if self.language_code is not None:
            result["LanguageCode"] = self.language_code
        if self.load_data_options is not None:
            result["LoadDataOptions"] = self.load_data_options
        if self.load_format is not None:
            result["LoadFormat"] = self.load_format
        if self.only_load_document_properties is not None:
            result["OnlyLoadDocumentProperties"] = self.only_load_document_properties
        if self.parsing_formula_on_open is not None:
            result["ParsingFormulaOnOpen"] = self.parsing_formula_on_open
        if self.password is not None:
            result["Password"] = self.password
        if self.region is not None:
            result["Region"] = self.region
        if self.standard_font is not None:
            result["StandardFont"] = self.standard_font
        if self.standard_font_size is not None:
            result["StandardFontSize"] = self.standard_font_size
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
