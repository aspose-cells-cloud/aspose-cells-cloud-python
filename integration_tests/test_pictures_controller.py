"""Integration tests for PicturesController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteWorksheetPictureRequest
from aspose.cells.cloud.request import DeleteWorksheetPicturesRequest
from aspose.cells.cloud.request import GetWorksheetPictureWithFormatRequest
from aspose.cells.cloud.request import GetWorksheetPicturesRequest
from aspose.cells.cloud.request import PostWorksheetPictureRequest
from aspose.cells.cloud.request import PutWorksheetAddPictureRequest

from aspose.cells.cloud.model import Picture


def test_get_worksheet_pictures(client):
    """Test for GetWorksheetPictures of PicturesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetPicturesRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_picture_with_format(client):
    """Test for GetWorksheetPictureWithFormat of PicturesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetPictureWithFormatRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        picture_number=0,
        format_="png",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_put_worksheet_add_picture(client):
    """Test for PutWorksheetAddPicture of PicturesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/WaterMark.png", "TestData/In/WaterMark.png", storage_name=None)

    request = PutWorksheetAddPictureRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        upper_left_row=1,
        upper_left_column=1,
        lower_right_row=10,
        lower_right_column=10,
        picture_path="TestData/In/WaterMark.png",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_picture(client):
    """Test for PostWorksheetPicture of PicturesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetPictureRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        picture_index=0,
        picture=Picture(left=10, bottom=10),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_picture(client):
    """Test for DeleteWorksheetPicture of PicturesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetPictureRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        picture_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_pictures(client):
    """Test for DeleteWorksheetPictures of PicturesController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetPicturesRequest(
        name="Book1.xlsx",
        sheet_name="Sheet6",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
