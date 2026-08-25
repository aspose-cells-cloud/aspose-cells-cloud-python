"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SplitTextOptions:
    """Appliance features: 1. Automatic defrost system 2. Energy-efficient LED lighting 3. Adjustable glass shelves 4. Ice and water dispenser with filtration system"""
    name: Optional[str] = None
    data_source: Optional[DataSource] = None
    file_info: Optional[FileInfo] = None
    worksheet: Optional[str] = None
    range_: Optional[str] = None
    split_delimiters_type: Optional[str] = None
    custom_delimiter: Optional[str] = None
    keep_delimiters_in_resulting_cells: Optional[bool] = None
    keep_delimiters_position: Optional[str] = None
    how_to_split: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.file_info is not None:
            result["FileInfo"] = self.file_info.to_dict()
        if self.worksheet is not None:
            result["Worksheet"] = self.worksheet
        if self.range_ is not None:
            result["Range"] = self.range_
        if self.split_delimiters_type is not None:
            result["SplitDelimitersType"] = self.split_delimiters_type
        if self.custom_delimiter is not None:
            result["CustomDelimiter"] = self.custom_delimiter
        if self.keep_delimiters_in_resulting_cells is not None:
            result["KeepDelimitersInResultingCells"] = self.keep_delimiters_in_resulting_cells
        if self.keep_delimiters_position is not None:
            result["KeepDelimitersPosition"] = self.keep_delimiters_position
        if self.how_to_split is not None:
            result["HowToSplit"] = self.how_to_split
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
