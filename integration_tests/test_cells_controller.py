"""Integration tests for CellsController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteWorksheetColumnsRequest
from aspose.cells.cloud.request import DeleteWorksheetRowRequest
from aspose.cells.cloud.request import DeleteWorksheetRowsRequest
from aspose.cells.cloud.request import GetCellHtmlStringRequest
from aspose.cells.cloud.request import GetWorksheetCellRequest
from aspose.cells.cloud.request import GetWorksheetCellStyleRequest
from aspose.cells.cloud.request import GetWorksheetCellsRequest
from aspose.cells.cloud.request import GetWorksheetColumnRequest
from aspose.cells.cloud.request import GetWorksheetColumnsRequest
from aspose.cells.cloud.request import GetWorksheetRowRequest
from aspose.cells.cloud.request import GetWorksheetRowsRequest
from aspose.cells.cloud.request import PostCellCalculateRequest
from aspose.cells.cloud.request import PostCellCharactersRequest
from aspose.cells.cloud.request import PostClearContentsRequest
from aspose.cells.cloud.request import PostClearFormatsRequest
from aspose.cells.cloud.request import PostColumnStyleRequest
from aspose.cells.cloud.request import PostCopyCellIntoCellRequest
from aspose.cells.cloud.request import PostCopyWorksheetColumnsRequest
from aspose.cells.cloud.request import PostCopyWorksheetRowsRequest
from aspose.cells.cloud.request import PostGroupWorksheetColumnsRequest
from aspose.cells.cloud.request import PostGroupWorksheetRowsRequest
from aspose.cells.cloud.request import PostHideWorksheetColumnsRequest
from aspose.cells.cloud.request import PostHideWorksheetRowsRequest
from aspose.cells.cloud.request import PostRowStyleRequest
from aspose.cells.cloud.request import PostSetCellHtmlStringRequest
from aspose.cells.cloud.request import PostSetCellRangeValueRequest
from aspose.cells.cloud.request import PostSetWorksheetColumnWidthRequest
from aspose.cells.cloud.request import PostUngroupWorksheetColumnsRequest
from aspose.cells.cloud.request import PostUngroupWorksheetRowsRequest
from aspose.cells.cloud.request import PostUnhideWorksheetColumnsRequest
from aspose.cells.cloud.request import PostUnhideWorksheetRowsRequest
from aspose.cells.cloud.request import PostUpdateWorksheetCellStyleRequest
from aspose.cells.cloud.request import PostUpdateWorksheetRangeStyleRequest
from aspose.cells.cloud.request import PostUpdateWorksheetRowRequest
from aspose.cells.cloud.request import PostWorksheetCellSetValueRequest
from aspose.cells.cloud.request import PostWorksheetMergeRequest
from aspose.cells.cloud.request import PostWorksheetUnmergeRequest
from aspose.cells.cloud.request import PutInsertWorksheetColumnsRequest
from aspose.cells.cloud.request import PutInsertWorksheetRowRequest
from aspose.cells.cloud.request import PutInsertWorksheetRowsRequest

from aspose.cells.cloud.model import CalculationOptions
from aspose.cells.cloud.model import Font
from aspose.cells.cloud.model import FontSetting
from aspose.cells.cloud.model import Style


def test_post_clear_contents(client):
    """Test for PostClearContents of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostClearContentsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:C10",
        start_row=1,
        start_column=1,
        end_row=3,
        end_column=3,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_clear_formats(client):
    """Test for PostClearFormats of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostClearFormatsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:C10",
        start_row=1,
        start_column=1,
        end_row=3,
        end_column=3,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_update_worksheet_range_style(client):
    """Test for PostUpdateWorksheetRangeStyle of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostUpdateWorksheetRangeStyleRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:C10",
        style=Style(font=Font(size=16)),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_merge(client):
    """Test for PostWorksheetMerge of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetMergeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        start_row=1,
        start_column=1,
        total_rows=4,
        total_columns=4,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_unmerge(client):
    """Test for PostWorksheetUnmerge of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetUnmergeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        start_row=1,
        start_column=1,
        total_rows=4,
        total_columns=4,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_cells(client):
    """Test for GetWorksheetCells of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetCellsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        offest=1,
        count=10,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_cell(client):
    """Test for GetWorksheetCell of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetCellRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_or_method_name="A1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_worksheet_cell_style(client):
    """Test for GetWorksheetCellStyle of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetCellStyleRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_name="A1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_cell_set_value(client):
    """Test for PostWorksheetCellSetValue of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetCellSetValueRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_name="A1",
        value="1",
        type_="int",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_update_worksheet_cell_style(client):
    """Test for PostUpdateWorksheetCellStyle of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostUpdateWorksheetCellStyleRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_name="A1",
        style=Style(font=Font(size=16)),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_set_cell_range_value(client):
    """Test for PostSetCellRangeValue of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostSetCellRangeValueRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cellarea="A1:C10",
        value="Test",
        type_="string",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_copy_cell_into_cell(client):
    """Test for PostCopyCellIntoCell of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostCopyCellIntoCellRequest(
        name="Book1.xlsx",
        dest_cell_name="C1",
        sheet_name="Sheet1",
        worksheet="Sheet2",
        cellname="A1",
        row=1,
        column=1,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_cell_html_string(client):
    """Test for GetCellHtmlString of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetCellHtmlStringRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_name="A1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_post_set_cell_html_string(client):
    """Test for PostSetCellHtmlString of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostSetCellHtmlStringRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_name="A1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_cell_calculate(client):
    """Test for PostCellCalculate of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostCellCalculateRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_name="A1",
        options=CalculationOptions(recursive=True, ignore_error=True),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_cell_characters(client):
    """Test for PostCellCharacters of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostCellCharactersRequest(
        options=[FontSetting(length=5, start_index=0, font=Font(is_bold=True, size=16))],
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cell_name="E36",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_columns(client):
    """Test for GetWorksheetColumns of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetColumnsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        offset=1,
        count=10,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_set_worksheet_column_width(client):
    """Test for PostSetWorksheetColumnWidth of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostSetWorksheetColumnWidthRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        column_index=1,
        width=10.9,
        count=10,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_column(client):
    """Test for GetWorksheetColumn of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetColumnRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        column_index=1,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_insert_worksheet_columns(client):
    """Test for PutInsertWorksheetColumns of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutInsertWorksheetColumnsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        column_index=1,
        columns=10,
        update_reference=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_columns(client):
    """Test for DeleteWorksheetColumns of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetColumnsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        column_index=1,
        columns=10,
        update_reference=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_hide_worksheet_columns(client):
    """Test for PostHideWorksheetColumns of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostHideWorksheetColumnsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        start_column=1,
        total_columns=10,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_unhide_worksheet_columns(client):
    """Test for PostUnhideWorksheetColumns of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostUnhideWorksheetColumnsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        start_column=1,
        total_columns=10,
        width=10.9,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_group_worksheet_columns(client):
    """Test for PostGroupWorksheetColumns of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostGroupWorksheetColumnsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        first_index=1,
        last_index=9,
        hide=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_ungroup_worksheet_columns(client):
    """Test for PostUngroupWorksheetColumns of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostUngroupWorksheetColumnsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        first_index=1,
        last_index=9,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_copy_worksheet_columns(client):
    """Test for PostCopyWorksheetColumns of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostCopyWorksheetColumnsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        source_column_index=1,
        destination_column_index=19,
        column_number=8,
        worksheet="Sheet2",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_column_style(client):
    """Test for PostColumnStyle of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostColumnStyleRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        column_index=1,
        style=Style(font=Font(size=16)),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_rows(client):
    """Test for GetWorksheetRows of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetRowsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        offset=1,
        count=10,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_row(client):
    """Test for GetWorksheetRow of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetRowRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        row_index=1,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_row(client):
    """Test for DeleteWorksheetRow of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetRowRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        row_index=1,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_rows(client):
    """Test for DeleteWorksheetRows of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetRowsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        startrow=1,
        total_rows=10,
        update_reference=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_insert_worksheet_rows(client):
    """Test for PutInsertWorksheetRows of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutInsertWorksheetRowsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        startrow=1,
        total_rows=10,
        update_reference=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_insert_worksheet_row(client):
    """Test for PutInsertWorksheetRow of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutInsertWorksheetRowRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        row_index=1,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_update_worksheet_row(client):
    """Test for PostUpdateWorksheetRow of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostUpdateWorksheetRowRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        row_index=1,
        height=10.8,
        count=9,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_hide_worksheet_rows(client):
    """Test for PostHideWorksheetRows of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostHideWorksheetRowsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        startrow=1,
        total_rows=6,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_unhide_worksheet_rows(client):
    """Test for PostUnhideWorksheetRows of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostUnhideWorksheetRowsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        startrow=1,
        total_rows=8,
        height=10.9,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_group_worksheet_rows(client):
    """Test for PostGroupWorksheetRows of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostGroupWorksheetRowsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        first_index=1,
        last_index=9,
        hide=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_ungroup_worksheet_rows(client):
    """Test for PostUngroupWorksheetRows of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostUngroupWorksheetRowsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        first_index=1,
        last_index=9,
        is_all=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_copy_worksheet_rows(client):
    """Test for PostCopyWorksheetRows of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostCopyWorksheetRowsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        source_row_index=1,
        destination_row_index=12,
        row_number=5,
        worksheet="Sheet2",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_row_style(client):
    """Test for PostRowStyle of CellsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostRowStyleRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        row_index=1,
        style=Style(font=Font(size=16)),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
