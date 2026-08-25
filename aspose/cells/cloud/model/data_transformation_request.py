"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataTransformationRequest:
    """Data Transformation Request"""
    file_info: Optional[FileInfo] = None
    data_source: Optional[DataSource] = None
    load_data: Optional[LoadData] = None
    applied_steps: Optional[List[AppliedStep]] = None
    region: Optional[str] = None
    out_format: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.file_info is not None:
            result["FileInfo"] = self.file_info.to_dict()
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.load_data is not None:
            result["LoadData"] = self.load_data.to_dict()
        if self.applied_steps is not None:
            result["AppliedSteps"] = [x.to_dict() for x in self.applied_steps]
        if self.region is not None:
            result["Region"] = self.region
        if self.out_format is not None:
            result["OutFormat"] = self.out_format
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
