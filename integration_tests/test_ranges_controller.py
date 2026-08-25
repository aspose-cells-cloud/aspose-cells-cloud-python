"""Integration tests for RangesController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteWorksheetCellsRangeRequest
from aspose.cells.cloud.request import GetWorksheetCellsRangeValueRequest
from aspose.cells.cloud.request import PostWorksheetCellsRangeColumnWidthRequest
from aspose.cells.cloud.request import PostWorksheetCellsRangeMergeRequest
from aspose.cells.cloud.request import PostWorksheetCellsRangeMoveToRequest
from aspose.cells.cloud.request import PostWorksheetCellsRangeOutlineBorderRequest
from aspose.cells.cloud.request import PostWorksheetCellsRangeRowHeightRequest
from aspose.cells.cloud.request import PostWorksheetCellsRangeSortRequest
from aspose.cells.cloud.request import PostWorksheetCellsRangeStyleRequest
from aspose.cells.cloud.request import PostWorksheetCellsRangeUnMergeRequest
from aspose.cells.cloud.request import PostWorksheetCellsRangeValueRequest
from aspose.cells.cloud.request import PostWorksheetCellsRangesCopyRequest
from aspose.cells.cloud.request import PutWorksheetCellsRangeRequest

from aspose.cells.cloud.model import Color
from aspose.cells.cloud.model import DataSorter
from aspose.cells.cloud.model import Font
from aspose.cells.cloud.model import Range
from aspose.cells.cloud.model import RangeCopyRequest
from aspose.cells.cloud.model import RangeSetOutlineBorderRequest
from aspose.cells.cloud.model import RangeSetStyleRequest
from aspose.cells.cloud.model import RangeSortRequest
from aspose.cells.cloud.model import Style


def test_post_worksheet_cells_ranges_copy(client):
    """Test for PostWorksheetCellsRanges of RangesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetCellsRangesCopyRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_operate=RangeCopyRequest(operate='copydata', source=Range(column_count=3, first_column=8, first_row=3, row_count=2), target=Range(column_count=3, first_column=8, first_row=13, row_count=2)),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_cells_range_merge(client):
    """Test for PostWorksheetCellsRangeMerge of RangesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetCellsRangeMergeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_=Range(column_count=1, column_width=10.0, first_row=1, row_count=10),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_cells_range_un_merge(client):
    """Test for PostWorksheetCellsRangeUnMerge of RangesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetCellsRangeUnMergeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_=Range(column_count=1, column_width=10.0, first_row=1, row_count=10),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_cells_range_style(client):
    """Test for PostWorksheetCellsRangeStyle of RangesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetCellsRangeStyleRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_operate=RangeSetStyleRequest(style=Style(font=Font(size=16)), range_=Range(column_count=1, column_width=10.0, first_row=1, row_count=10)),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_cells_range_value(client):
    """Test for GetWorksheetCellsRangeValue of RangesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetCellsRangeValueRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        namerange="Name_2",
        first_row=0,
        first_column=0,
        row_count=3,
        column_count=2,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_cells_range_value(client):
    """Test for PostWorksheetCellsRangeValue of RangesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetCellsRangeValueRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_=Range(column_count=1, column_width=10.0, first_row=1, row_count=10),
        value="100",
        is_converted=True,
        set_style=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_cells_range_move_to(client):
    """Test for PostWorksheetCellsRangeMoveTo of RangesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetCellsRangeMoveToRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_=Range(column_count=1, column_width=10.0, first_row=1, row_count=10),
        dest_row=10,
        dest_column=10,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_cells_range_outline_border(client):
    """Test for PostWorksheetCellsRangeOutlineBorder of RangesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetCellsRangeOutlineBorderRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_operate=RangeSetOutlineBorderRequest(border_edge='LeftBorder', border_style='Dotted', border_color=Color(r=48, g=48, b=48), range_=Range(column_count=1, column_width=10.0, first_row=1, row_count=10)),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_cells_range_column_width(client):
    """Test for PostWorksheetCellsRangeColumnWidth of RangesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetCellsRangeColumnWidthRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_=Range(column_count=1, column_width=10.0, first_row=1, row_count=10),
        value=10.7,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_cells_range_row_height(client):
    """Test for PostWorksheetCellsRangeRowHeight of RangesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetCellsRangeRowHeightRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_=Range(column_count=1, column_width=10.0, first_row=1, row_count=10),
        value=10.9,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_cells_range(client):
    """Test for PutWorksheetCellsRange of RangesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetCellsRangeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:C6",
        shift="Down",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_cells_range(client):
    """Test for DeleteWorksheetCellsRange of RangesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetCellsRangeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:C6",
        shift="Up",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_cells_range_sort(client):
    """Test for PostWorksheetCellsRangeSort of RangesController.."""
    client.upload_file("testdata/Group.xlsx", "TestData/In/Group.xlsx", storage_name=None)

    request = PostWorksheetCellsRangeSortRequest(
        name="Group.xlsx",
        sheet_name="book1",
        range_sort_request=RangeSortRequest(data_sorter=DataSorter(case_sensitive=True), cell_area=Range(column_count=3, first_column=0, first_row=0, row_count=15)),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
