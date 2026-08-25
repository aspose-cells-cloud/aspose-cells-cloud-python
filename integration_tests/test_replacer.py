"""Integration tests for Replacer (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import ReplaceContentInRemoteRangeRequest
from aspose.cells.cloud.request import ReplaceSpreadsheetContentRequest


def test_replace_text_in_local_file(client):
    """Test for replace content in local file.."""
    request = ReplaceSpreadsheetContentRequest(
        spreadsheet="testdata/BookText.xlsx",
        search_text="Bike",
        replace_text="****",
    )

    response = client.do(request)
    assert response is not None


def test_replace_text_from_worksheet_in_local_file(client):
    """Test for replace content in local file.."""
    request = ReplaceSpreadsheetContentRequest(
        spreadsheet="testdata/BookText.xlsx",
        search_text="Bike",
        replace_text="****",
        worksheet="Sales",
    )

    response = client.do(request)
    assert response is not None


def test_replace_text_in_remote(client):
    pytest.skip("API ReplaceRemoteSpreadsheetContent is not defined in the specification")


def test_replace_text_in_remote_spreadsheet(client):
    pytest.skip("API ReplaceRemoteSpreadsheetContent is not defined in the specification")


def test_replace_text_in_remote_range(client):
    """Test for replace content in local file.."""
    client.upload_file("testdata/BookText.xlsx", "TestData/In/BookText.xlsx", storage_name=None)

    request = ReplaceContentInRemoteRangeRequest(
        name="BookText.xlsx",
        search_text="Bike",
        replace_text="****",
        worksheet="Sales",
        cell_area="A1:A10",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None
