"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ImportCSVDataOption:
    """I'm happy to help! Could you please provide me with the features you would like me to summarize into a class summary?"""
    separator_string: Optional[str] = None
    convert_numeric_data: Optional[bool] = None
    first_row: Optional[int] = None
    first_column: Optional[int] = None
    source_file: Optional[str] = None
    custom_parsers: Optional[List[CustomParserConfig]] = None
    destination_worksheet: Optional[str] = None
    is_insert: Optional[bool] = None
    import_data_type: Optional[str] = None
    data_source: Optional[DataSource] = None
    source: Optional[FileSource] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.separator_string is not None:
            result["SeparatorString"] = self.separator_string
        if self.convert_numeric_data is not None:
            result["ConvertNumericData"] = self.convert_numeric_data
        if self.first_row is not None:
            result["FirstRow"] = self.first_row
        if self.first_column is not None:
            result["FirstColumn"] = self.first_column
        if self.source_file is not None:
            result["SourceFile"] = self.source_file
        if self.custom_parsers is not None:
            result["CustomParsers"] = [x.to_dict() for x in self.custom_parsers]
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
