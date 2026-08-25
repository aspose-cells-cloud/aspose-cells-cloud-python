"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TrimContentOptions:
    """TrimContentOptions."""
    data_source: Optional[DataSource] = None
    file_info: Optional[FileInfo] = None
    trim_content: Optional[str] = None
    trim_leading: Optional[bool] = None
    trim_trailing: Optional[bool] = None
    trim_space_between_word_to1: Optional[bool] = None
    trim_non_breaking_spaces: Optional[bool] = None
    remove_extra_line_breaks: Optional[bool] = None
    remove_all_line_breaks: Optional[bool] = None
    scope_options: Optional[ScopeOptions] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.file_info is not None:
            result["FileInfo"] = self.file_info.to_dict()
        if self.trim_content is not None:
            result["TrimContent"] = self.trim_content
        if self.trim_leading is not None:
            result["TrimLeading"] = self.trim_leading
        if self.trim_trailing is not None:
            result["TrimTrailing"] = self.trim_trailing
        if self.trim_space_between_word_to1 is not None:
            result["TrimSpaceBetweenWordTo1"] = self.trim_space_between_word_to1
        if self.trim_non_breaking_spaces is not None:
            result["TrimNonBreakingSpaces"] = self.trim_non_breaking_spaces
        if self.remove_extra_line_breaks is not None:
            result["RemoveExtraLineBreaks"] = self.remove_extra_line_breaks
        if self.remove_all_line_breaks is not None:
            result["RemoveAllLineBreaks"] = self.remove_all_line_breaks
        if self.scope_options is not None:
            result["ScopeOptions"] = self.scope_options.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
