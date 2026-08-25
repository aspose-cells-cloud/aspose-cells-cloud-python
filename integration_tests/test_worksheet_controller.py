"""Integration tests for WorksheetController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteUnprotectWorksheetRequest
from aspose.cells.cloud.request import DeleteWorksheetBackgroundRequest
from aspose.cells.cloud.request import DeleteWorksheetCommentRequest
from aspose.cells.cloud.request import DeleteWorksheetCommentsRequest
from aspose.cells.cloud.request import DeleteWorksheetFreezePanesRequest
from aspose.cells.cloud.request import DeleteWorksheetRequest
from aspose.cells.cloud.request import DeleteWorksheetsRequest
from aspose.cells.cloud.request import GetNamedRangeValueRequest
from aspose.cells.cloud.request import GetNamedRangesRequest
from aspose.cells.cloud.request import GetWorksheetCalculateFormulaRequest
from aspose.cells.cloud.request import GetWorksheetCommentRequest
from aspose.cells.cloud.request import GetWorksheetCommentsRequest
from aspose.cells.cloud.request import GetWorksheetMergedCellRequest
from aspose.cells.cloud.request import GetWorksheetMergedCellsRequest
from aspose.cells.cloud.request import GetWorksheetPageCountRequest
from aspose.cells.cloud.request import GetWorksheetTextItemsRequest
from aspose.cells.cloud.request import GetWorksheetWithFormatRequest
from aspose.cells.cloud.request import GetWorksheetsRequest
from aspose.cells.cloud.request import PostAutofitWorksheetColumnsRequest
from aspose.cells.cloud.request import PostAutofitWorksheetRowRequest
from aspose.cells.cloud.request import PostAutofitWorksheetRowsRequest
from aspose.cells.cloud.request import PostCopyWorksheetRequest
from aspose.cells.cloud.request import PostMoveWorksheetRequest
from aspose.cells.cloud.request import PostRenameWorksheetRequest
from aspose.cells.cloud.request import PostUpdateWorksheetPropertyRequest
from aspose.cells.cloud.request import PostUpdateWorksheetZoomRequest
from aspose.cells.cloud.request import PostWorksheetCalculateFormulaRequest
from aspose.cells.cloud.request import PostWorksheetCommentRequest
from aspose.cells.cloud.request import PostWorksheetRangeSortRequest
from aspose.cells.cloud.request import PostWorksheetTextReplaceRequest
from aspose.cells.cloud.request import PostWorksheetTextSearchRequest
from aspose.cells.cloud.request import PutActiveWorksheetRequest
from aspose.cells.cloud.request import PutAddNewWorksheetRequest
from aspose.cells.cloud.request import PutChangeVisibilityWorksheetRequest
from aspose.cells.cloud.request import PutInsertNewWorksheetRequest
from aspose.cells.cloud.request import PutProtectWorksheetRequest
from aspose.cells.cloud.request import PutWorksheetBackgroundRequest
from aspose.cells.cloud.request import PutWorksheetCommentRequest
from aspose.cells.cloud.request import PutWorksheetFreezePanesRequest

from aspose.cells.cloud.model import Comment
from aspose.cells.cloud.model import CopyOptions
from aspose.cells.cloud.model import DataSorter
from aspose.cells.cloud.model import MatchConditionRequest
from aspose.cells.cloud.model import ProtectSheetParameter
from aspose.cells.cloud.model import Worksheet
from aspose.cells.cloud.model import WorksheetMovingRequest


def test_get_worksheets(client):
    """Test for GetWorksheet of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetsRequest(
        name="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_with_format(client):
    """Test for GetWorksheetWithFormat of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetWithFormatRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        format_="png",
        page_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_put_change_visibility_worksheet(client):
    """Test for PutChangeVisibilityWorksheet of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutChangeVisibilityWorksheetRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        is_visible=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_active_worksheet(client):
    """Test for PutActiveWorksheet of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutActiveWorksheetRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_insert_new_worksheet(client):
    """Test for PutInsertNewWorksheet of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutInsertNewWorksheetRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        index=1,
        sheettype="VB",
        newsheetname="VBASheet",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_add_new_worksheet(client):
    """Test for PutAddNewWorksheet of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutAddNewWorksheetRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        position=0,
        sheettype="VB",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet(client):
    """Test for DeleteWorksheet of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheets(client):
    """Test for DeleteWorksheet of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetsRequest(
        name="Book1.xlsx",
        match_condition=MatchConditionRequest(regex_pattern='{*}'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_move_worksheet(client):
    """Test for PostMoveWorksheet of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostMoveWorksheetRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        moving=WorksheetMovingRequest(destination_worksheet='Sheet4', position='After'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_protect_worksheet(client):
    """Test for PutProtectWorksheet of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutProtectWorksheetRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        protect_parameter=ProtectSheetParameter(protection_type='ALL', password='123'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_unprotect_worksheet(client):
    """Test for DeleteUnprotectWorksheet of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteUnprotectWorksheetRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        protect_parameter=ProtectSheetParameter(protection_type='ALL', password='123'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_text_items(client):
    """Test for GetWorksheetTextItems of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetTextItemsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_comments(client):
    """Test for GetWorksheetComments of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetCommentsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_comment(client):
    """Test for GetWorksheetComment of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetCommentRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_name="B3",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_comment(client):
    """Test for PutWorksheetComment of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetCommentRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_name="C1",
        comment=Comment(author='aspose cells developer', note='aspose cells cloud api add comment.'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_comment(client):
    """Test for PostWorksheetComment of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetCommentRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_name="B3",
        comment=Comment(author='aspose cells developer', note='aspose cells cloud api update comment.'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_comment(client):
    """Test for DeleteWorksheetComment of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetCommentRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_name="B3",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_comments(client):
    """Test for DeleteWorksheetComments of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetCommentsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_merged_cells(client):
    """Test for GetWorksheetMergedCells of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetMergedCellsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_merged_cell(client):
    """Test for GetWorksheetMergedCell of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetMergedCellRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        merged_cell_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_calculate_formula(client):
    """Test for GetWorksheetCalculateFormula of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetCalculateFormulaRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        formula="=NOW()",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_calculate_formula(client):
    """Test for PostWorksheetCalculateFormula of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetCalculateFormulaRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        formula="=NOW()",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_text_search(client):
    """Test for PostWorksheetTextSearch of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetTextSearchRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        text="123",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_text_replace(client):
    """Test for PostWorksheetTextReplace of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetTextReplaceRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        old_value="123",
        new_value="456",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_range_sort(client):
    """Test for PostWorksheetRangeSort of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetRangeSortRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_area="A1:C10",
        data_sorter=DataSorter(case_sensitive=True),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_autofit_worksheet_row(client):
    """Test for PostAutofitWorksheetRow of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostAutofitWorksheetRowRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        row_index=1,
        first_column=1,
        last_column=8,
        row_count=1,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_autofit_worksheet_rows(client):
    """Test for PostAutofitWorksheetRows of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostAutofitWorksheetRowsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        start_row=1,
        end_row=9,
        only_auto=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_autofit_worksheet_columns(client):
    """Test for PostAutofitWorksheetColumns of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostAutofitWorksheetColumnsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        start_column=1,
        end_column=9,
        only_auto=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_background(client):
    """Test for PutWorksheetBackground of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/WaterMark.png", "TestData/In/WaterMark.png", storage_name=None)

    request = PutWorksheetBackgroundRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        pic_path="TestData/In/WaterMark.png",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_background(client):
    """Test for DeleteWorksheetBackground of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetBackgroundRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_freeze_panes(client):
    """Test for PutWorksheetFreezePanes of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetFreezePanesRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        row=1,
        column=1,
        freezed_rows=4,
        freezed_columns=5,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_freeze_panes(client):
    """Test for DeleteWorksheetFreezePanes of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetFreezePanesRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        row=1,
        column=1,
        freezed_rows=4,
        freezed_columns=5,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_copy_worksheet(client):
    """Test for PostCopyWorksheet of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostCopyWorksheetRequest(
        name="Book1.xlsx",
        sheet_name="Sheet15",
        source_sheet="Sheet6",
        options=CopyOptions(column_character_width=True),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_rename_worksheet(client):
    """Test for PostRenameWorksheet of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostRenameWorksheetRequest(
        name="Book1.xlsx",
        sheet_name="Sheet5",
        newname="Sheet55",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_update_worksheet_property(client):
    """Test for PostUpdateWorksheetProperty of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostUpdateWorksheetPropertyRequest(
        name="Book1.xlsx",
        sheet_name="Sheet5",
        sheet=Worksheet(name='sheet65', is_gridlines_visible=True),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_named_ranges(client):
    """Test for GetNamedRanges of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetNamedRangesRequest(
        name="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_named_range_value(client):
    """Test for GetNamedRangeValue of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetNamedRangeValueRequest(
        name="Book1.xlsx",
        namerange="Name_2",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_update_worksheet_zoom(client):
    """Test for PostUpdateWorksheetZoom of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostUpdateWorksheetZoomRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        value=90,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_page_count(client):
    """Test for GetWorksheetPageCount of WorksheetController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetPageCountRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None
