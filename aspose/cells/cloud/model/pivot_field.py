"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PivotField:
    """Represents a field in a PivotTable report."""
    auto_show_count: Optional[int] = None
    auto_show_field: Optional[int] = None
    auto_sort_field: Optional[int] = None
    base_field: Optional[int] = None
    base_index: Optional[int] = None
    base_item: Optional[int] = None
    base_item_position: Optional[str] = None
    current_page_item: Optional[int] = None
    data_display_format: Optional[str] = None
    display_name: Optional[str] = None
    drag_to_column: Optional[bool] = None
    drag_to_data: Optional[bool] = None
    drag_to_hide: Optional[bool] = None
    drag_to_page: Optional[bool] = None
    drag_to_row: Optional[bool] = None
    function: Optional[str] = None
    insert_blank_row: Optional[bool] = None
    is_ascend_show: Optional[bool] = None
    is_ascend_sort: Optional[bool] = None
    is_auto_show: Optional[bool] = None
    is_auto_sort: Optional[bool] = None
    is_auto_subtotals: Optional[bool] = None
    is_calculated_field: Optional[bool] = None
    is_include_new_items_in_filter: Optional[bool] = None
    is_insert_page_breaks_between_items: Optional[bool] = None
    is_multiple_item_selection_allowed: Optional[bool] = None
    is_repeat_item_labels: Optional[bool] = None
    item_count: Optional[int] = None
    items: Optional[List[str]] = None
    name: Optional[str] = None
    number: Optional[int] = None
    number_format: Optional[str] = None
    original_items: Optional[List[str]] = None
    pivot_items: Optional[List[PivotItem]] = None
    position: Optional[int] = None
    show_all_items: Optional[bool] = None
    show_compact: Optional[bool] = None
    show_in_outline_form: Optional[bool] = None
    show_subtotal_at_top: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.auto_show_count is not None:
            result["AutoShowCount"] = self.auto_show_count
        if self.auto_show_field is not None:
            result["AutoShowField"] = self.auto_show_field
        if self.auto_sort_field is not None:
            result["AutoSortField"] = self.auto_sort_field
        if self.base_field is not None:
            result["BaseField"] = self.base_field
        if self.base_index is not None:
            result["BaseIndex"] = self.base_index
        if self.base_item is not None:
            result["BaseItem"] = self.base_item
        if self.base_item_position is not None:
            result["BaseItemPosition"] = self.base_item_position
        if self.current_page_item is not None:
            result["CurrentPageItem"] = self.current_page_item
        if self.data_display_format is not None:
            result["DataDisplayFormat"] = self.data_display_format
        if self.display_name is not None:
            result["DisplayName"] = self.display_name
        if self.drag_to_column is not None:
            result["DragToColumn"] = self.drag_to_column
        if self.drag_to_data is not None:
            result["DragToData"] = self.drag_to_data
        if self.drag_to_hide is not None:
            result["DragToHide"] = self.drag_to_hide
        if self.drag_to_page is not None:
            result["DragToPage"] = self.drag_to_page
        if self.drag_to_row is not None:
            result["DragToRow"] = self.drag_to_row
        if self.function is not None:
            result["Function"] = self.function
        if self.insert_blank_row is not None:
            result["InsertBlankRow"] = self.insert_blank_row
        if self.is_ascend_show is not None:
            result["IsAscendShow"] = self.is_ascend_show
        if self.is_ascend_sort is not None:
            result["IsAscendSort"] = self.is_ascend_sort
        if self.is_auto_show is not None:
            result["IsAutoShow"] = self.is_auto_show
        if self.is_auto_sort is not None:
            result["IsAutoSort"] = self.is_auto_sort
        if self.is_auto_subtotals is not None:
            result["IsAutoSubtotals"] = self.is_auto_subtotals
        if self.is_calculated_field is not None:
            result["IsCalculatedField"] = self.is_calculated_field
        if self.is_include_new_items_in_filter is not None:
            result["IsIncludeNewItemsInFilter"] = self.is_include_new_items_in_filter
        if self.is_insert_page_breaks_between_items is not None:
            result["IsInsertPageBreaksBetweenItems"] = self.is_insert_page_breaks_between_items
        if self.is_multiple_item_selection_allowed is not None:
            result["IsMultipleItemSelectionAllowed"] = self.is_multiple_item_selection_allowed
        if self.is_repeat_item_labels is not None:
            result["IsRepeatItemLabels"] = self.is_repeat_item_labels
        if self.item_count is not None:
            result["ItemCount"] = self.item_count
        if self.items is not None:
            result["Items"] = self.items
        if self.name is not None:
            result["Name"] = self.name
        if self.number is not None:
            result["Number"] = self.number
        if self.number_format is not None:
            result["NumberFormat"] = self.number_format
        if self.original_items is not None:
            result["OriginalItems"] = self.original_items
        if self.pivot_items is not None:
            result["PivotItems"] = [x.to_dict() for x in self.pivot_items]
        if self.position is not None:
            result["Position"] = self.position
        if self.show_all_items is not None:
            result["ShowAllItems"] = self.show_all_items
        if self.show_compact is not None:
            result["ShowCompact"] = self.show_compact
        if self.show_in_outline_form is not None:
            result["ShowInOutlineForm"] = self.show_in_outline_form
        if self.show_subtotal_at_top is not None:
            result["ShowSubtotalAtTop"] = self.show_subtotal_at_top
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
