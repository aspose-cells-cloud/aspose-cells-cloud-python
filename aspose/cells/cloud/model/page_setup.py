"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PageSetup:
    """excel print page setting"""
    black_and_white: Optional[bool] = None
    bottom_margin: Optional[float] = None
    center_horizontally: Optional[bool] = None
    center_vertically: Optional[bool] = None
    first_page_number: Optional[int] = None
    fit_to_pages_tall: Optional[int] = None
    fit_to_pages_wide: Optional[int] = None
    footer_margin: Optional[float] = None
    header_margin: Optional[float] = None
    is_auto_first_page_number: Optional[bool] = None
    is_hf_align_margins: Optional[bool] = None
    is_hf_diff_first: Optional[bool] = None
    is_hf_diff_odd_even: Optional[bool] = None
    is_hf_scale_with_doc: Optional[bool] = None
    is_percent_scale: Optional[bool] = None
    left_margin: Optional[float] = None
    order: Optional[str] = None
    orientation: Optional[str] = None
    paper_size: Optional[str] = None
    print_area: Optional[str] = None
    print_comments: Optional[str] = None
    print_copies: Optional[int] = None
    print_draft: Optional[bool] = None
    print_errors: Optional[str] = None
    print_gridlines: Optional[bool] = None
    print_headings: Optional[bool] = None
    print_quality: Optional[int] = None
    print_title_columns: Optional[str] = None
    print_title_rows: Optional[str] = None
    right_margin: Optional[float] = None
    top_margin: Optional[float] = None
    zoom: Optional[int] = None
    header: Optional[List[PageSection]] = None
    footer: Optional[List[PageSection]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.black_and_white is not None:
            result["BlackAndWhite"] = self.black_and_white
        if self.bottom_margin is not None:
            result["BottomMargin"] = self.bottom_margin
        if self.center_horizontally is not None:
            result["CenterHorizontally"] = self.center_horizontally
        if self.center_vertically is not None:
            result["CenterVertically"] = self.center_vertically
        if self.first_page_number is not None:
            result["FirstPageNumber"] = self.first_page_number
        if self.fit_to_pages_tall is not None:
            result["FitToPagesTall"] = self.fit_to_pages_tall
        if self.fit_to_pages_wide is not None:
            result["FitToPagesWide"] = self.fit_to_pages_wide
        if self.footer_margin is not None:
            result["FooterMargin"] = self.footer_margin
        if self.header_margin is not None:
            result["HeaderMargin"] = self.header_margin
        if self.is_auto_first_page_number is not None:
            result["IsAutoFirstPageNumber"] = self.is_auto_first_page_number
        if self.is_hf_align_margins is not None:
            result["IsHFAlignMargins"] = self.is_hf_align_margins
        if self.is_hf_diff_first is not None:
            result["IsHFDiffFirst"] = self.is_hf_diff_first
        if self.is_hf_diff_odd_even is not None:
            result["IsHFDiffOddEven"] = self.is_hf_diff_odd_even
        if self.is_hf_scale_with_doc is not None:
            result["IsHFScaleWithDoc"] = self.is_hf_scale_with_doc
        if self.is_percent_scale is not None:
            result["IsPercentScale"] = self.is_percent_scale
        if self.left_margin is not None:
            result["LeftMargin"] = self.left_margin
        if self.order is not None:
            result["Order"] = self.order
        if self.orientation is not None:
            result["Orientation"] = self.orientation
        if self.paper_size is not None:
            result["PaperSize"] = self.paper_size
        if self.print_area is not None:
            result["PrintArea"] = self.print_area
        if self.print_comments is not None:
            result["PrintComments"] = self.print_comments
        if self.print_copies is not None:
            result["PrintCopies"] = self.print_copies
        if self.print_draft is not None:
            result["PrintDraft"] = self.print_draft
        if self.print_errors is not None:
            result["PrintErrors"] = self.print_errors
        if self.print_gridlines is not None:
            result["PrintGridlines"] = self.print_gridlines
        if self.print_headings is not None:
            result["PrintHeadings"] = self.print_headings
        if self.print_quality is not None:
            result["PrintQuality"] = self.print_quality
        if self.print_title_columns is not None:
            result["PrintTitleColumns"] = self.print_title_columns
        if self.print_title_rows is not None:
            result["PrintTitleRows"] = self.print_title_rows
        if self.right_margin is not None:
            result["RightMargin"] = self.right_margin
        if self.top_margin is not None:
            result["TopMargin"] = self.top_margin
        if self.zoom is not None:
            result["Zoom"] = self.zoom
        if self.header is not None:
            result["Header"] = [x.to_dict() for x in self.header]
        if self.footer is not None:
            result["Footer"] = [x.to_dict() for x in self.footer]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
