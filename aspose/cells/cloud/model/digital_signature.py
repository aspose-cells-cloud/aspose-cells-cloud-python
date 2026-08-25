"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DigitalSignature:
    """Signature in file."""
    comments: Optional[str] = None
    sign_time: Optional[str] = None
    id_: Optional[str] = None
    password: Optional[str] = None
    image: Optional[List[bytes]] = None
    provider_id: Optional[str] = None
    is_valid: Optional[bool] = None
    x_ad_es_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.comments is not None:
            result["Comments"] = self.comments
        if self.sign_time is not None:
            result["SignTime"] = self.sign_time
        if self.id_ is not None:
            result["Id"] = self.id_
        if self.password is not None:
            result["Password"] = self.password
        if self.image is not None:
            result["Image"] = self.image
        if self.provider_id is not None:
            result["ProviderId"] = self.provider_id
        if self.is_valid is not None:
            result["IsValid"] = self.is_valid
        if self.x_ad_es_type is not None:
            result["XAdESType"] = self.x_ad_es_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
