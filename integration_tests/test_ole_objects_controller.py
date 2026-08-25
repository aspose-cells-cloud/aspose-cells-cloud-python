"""Integration tests for OleObjectsController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteWorksheetOleObjectRequest
from aspose.cells.cloud.request import DeleteWorksheetOleObjectsRequest
from aspose.cells.cloud.request import GetWorksheetOleObjectRequest
from aspose.cells.cloud.request import GetWorksheetOleObjectsRequest
from aspose.cells.cloud.request import PostUpdateWorksheetOleObjectRequest
from aspose.cells.cloud.request import PutWorksheetOleObjectRequest

from aspose.cells.cloud.model import OleObject


def test_get_worksheet_ole_objects(client):
    """Test for GetWorksheetOleObjects of OleObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetOleObjectsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_ole_object(client):
    """Test for GetWorksheetOleObject of OleObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetOleObjectRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        object_number=0,
        format_="png",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_delete_worksheet_ole_objects(client):
    """Test for DeleteWorksheetOleObjects of OleObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetOleObjectsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_ole_object(client):
    """Test for DeleteWorksheetOleObject of OleObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetOleObjectRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        ole_object_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_update_worksheet_ole_object(client):
    """Test for PostUpdateWorksheetOleObject of OleObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostUpdateWorksheetOleObjectRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        ole_object_index=0,
        ole=OleObject(left=10, right=10, height=90, width=78),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_ole_object(client):
    """Test for PutWorksheetOleObject of OleObjectsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/OLEDoc.docx", "OLEDoc.docx", storage_name=None)

    client.upload_file("testdata/word.jpg", "word.jpg", storage_name=None)

    request = PutWorksheetOleObjectRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        upper_left_row=1,
        upper_left_column=1,
        height=100,
        width=80,
        ole_file="OLEDoc.docx",
        image_file="word.jpg",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
