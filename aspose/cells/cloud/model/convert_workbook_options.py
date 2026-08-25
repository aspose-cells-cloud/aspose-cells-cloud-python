"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ConvertWorkbookOptions:
    """ConvertWorkbookOptions."""
    name: Optional[str] = None
    data_source: Optional[DataSource] = None
    file_info: Optional[FileInfo] = None
    page_setup: Optional[PageSetup] = None
    save_options: Optional[SaveOptions] = None
    convert_format: Optional[str] = None
    check_excel_restriction: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.file_info is not None:
            result["FileInfo"] = self.file_info.to_dict()
        if self.page_setup is not None:
            result["PageSetup"] = self.page_setup.to_dict()
        if self.save_options is not None:
            result["SaveOptions"] = self.save_options.to_dict()
        if self.convert_format is not None:
            result["ConvertFormat"] = self.convert_format
        if self.check_excel_restriction is not None:
            result["CheckExcelRestriction"] = self.check_excel_restriction
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
