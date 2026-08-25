"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ImportStringArrayOption:
    """I'm happy to help! Could you please provide me with the features you would like me to summarize for the class?"""
    first_row: Optional[int] = None
    first_column: Optional[int] = None
    is_vertical: Optional[bool] = None
    data: Optional[List[str]] = None
    destination_worksheet: Optional[str] = None
    is_insert: Optional[bool] = None
    import_data_type: Optional[str] = None
    data_source: Optional[DataSource] = None
    source: Optional[FileSource] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.first_row is not None:
            result["FirstRow"] = self.first_row
        if self.first_column is not None:
            result["FirstColumn"] = self.first_column
        if self.is_vertical is not None:
            result["IsVertical"] = self.is_vertical
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
