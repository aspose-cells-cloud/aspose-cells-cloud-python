"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SeriesItems:
    """Class Summary: - Features: Active class participation, group projects, quizzes, and final exam."""
    category_data: Optional[str] = None
    is_color_varied: Optional[bool] = None
    second_catergory_data: Optional[str] = None
    series_list: Optional[List[Series]] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.category_data is not None:
            result["CategoryData"] = self.category_data
        if self.is_color_varied is not None:
            result["IsColorVaried"] = self.is_color_varied
        if self.second_catergory_data is not None:
            result["SecondCatergoryData"] = self.second_catergory_data
        if self.series_list is not None:
            result["SeriesList"] = [x.to_dict() for x in self.series_list]
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
