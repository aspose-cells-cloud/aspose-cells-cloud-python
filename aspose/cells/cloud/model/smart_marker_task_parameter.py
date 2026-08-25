"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SmartMarkerTaskParameter:
    """Represents smart marker task parameter."""
    source_workbook: Optional[FileSource] = None
    destination_workbook: Optional[FileSource] = None
    xml_file: Optional[FileSource] = None
    data_source: Optional[DataSource] = None
    target_data_source: Optional[DataSource] = None
    xml_file_data_source: Optional[DataSource] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.source_workbook is not None:
            result["SourceWorkbook"] = self.source_workbook.to_dict()
        if self.destination_workbook is not None:
            result["DestinationWorkbook"] = self.destination_workbook.to_dict()
        if self.xml_file is not None:
            result["xmlFile"] = self.xml_file.to_dict()
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.target_data_source is not None:
            result["TargetDataSource"] = self.target_data_source.to_dict()
        if self.xml_file_data_source is not None:
            result["XMLFileDataSource"] = self.xml_file_data_source.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
