"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PivotTable:
    """Summary description for PivotTable."""
    alt_text_description: Optional[str] = None
    alt_text_title: Optional[str] = None
    auto_format_type: Optional[str] = None
    base_fields: Optional[List[PivotField]] = None
    column_fields: Optional[List[PivotField]] = None
    column_grand: Optional[bool] = None
    column_header_caption: Optional[str] = None
    column_range: Optional[CellArea] = None
    custom_list_sort: Optional[bool] = None
    data_body_range: Optional[CellArea] = None
    data_field: Optional[PivotField] = None
    data_fields: Optional[List[PivotField]] = None
    data_source: Optional[List[str]] = None
    display_error_string: Optional[bool] = None
    display_immediate_items: Optional[bool] = None
    display_null_string: Optional[bool] = None
    enable_data_value_editing: Optional[bool] = None
    enable_drilldown: Optional[bool] = None
    enable_field_dialog: Optional[bool] = None
    enable_field_list: Optional[bool] = None
    enable_wizard: Optional[bool] = None
    error_string: Optional[str] = None
    field_list_sort_ascending: Optional[bool] = None
    grand_total_name: Optional[str] = None
    has_blank_rows: Optional[bool] = None
    indent: Optional[int] = None
    is_auto_format: Optional[bool] = None
    is_grid_drop_zones: Optional[bool] = None
    is_multiple_field_filters: Optional[bool] = None
    is_selected: Optional[bool] = None
    item_print_titles: Optional[bool] = None
    manual_update: Optional[bool] = None
    merge_labels: Optional[bool] = None
    missing_items_limit: Optional[str] = None
    name: Optional[str] = None
    null_string: Optional[str] = None
    page_field_order: Optional[str] = None
    page_fields: Optional[List[PivotField]] = None
    page_field_wrap_count: Optional[int] = None
    pivot_filters: Optional[List[PivotFilter]] = None
    pivot_table_style_name: Optional[str] = None
    pivot_table_style_type: Optional[str] = None
    preserve_formatting: Optional[bool] = None
    print_drill: Optional[bool] = None
    print_titles: Optional[bool] = None
    refresh_data_flag: Optional[bool] = None
    refresh_data_on_opening_file: Optional[bool] = None
    row_fields: Optional[List[PivotField]] = None
    row_grand: Optional[bool] = None
    row_header_caption: Optional[str] = None
    row_range: Optional[CellArea] = None
    save_data: Optional[bool] = None
    show_data_tips: Optional[bool] = None
    show_drill: Optional[bool] = None
    show_empty_col: Optional[bool] = None
    show_empty_row: Optional[bool] = None
    show_member_property_tips: Optional[bool] = None
    show_pivot_style_column_header: Optional[bool] = None
    show_pivot_style_column_stripes: Optional[bool] = None
    show_pivot_style_last_column: Optional[bool] = None
    show_pivot_style_row_header: Optional[bool] = None
    show_pivot_style_row_stripes: Optional[bool] = None
    show_row_header_caption: Optional[bool] = None
    show_values_row: Optional[bool] = None
    subtotal_hidden_page_items: Optional[bool] = None
    table_range1: Optional[CellArea] = None
    table_range2: Optional[CellArea] = None
    tag: Optional[str] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.alt_text_description is not None:
            result["AltTextDescription"] = self.alt_text_description
        if self.alt_text_title is not None:
            result["AltTextTitle"] = self.alt_text_title
        if self.auto_format_type is not None:
            result["AutoFormatType"] = self.auto_format_type
        if self.base_fields is not None:
            result["BaseFields"] = [x.to_dict() for x in self.base_fields]
        if self.column_fields is not None:
            result["ColumnFields"] = [x.to_dict() for x in self.column_fields]
        if self.column_grand is not None:
            result["ColumnGrand"] = self.column_grand
        if self.column_header_caption is not None:
            result["ColumnHeaderCaption"] = self.column_header_caption
        if self.column_range is not None:
            result["ColumnRange"] = self.column_range.to_dict()
        if self.custom_list_sort is not None:
            result["CustomListSort"] = self.custom_list_sort
        if self.data_body_range is not None:
            result["DataBodyRange"] = self.data_body_range.to_dict()
        if self.data_field is not None:
            result["DataField"] = self.data_field.to_dict()
        if self.data_fields is not None:
            result["DataFields"] = [x.to_dict() for x in self.data_fields]
        if self.data_source is not None:
            result["DataSource"] = self.data_source
        if self.display_error_string is not None:
            result["DisplayErrorString"] = self.display_error_string
        if self.display_immediate_items is not None:
            result["DisplayImmediateItems"] = self.display_immediate_items
        if self.display_null_string is not None:
            result["DisplayNullString"] = self.display_null_string
        if self.enable_data_value_editing is not None:
            result["EnableDataValueEditing"] = self.enable_data_value_editing
        if self.enable_drilldown is not None:
            result["EnableDrilldown"] = self.enable_drilldown
        if self.enable_field_dialog is not None:
            result["EnableFieldDialog"] = self.enable_field_dialog
        if self.enable_field_list is not None:
            result["EnableFieldList"] = self.enable_field_list
        if self.enable_wizard is not None:
            result["EnableWizard"] = self.enable_wizard
        if self.error_string is not None:
            result["ErrorString"] = self.error_string
        if self.field_list_sort_ascending is not None:
            result["FieldListSortAscending"] = self.field_list_sort_ascending
        if self.grand_total_name is not None:
            result["GrandTotalName"] = self.grand_total_name
        if self.has_blank_rows is not None:
            result["HasBlankRows"] = self.has_blank_rows
        if self.indent is not None:
            result["Indent"] = self.indent
        if self.is_auto_format is not None:
            result["IsAutoFormat"] = self.is_auto_format
        if self.is_grid_drop_zones is not None:
            result["IsGridDropZones"] = self.is_grid_drop_zones
        if self.is_multiple_field_filters is not None:
            result["IsMultipleFieldFilters"] = self.is_multiple_field_filters
        if self.is_selected is not None:
            result["IsSelected"] = self.is_selected
        if self.item_print_titles is not None:
            result["ItemPrintTitles"] = self.item_print_titles
        if self.manual_update is not None:
            result["ManualUpdate"] = self.manual_update
        if self.merge_labels is not None:
            result["MergeLabels"] = self.merge_labels
        if self.missing_items_limit is not None:
            result["MissingItemsLimit"] = self.missing_items_limit
        if self.name is not None:
            result["Name"] = self.name
        if self.null_string is not None:
            result["NullString"] = self.null_string
        if self.page_field_order is not None:
            result["PageFieldOrder"] = self.page_field_order
        if self.page_fields is not None:
            result["PageFields"] = [x.to_dict() for x in self.page_fields]
        if self.page_field_wrap_count is not None:
            result["PageFieldWrapCount"] = self.page_field_wrap_count
        if self.pivot_filters is not None:
            result["PivotFilters"] = [x.to_dict() for x in self.pivot_filters]
        if self.pivot_table_style_name is not None:
            result["PivotTableStyleName"] = self.pivot_table_style_name
        if self.pivot_table_style_type is not None:
            result["PivotTableStyleType"] = self.pivot_table_style_type
        if self.preserve_formatting is not None:
            result["PreserveFormatting"] = self.preserve_formatting
        if self.print_drill is not None:
            result["PrintDrill"] = self.print_drill
        if self.print_titles is not None:
            result["PrintTitles"] = self.print_titles
        if self.refresh_data_flag is not None:
            result["RefreshDataFlag"] = self.refresh_data_flag
        if self.refresh_data_on_opening_file is not None:
            result["RefreshDataOnOpeningFile"] = self.refresh_data_on_opening_file
        if self.row_fields is not None:
            result["RowFields"] = [x.to_dict() for x in self.row_fields]
        if self.row_grand is not None:
            result["RowGrand"] = self.row_grand
        if self.row_header_caption is not None:
            result["RowHeaderCaption"] = self.row_header_caption
        if self.row_range is not None:
            result["RowRange"] = self.row_range.to_dict()
        if self.save_data is not None:
            result["SaveData"] = self.save_data
        if self.show_data_tips is not None:
            result["ShowDataTips"] = self.show_data_tips
        if self.show_drill is not None:
            result["ShowDrill"] = self.show_drill
        if self.show_empty_col is not None:
            result["ShowEmptyCol"] = self.show_empty_col
        if self.show_empty_row is not None:
            result["ShowEmptyRow"] = self.show_empty_row
        if self.show_member_property_tips is not None:
            result["ShowMemberPropertyTips"] = self.show_member_property_tips
        if self.show_pivot_style_column_header is not None:
            result["ShowPivotStyleColumnHeader"] = self.show_pivot_style_column_header
        if self.show_pivot_style_column_stripes is not None:
            result["ShowPivotStyleColumnStripes"] = self.show_pivot_style_column_stripes
        if self.show_pivot_style_last_column is not None:
            result["ShowPivotStyleLastColumn"] = self.show_pivot_style_last_column
        if self.show_pivot_style_row_header is not None:
            result["ShowPivotStyleRowHeader"] = self.show_pivot_style_row_header
        if self.show_pivot_style_row_stripes is not None:
            result["ShowPivotStyleRowStripes"] = self.show_pivot_style_row_stripes
        if self.show_row_header_caption is not None:
            result["ShowRowHeaderCaption"] = self.show_row_header_caption
        if self.show_values_row is not None:
            result["ShowValuesRow"] = self.show_values_row
        if self.subtotal_hidden_page_items is not None:
            result["SubtotalHiddenPageItems"] = self.subtotal_hidden_page_items
        if self.table_range1 is not None:
            result["TableRange1"] = self.table_range1.to_dict()
        if self.table_range2 is not None:
            result["TableRange2"] = self.table_range2.to_dict()
        if self.tag is not None:
            result["Tag"] = self.tag
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
