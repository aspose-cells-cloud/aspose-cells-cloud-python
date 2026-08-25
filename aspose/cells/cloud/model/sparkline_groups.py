"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SparklineGroups:
    """Encapsulates a collection of Aspose.Cells.Charts.SparklineGroup objects."""
    sparkline_group_list: Optional[List[SparklineGroup]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.sparkline_group_list is not None:
            result["SparklineGroupList"] = [x.to_dict() for x in self.sparkline_group_list]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
