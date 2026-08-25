"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ConvertTaskParameter:
    """Represents convert task parameter."""
    data_source: Optional[DataSource] = None
    workbook: Optional[FileSource] = None
    destination_file: Optional[str] = None
    region: Optional[str] = None
    save_options: Optional[SaveOptions] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.workbook is not None:
            result["Workbook"] = self.workbook.to_dict()
        if self.destination_file is not None:
            result["DestinationFile"] = self.destination_file
        if self.region is not None:
            result["Region"] = self.region
        if self.save_options is not None:
            result["SaveOptions"] = self.save_options.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
