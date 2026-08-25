"""Integration tests for Protection (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import ProtectSpreadsheetRequest
from aspose.cells.cloud.request import UnprotectSpreadsheetRequest


def test_protect_spreadsheet(client):
    """Test for protect local spreadsheet file.."""
    request = ProtectSpreadsheetRequest(
        password="123456",
        modify_password="123456",
        spreadsheet="testdata/EmployeeSalesSummary.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_unprotect_spreadsheet(client):
    """Test for unprotect the local spreadsheet file.."""
    request = UnprotectSpreadsheetRequest(
        password="123456",
        modify_password="123456",
        spreadsheet="testdata/EmployeeSalesSummary_Locked.xlsx",
    )

    response = client.do(request)
    assert response is not None
