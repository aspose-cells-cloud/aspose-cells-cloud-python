"""Integration tests for PivotTablesController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeletePivotTableFieldRequest
from aspose.cells.cloud.request import DeleteWorksheetPivotTableFilterRequest
from aspose.cells.cloud.request import DeleteWorksheetPivotTableFiltersRequest
from aspose.cells.cloud.request import DeleteWorksheetPivotTableRequest
from aspose.cells.cloud.request import DeleteWorksheetPivotTablesRequest
from aspose.cells.cloud.request import GetPivotTableFieldRequest
from aspose.cells.cloud.request import GetWorksheetPivotTableFiltersRequest
from aspose.cells.cloud.request import GetWorksheetPivotTableRequest
from aspose.cells.cloud.request import GetWorksheetPivotTablesRequest
from aspose.cells.cloud.request import PostPivotTableCellStyleRequest
from aspose.cells.cloud.request import PostPivotTableFieldHideItemRequest
from aspose.cells.cloud.request import PostPivotTableFieldMoveToRequest
from aspose.cells.cloud.request import PostPivotTableStyleRequest
from aspose.cells.cloud.request import PostPivotTableUpdatePivotFieldRequest
from aspose.cells.cloud.request import PostPivotTableUpdatePivotFieldsRequest
from aspose.cells.cloud.request import PostWorksheetPivotTableCalculateRequest
from aspose.cells.cloud.request import PostWorksheetPivotTableMoveRequest
from aspose.cells.cloud.request import PutPivotTableFieldRequest
from aspose.cells.cloud.request import PutWorksheetPivotTableRequest

from aspose.cells.cloud.model import Font
from aspose.cells.cloud.model import PivotField
from aspose.cells.cloud.model import PivotTableFieldRequest
from aspose.cells.cloud.model import Style


def test_get_worksheet_pivot_tables(client):
    """Test for GetWorksheetPivotTables of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = GetWorksheetPivotTablesRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_pivot_table(client):
    """Test for GetWorksheetPivotTable of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = GetWorksheetPivotTableRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivottable_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_pivot_table_field(client):
    """Test for GetPivotTableField of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = GetPivotTableFieldRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        pivot_field_index=0,
        pivot_field_type="Row",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_pivot_table_filters(client):
    """Test for GetWorksheetPivotTableFilters of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = GetWorksheetPivotTableFiltersRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_pivot_table(client):
    """Test for PutWorksheetPivotTable of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = PutWorksheetPivotTableRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        folder="TestData/In",
        source_data="=Sheet1!C6:E13",
        dest_cell_name="C1",
        table_name="TestPivot",
        use_same_source=True,
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_pivot_table_field(client):
    """Test for PutPivotTableField of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = PutPivotTableFieldRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        pivot_field_type="Row",
        pivot_table_field_request=PivotTableFieldRequest(data=[0]),
        need_re_calculate=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_pivot_table_field_hide_item(client):
    """Test for PostPivotTableFieldHideItem of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = PostPivotTableFieldHideItemRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        pivot_field_type="Row",
        field_index=0,
        item_index=1,
        is_hide=True,
        need_re_calculate=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_pivot_table_field_move_to(client):
    """Test for PostPivotTableFieldMoveTo of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = PostPivotTableFieldMoveToRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        field_index=0,
        from_="Row",
        to="Column",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_pivot_table_cell_style(client):
    """Test for PostPivotTableCellStyle of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = PostPivotTableCellStyleRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        column=1,
        row=1,
        style=Style(font=Font(size=16)),
        need_re_calculate=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_pivot_table_style(client):
    """Test for PostPivotTableStyle of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = PostPivotTableStyleRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        style=Style(font=Font(size=16)),
        need_re_calculate=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_pivot_table_update_pivot_fields(client):
    """Test for PostPivotTableUpdatePivotFields of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = PostPivotTableUpdatePivotFieldsRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        pivot_field_type="Row",
        pivot_field=PivotField(show_compact=True),
        need_re_calculate=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_pivot_table_update_pivot_field(client):
    """Test for PostPivotTableUpdatePivotField of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = PostPivotTableUpdatePivotFieldRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        pivot_field_index=0,
        pivot_field_type="Row",
        pivot_field=PivotField(show_compact=True),
        need_re_calculate=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_pivot_table_calculate(client):
    """Test for PostWorksheetPivotTableCalculate of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = PostWorksheetPivotTableCalculateRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_pivot_table_move(client):
    """Test for PostWorksheetPivotTableMove of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = PostWorksheetPivotTableMoveRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        row=1,
        column=1,
        dest_cell_name="C10",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_pivot_tables(client):
    """Test for DeleteWorksheetPivotTables of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = DeleteWorksheetPivotTablesRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_pivot_table(client):
    """Test for DeleteWorksheetPivotTable of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = DeleteWorksheetPivotTableRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_pivot_table_field(client):
    """Test for DeletePivotTableField of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = DeletePivotTableFieldRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet4",
        pivot_table_index=0,
        pivot_field_type="Row",
        pivot_table_field_request=PivotTableFieldRequest(data=[0]),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_pivot_table_filters(client):
    """Test for DeleteWorksheetPivotTableFilters of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = DeleteWorksheetPivotTableFiltersRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet3",
        pivot_table_index=0,
        need_re_calculate=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_pivot_table_filter(client):
    """Test for DeleteWorksheetPivotTableFilter of PivotTablesController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = DeleteWorksheetPivotTableFilterRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet3",
        pivot_table_index=0,
        field_index=0,
        need_re_calculate=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
