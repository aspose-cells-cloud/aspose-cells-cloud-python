"""Integration tests for ShapesController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteWorksheetShapeRequest
from aspose.cells.cloud.request import DeleteWorksheetShapesRequest
from aspose.cells.cloud.request import GetWorksheetShapeRequest
from aspose.cells.cloud.request import GetWorksheetShapesRequest
from aspose.cells.cloud.request import PostWorksheetGroupShapeRequest
from aspose.cells.cloud.request import PostWorksheetShapeRequest
from aspose.cells.cloud.request import PostWorksheetUngroupShapeRequest
from aspose.cells.cloud.request import PutWorksheetShapeRequest

from aspose.cells.cloud.model import Shape


def test_get_worksheet_shapes(client):
    """Test for GetWorksheetShapes of ShapesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetShapesRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_shape(client):
    """Test for GetWorksheetShape of ShapesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetShapeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        shapeindex=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_shape(client):
    """Test for PutWorksheetShape of ShapesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetShapeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        drawing_type="arc",
        upper_left_row=1,
        upper_left_column=1,
        top=10,
        left=10,
        width=100,
        height=100,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_shapes(client):
    """Test for DeleteWorksheetShapes of ShapesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetShapesRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_shape(client):
    """Test for DeleteWorksheetShape of ShapesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetShapeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        shapeindex=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_shape(client):
    """Test for PostWorksheetShape of ShapesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetShapeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        shapeindex=0,
        dto=Shape(lower_right_column=10),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_group_shape(client):
    """Test for PostWorksheetGroupShape of ShapesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetGroupShapeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        list_shape=[0, 1],
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_ungroup_shape(client):
    """Test for PostWorksheetUngroupShape of ShapesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetUngroupShapeRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        shapeindex=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
