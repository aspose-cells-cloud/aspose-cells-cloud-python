"""Integration tests for Splitter (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import SplitRemoteSpreadsheetRequest
from aspose.cells.cloud.request import SplitSpreadsheetRequest


def test_split_local_file(client):
    """Test for merge local file into a excel file.."""
    request = SplitSpreadsheetRequest(
        spreadsheet="testdata/Book1.xlsx",
        out_format="PDF",
    )

    response = client.do(request)
    assert response is not None


def test_split_local_file_to_remote_folder(client):
    """Test for merge local file into a excel file.."""
    request = SplitSpreadsheetRequest(
        spreadsheet="testdata/Book1.xlsx",
        out_format="PDF",
        out_path="TestData/Out",
    )

    response = client.do(request)
    assert response is not None


def test_split_file_in_remote(client):
    """Test for merge local file into a excel file.."""
    request = SplitRemoteSpreadsheetRequest(
        name="Book1.xlsx",
        out_format="PDF",
        folder="TestData/In",
        out_path="TestData/Out",
    )

    response = client.do(request)
    assert response is not None
