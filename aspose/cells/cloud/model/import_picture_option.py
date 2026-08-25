"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ImportPictureOption:
    """Class summary: The features of the topic were explored, discussing its components, patterns, and significance."""
    upper_left_row: Optional[int] = None
    upper_left_column: Optional[int] = None
    lower_right_row: Optional[int] = None
    lower_right_column: Optional[int] = None
    filename: Optional[str] = None
    data: Optional[str] = None
    destination_worksheet: Optional[str] = None
    is_insert: Optional[bool] = None
    import_data_type: Optional[str] = None
    data_source: Optional[DataSource] = None
    source: Optional[FileSource] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.upper_left_row is not None:
            result["UpperLeftRow"] = self.upper_left_row
        if self.upper_left_column is not None:
            result["UpperLeftColumn"] = self.upper_left_column
        if self.lower_right_row is not None:
            result["LowerRightRow"] = self.lower_right_row
        if self.lower_right_column is not None:
            result["LowerRightColumn"] = self.lower_right_column
        if self.filename is not None:
            result["Filename"] = self.filename
        if self.data is not None:
            result["Data"] = self.data
        if self.destination_worksheet is not None:
            result["DestinationWorksheet"] = self.destination_worksheet
        if self.is_insert is not None:
            result["IsInsert"] = self.is_insert
        if self.import_data_type is not None:
            result["ImportDataType"] = self.import_data_type
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.source is not None:
            result["Source"] = self.source.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
