"""Integration tests for Merger (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import MergeRemoteSpreadsheetRequest


def test_merge_files_in_remote_folder(client):
    pytest.skip("API MergeRemoteSpreadsheets is not defined in the specification")


def test_merge_remote_spreadsheet(client):
    """Test for merge local file into a excel file.."""
    client.upload_file("testdata/BookText.xlsx", "TestData/In/BookText.xlsx", storage_name=None)

    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = MergeRemoteSpreadsheetRequest(
        name="BookText.xlsx",
        merged_spreadsheet="TestData/In/Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None
