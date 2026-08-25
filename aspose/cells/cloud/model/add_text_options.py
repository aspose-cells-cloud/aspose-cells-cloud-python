"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AddTextOptions:
    """Class summary: The features of this class include hands-on learning activities, group projects, interactive discussions, guest speakers, and field trips to real-world applications."""
    name: Optional[str] = None
    data_source: Optional[DataSource] = None
    file_info: Optional[FileInfo] = None
    scope_options: Optional[ScopeOptions] = None
    text: Optional[str] = None
    select_poistion: Optional[str] = None
    select_text: Optional[str] = None
    skip_empty_cells: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.file_info is not None:
            result["FileInfo"] = self.file_info.to_dict()
        if self.scope_options is not None:
            result["ScopeOptions"] = self.scope_options.to_dict()
        if self.text is not None:
            result["Text"] = self.text
        if self.select_poistion is not None:
            result["SelectPoistion"] = self.select_poistion
        if self.select_text is not None:
            result["SelectText"] = self.select_text
        if self.skip_empty_cells is not None:
            result["SkipEmptyCells"] = self.skip_empty_cells
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
