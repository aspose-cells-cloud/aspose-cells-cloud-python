"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CellsObjectOperateTaskParameter:
    """Represents cells object operate task parameter."""
    operate_object: Optional[OperateObject] = None
    operate_parameter: Optional[OperateParameter] = None
    destination_data_source: Optional[DataSource] = None
    destination_workbook: Optional[FileSource] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.operate_object is not None:
            result["OperateObject"] = self.operate_object.to_dict()
        if self.operate_parameter is not None:
            result["OperateParameter"] = self.operate_parameter.to_dict()
        if self.destination_data_source is not None:
            result["DestinationDataSource"] = self.destination_data_source.to_dict()
        if self.destination_workbook is not None:
            result["DestinationWorkbook"] = self.destination_workbook.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
