"""Integration tests for PageBreaksController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteHorizontalPageBreakRequest
from aspose.cells.cloud.request import DeleteHorizontalPageBreaksRequest
from aspose.cells.cloud.request import DeleteVerticalPageBreakRequest
from aspose.cells.cloud.request import DeleteVerticalPageBreaksRequest
from aspose.cells.cloud.request import GetHorizontalPageBreakRequest
from aspose.cells.cloud.request import GetHorizontalPageBreaksRequest
from aspose.cells.cloud.request import GetVerticalPageBreakRequest
from aspose.cells.cloud.request import GetVerticalPageBreaksRequest
from aspose.cells.cloud.request import PutHorizontalPageBreakRequest
from aspose.cells.cloud.request import PutVerticalPageBreakRequest


def test_get_vertical_page_breaks(client):
    """Test for GetVerticalPageBreaks of PageBreaksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetVerticalPageBreaksRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_horizontal_page_breaks(client):
    """Test for GetHorizontalPageBreaks of PageBreaksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetHorizontalPageBreaksRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_vertical_page_break(client):
    """Test for GetVerticalPageBreak of PageBreaksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetVerticalPageBreakRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_horizontal_page_break(client):
    """Test for GetHorizontalPageBreak of PageBreaksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetHorizontalPageBreakRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_vertical_page_break(client):
    """Test for PutVerticalPageBreak of PageBreaksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutVerticalPageBreakRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cellname="A1",
        column=1,
        row=1,
        start_row=1,
        end_row=1,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_horizontal_page_break(client):
    """Test for PutHorizontalPageBreak of PageBreaksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutHorizontalPageBreakRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        cellname="A1",
        row=1,
        column=1,
        start_column=1,
        end_column=1,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_vertical_page_breaks(client):
    """Test for DeleteVerticalPageBreaks of PageBreaksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteVerticalPageBreaksRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        column=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_horizontal_page_breaks(client):
    """Test for DeleteHorizontalPageBreaks of PageBreaksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteHorizontalPageBreaksRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        row=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_vertical_page_break(client):
    """Test for DeleteVerticalPageBreak of PageBreaksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteVerticalPageBreakRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_horizontal_page_break(client):
    """Test for DeleteHorizontalPageBreak of PageBreaksController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteHorizontalPageBreakRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
