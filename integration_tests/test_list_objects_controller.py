"""Integration tests for ListObjectsController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteWorksheetListObjectRequest
from aspose.cells.cloud.request import DeleteWorksheetListObjectsRequest
from aspose.cells.cloud.request import GetWorksheetListObjectRequest
from aspose.cells.cloud.request import GetWorksheetListObjectsRequest
from aspose.cells.cloud.request import PostWorksheetListColumnRequest
from aspose.cells.cloud.request import PostWorksheetListColumnsTotalRequest
from aspose.cells.cloud.request import PostWorksheetListObjectConvertToRangeRequest
from aspose.cells.cloud.request import PostWorksheetListObjectInsertSlicerRequest
from aspose.cells.cloud.request import PostWorksheetListObjectRemoveDuplicatesRequest
from aspose.cells.cloud.request import PostWorksheetListObjectRequest
from aspose.cells.cloud.request import PostWorksheetListObjectSortTableRequest
from aspose.cells.cloud.request import PostWorksheetListObjectSummarizeWithPivotTableRequest
from aspose.cells.cloud.request import PutWorksheetListObjectRequest

from aspose.cells.cloud.model import CreatePivotTableRequest
from aspose.cells.cloud.model import DataSorter
from aspose.cells.cloud.model import ListColumn
from aspose.cells.cloud.model import ListObject
from aspose.cells.cloud.model import TableTotalRequest


def test_get_worksheet_list_objects(client):
    """Test for GetWorksheetListObjects of ListObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetListObjectsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet7",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_list_object(client):
    """Test for GetWorksheetListObject of ListObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetListObjectRequest(
        name="Book1.xlsx",
        sheet_name="Sheet7",
        listobjectindex=0,
        format_="pdf",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_put_worksheet_list_object(client):
    """Test for PutWorksheetListObject of ListObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetListObjectRequest(
        name="Book1.xlsx",
        sheet_name="Sheet7",
        start_row=1,
        start_column=1,
        end_row=6,
        end_column=6,
        folder="TestData/In",
        has_headers=True,
        display_name="true",
        show_totals=False,
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_list_objects(client):
    """Test for DeleteWorksheetListObjects of ListObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetListObjectsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet7",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_list_object(client):
    """Test for DeleteWorksheetListObject of ListObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetListObjectRequest(
        name="Book1.xlsx",
        sheet_name="Sheet7",
        list_object_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_list_object(client):
    """Test for PostWorksheetListObject of ListObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetListObjectRequest(
        name="Book1.xlsx",
        sheet_name="Sheet7",
        list_object_index=0,
        list_object=ListObject(show_header_row=True),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_list_object_convert_to_range(client):
    """Test for PostWorksheetListObjectConvertToRange of ListObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetListObjectConvertToRangeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet7",
        list_object_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_list_object_summarize_with_pivot_table(client):
    """Test for PostWorksheetListObjectSummarizeWithPivotTable of ListObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetListObjectSummarizeWithPivotTableRequest(
        name="Book1.xlsx",
        sheet_name="Sheet7",
        list_object_index=0,
        destsheet_name="Sheet2",
        create_pivot_table_request=CreatePivotTableRequest(dest_cell_name='C1', name='testp', source_data='=Sheet2!A1:E8', use_same_source=True, pivot_field_columns=[2], pivot_field_data=[1], pivot_field_rows=[0]),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_list_object_sort_table(client):
    """Test for PostWorksheetListObjectSortTable of ListObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetListObjectSortTableRequest(
        name="Book1.xlsx",
        sheet_name="Sheet7",
        list_object_index=0,
        data_sorter=DataSorter(case_sensitive=True),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_list_column(client):
    """Test for PostWorksheetListColumn of ListObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetListColumnRequest(
        name="Book1.xlsx",
        sheet_name="Sheet7",
        list_object_index=0,
        column_index=0,
        list_column=ListColumn(name='test cloumn'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_list_columns_total(client):
    """Test for PostWorksheetListColumnsTotal of ListObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetListColumnsTotalRequest(
        name="Book1.xlsx",
        sheet_name="Sheet7",
        list_object_index=0,
        table_total_requests=[TableTotalRequest(list_column_index=1, totals_calculation='Average')],
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_list_object_remove_duplicates(client):
    """Test for PostWorksheetListObjectRemoveDuplicates of ListObjectsController.."""
    client.upload_file("testdata/TestTables.xlsx", "TestData/In/TestTables.xlsx", storage_name=None)

    request = PostWorksheetListObjectRemoveDuplicatesRequest(
        name="TestTables.xlsx",
        sheet_name="Sheet2",
        list_object_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_list_object_insert_slicer(client):
    """Test for TestPostWorksheetListObjectInsertSlicer of ListObjectsController.."""
    client.upload_file("testdata/TestTables.xlsx", "TestData/In/TestTables.xlsx", storage_name=None)

    request = PostWorksheetListObjectInsertSlicerRequest(
        name="TestTables.xlsx",
        sheet_name="Sheet1",
        list_object_index=0,
        column_index=2,
        dest_cell_name="j9",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
