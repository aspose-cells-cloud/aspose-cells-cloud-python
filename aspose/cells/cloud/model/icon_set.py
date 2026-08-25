"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class IconSet:
    """Describe the IconSet conditional formatting rule. This conditional formatting rule applies icons to cells according to their values."""
    cf_icons: Optional[List[ConditionalFormattingIcon]] = None
    cfvos: Optional[List[ConditionalFormattingValue]] = None
    is_custom: Optional[bool] = None
    reverse: Optional[bool] = None
    show_value: Optional[bool] = None
    icon_set_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.cf_icons is not None:
            result["CfIcons"] = [x.to_dict() for x in self.cf_icons]
        if self.cfvos is not None:
            result["Cfvos"] = [x.to_dict() for x in self.cfvos]
        if self.is_custom is not None:
            result["IsCustom"] = self.is_custom
        if self.reverse is not None:
            result["Reverse"] = self.reverse
        if self.show_value is not None:
            result["ShowValue"] = self.show_value
        if self.icon_set_type is not None:
            result["IconSetType"] = self.icon_set_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
