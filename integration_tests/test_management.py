"""Integration tests for Management (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import AddWorksheetToSpreadsheetRequest
from aspose.cells.cloud.request import CompressSpreadsheetRequest
from aspose.cells.cloud.request import CreateSpreadsheetRequest
from aspose.cells.cloud.request import DeleteWorksheetFromSpreadsheetRequest
from aspose.cells.cloud.request import GetMergedCellsInRemotedWorksheetRequest
from aspose.cells.cloud.request import GetMergedCellsInWorksheetRequest
from aspose.cells.cloud.request import MoveWorksheetInSpreadsheetRequest
from aspose.cells.cloud.request import RenameWorksheetInSpreadsheetRequest
from aspose.cells.cloud.request import RepairSpreadsheetRequest


def test_create_spreadsheet(client):
    """Test for creating spreadsheet.."""
    request = CreateSpreadsheetRequest(
        format_="xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_create_spreadsheet_with_template(client):
    """Test for creating spreadsheet.."""
    request = CreateSpreadsheetRequest(
        format_="pdf",
        template="SalesDataComparisonXLSX",
    )

    response = client.do(request)
    assert response is not None


def test_add_worksheet(client):
    """Test for adding worksheet on spreadsheet.."""
    request = AddWorksheetToSpreadsheetRequest(
        spreadsheet="testdata/AggregateCellsByColor.xlsx",
        sheet_type="Worksheet",
        position=1,
    )

    response = client.do(request)
    assert response is not None


def test_delete_worksheet(client):
    """Test for deleting worksheet on spreadsheet.."""
    request = DeleteWorksheetFromSpreadsheetRequest(
        spreadsheet="testdata/EmployeeSalesSummary.xlsx",
        sheet_name="Sales",
    )

    response = client.do(request)
    assert response is not None


def test_rename_worksheet(client):
    """Test for rename worksheet on spreadsheet.."""
    request = RenameWorksheetInSpreadsheetRequest(
        spreadsheet="testdata/EmployeeSalesSummary.xlsx",
        source_name="Sales",
        target_name="SalesData",
    )

    response = client.do(request)
    assert response is not None


def test_move_worksheet(client):
    """Test for move worksheet on spreadsheet.."""
    request = MoveWorksheetInSpreadsheetRequest(
        spreadsheet="testdata/EmployeeSalesSummary.xlsx",
        worksheet="Sales",
        position=1,
    )

    response = client.do(request)
    assert response is not None


def test_compress_spreadsheet(client):
    """Test for compress spreadsheet.."""
    request = CompressSpreadsheetRequest(
        spreadsheet="testdata/EmployeeSalesSummary.xlsx",
        level=9,
    )

    response = client.do(request)
    assert response is not None


def test_repair_spreadsheet(client):
    """Test for compress spreadsheet.."""
    request = RepairSpreadsheetRequest(
        spreadsheet="testdata/EmployeeSalesSummary.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_get_worksheets_with_spreadsheet(client):
    pytest.skip("API GetWorksheetsWithSpreadsheet is not defined in the specification")


def test_get_merged_cells_in_remoted_worksheet(client):
    """Test for replace content in local file.."""
    client.upload_file("testdata/EmployeeSalesSummary.xlsx", "TestData/In/EmployeeSalesSummary.xlsx", storage_name=None)

    request = GetMergedCellsInRemotedWorksheetRequest(
        name="EmployeeSalesSummary.xlsx",
        worksheet="Sales",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_merged_cells_in_worksheet(client):
    """Test for replace content in local file.."""
    request = GetMergedCellsInWorksheetRequest(
        spreadsheet="testdata/EmployeeSalesSummary.xlsx",
        worksheet="Sales",
    )

    response = client.do(request)
    assert response is not None
