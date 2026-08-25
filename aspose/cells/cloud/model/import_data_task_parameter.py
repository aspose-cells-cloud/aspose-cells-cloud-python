"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ImportDataTaskParameter:
    """Represents import data task parameter."""
    data_source: Optional[DataSource] = None
    workbook: Optional[FileSource] = None
    import_option: Optional[ImportOption] = None
    target_data_source: Optional[DataSource] = None
    destination_workbook: Optional[FileSource] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.workbook is not None:
            result["Workbook"] = self.workbook.to_dict()
        if self.import_option is not None:
            result["ImportOption"] = self.import_option.to_dict()
        if self.target_data_source is not None:
            result["TargetDataSource"] = self.target_data_source.to_dict()
        if self.destination_workbook is not None:
            result["DestinationWorkbook"] = self.destination_workbook.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
