"""Integration tests for Transform (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import RemoveSpreadsheetBlankColumnsRequest
from aspose.cells.cloud.request import RemoveSpreadsheetBlankRowsRequest
from aspose.cells.cloud.request import RemoveSpreadsheetBlankWorksheetsRequest


def test_remove_spreadsheet_blank_rows(client):
    """Test for deleting spreadsheet blank rows.."""
    request = RemoveSpreadsheetBlankRowsRequest(
        spreadsheet="testdata/EmployeeSalesSummary.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_remove_spreadsheet_blank_columns(client):
    """Test for deleting spreadsheet blank columns.."""
    request = RemoveSpreadsheetBlankColumnsRequest(
        spreadsheet="testdata/EmployeeSalesSummary.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_remove_spreadsheet_blank_worksheets(client):
    """Test for deleting spreadsheet blank worksheets.."""
    request = RemoveSpreadsheetBlankWorksheetsRequest(
        spreadsheet="testdata/EmployeeSalesSummary-BlankWorksheet.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_sawp_range(client):
    pytest.skip("API SawpRange is not defined in the specification")
