"""Integration tests for HypelinksController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteWorksheetHyperlinkRequest
from aspose.cells.cloud.request import DeleteWorksheetHyperlinksRequest
from aspose.cells.cloud.request import GetWorksheetHyperlinkRequest
from aspose.cells.cloud.request import GetWorksheetHyperlinksRequest
from aspose.cells.cloud.request import PostWorksheetHyperlinkRequest
from aspose.cells.cloud.request import PutWorksheetHyperlinkRequest

from aspose.cells.cloud.model import Hyperlink


def test_get_worksheet_hyperlinks(client):
    """Test for GetWorksheetHyperlinks of HypelinksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetHyperlinksRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_hyperlink(client):
    """Test for GetWorksheetHyperlink of HypelinksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetHyperlinkRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        hyperlink_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_hyperlink(client):
    """Test for DeleteWorksheetHyperlink of HypelinksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetHyperlinkRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        hyperlink_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_hyperlink(client):
    """Test for PostWorksheetHyperlink of HypelinksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetHyperlinkRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        hyperlink_index=0,
        hyperlink=Hyperlink(address='https://products.aspose.cloud/cells/'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_hyperlink(client):
    """Test for PutWorksheetHyperlink of HypelinksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetHyperlinkRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        first_row=1,
        first_column=1,
        total_rows=2,
        total_columns=3,
        address="https://products.aspose.cloud/cells/",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_hyperlinks(client):
    """Test for DeleteWorksheetHyperlinks of HypelinksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetHyperlinksRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
