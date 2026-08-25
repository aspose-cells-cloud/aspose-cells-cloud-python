"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class SplitTextRequest(RequestOption):
    """Indicates performing text segmentation on the specified area according to the segmentation method, and outputting to the designated interval."""

    def __init__(
        self,
        spreadsheet: FileSource,
        delimiters: str,
        keep_delimiters_in_resulting_cells: Optional[bool] = None,
        keep_delimiters_position: Optional[str] = None,
        how_to_split: Optional[str] = None,
        out_position_range: Optional[str] = None,
        worksheet: Optional[str] = None,
        range_: Optional[str] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        if not delimiters:
            raise ValueError("delimiters is required")
        self.spreadsheet = spreadsheet
        self.delimiters = delimiters
        self.keep_delimiters_in_resulting_cells = keep_delimiters_in_resulting_cells
        self.keep_delimiters_position = keep_delimiters_position
        self.how_to_split = how_to_split
        self.out_position_range = out_position_range
        self.worksheet = worksheet
        self.range_ = range_
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/content/split/text"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["delimiters"] = self.delimiters
        if self.keep_delimiters_in_resulting_cells is not None:
            params["keepDelimitersInResultingCells"] = "true" if self.keep_delimiters_in_resulting_cells else "false"
        if self.keep_delimiters_position:
            params["keepDelimitersPosition"] = self.keep_delimiters_position
        if self.how_to_split:
            params["HowToSplit"] = self.how_to_split
        if self.out_position_range:
            params["outPositionRange"] = self.out_position_range
        if self.worksheet:
            params["worksheet"] = self.worksheet
        if self.range_:
            params["range"] = self.range_
        if self.out_path:
            params["outPath"] = self.out_path
        if self.out_storage_name:
            params["outStorageName"] = self.out_storage_name
        if self.region:
            params["region"] = self.region
        if self.password:
            params["password"] = self.password
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return {"Spreadsheet": self.spreadsheet}
