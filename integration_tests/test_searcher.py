"""Integration tests for Searcher (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import SearchAllTextItemsInRemoteSpreadsheetRequest
from aspose.cells.cloud.request import SearchBrokenLinksInRemoteRangeRequest
from aspose.cells.cloud.request import SearchBrokenLinksInRemoteSpreadsheetRequest
from aspose.cells.cloud.request import SearchBrokenLinksInRemoteWorksheetRequest
from aspose.cells.cloud.request import SearchContentInRemoteRangeRequest
from aspose.cells.cloud.request import SearchContentInRemoteSpreadsheetRequest
from aspose.cells.cloud.request import SearchSpreadsheetAllTextItemsRequest
from aspose.cells.cloud.request import SearchSpreadsheetBrokenLinksRequest
from aspose.cells.cloud.request import SearchSpreadsheetContentRequest


def test_search_text_in_local_file(client):
    """Test for search content in local file.."""
    request = SearchSpreadsheetContentRequest(
        spreadsheet="testdata/BookText.xlsx",
        search_text="Bike",
        ignoring_case=False,
    )

    response = client.do(request)
    assert response is not None


def test_search_text_from_worksheet_in_local_file(client):
    """Test for search content in local file.."""
    request = SearchSpreadsheetContentRequest(
        spreadsheet="testdata/BookText.xlsx",
        search_text="Bike",
        ignoring_case=False,
        worksheet="Sales",
    )

    response = client.do(request)
    assert response is not None


def test_search_text_in_remote_spreadsheet(client):
    """Test for search content in local file.."""
    client.upload_file("testdata/BookText.xlsx", "TestData/In/BookText.xlsx", storage_name=None)

    request = SearchContentInRemoteSpreadsheetRequest(
        name="BookText.xlsx",
        search_text="Bike",
        ignoring_case=False,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_search_text_in_remote_range(client):
    """Test for search content in local file.."""
    client.upload_file("testdata/BookText.xlsx", "TestData/In/BookText.xlsx", storage_name=None)

    request = SearchContentInRemoteRangeRequest(
        name="BookText.xlsx",
        search_text="Bike",
        ignoring_case=False,
        worksheet="Sales",
        cell_area="A1:A10",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_search_spreadsheet_broken_links(client):
    """Test for search content in local file.."""
    request = SearchSpreadsheetBrokenLinksRequest(
        spreadsheet="testdata/BookFormula.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_search_broken_links_in_remote_spreadsheet(client):
    """Test for replace content in local file.."""
    client.upload_file("testdata/BookFormula.xlsx", "TestData/In/BookFormula.xlsx", storage_name=None)

    request = SearchBrokenLinksInRemoteSpreadsheetRequest(
        name="BookFormula.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_search_broken_links_in_remote_worksheet(client):
    """Test for replace content in local file.."""
    client.upload_file("testdata/BookFormula.xlsx", "TestData/In/BookFormula.xlsx", storage_name=None)

    request = SearchBrokenLinksInRemoteWorksheetRequest(
        name="BookFormula.xlsx",
        worksheet="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_search_broken_links_in_remote_range(client):
    """Test for replace content in local file.."""
    client.upload_file("testdata/BookFormula.xlsx", "TestData/In/BookFormula.xlsx", storage_name=None)

    request = SearchBrokenLinksInRemoteRangeRequest(
        name="BookFormula.xlsx",
        worksheet="Sheet1",
        cell_area="A1:F40",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_search_all_text_items_in_remote_spreadsheet(client):
    """Test for replace content in local file.."""
    client.upload_file("testdata/BookFormula.xlsx", "TestData/In/BookFormula.xlsx", storage_name=None)

    request = SearchAllTextItemsInRemoteSpreadsheetRequest(
        name="BookFormula.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_search_spreadsheet_all_text_items(client):
    """Test for getting worksheets with spreadsheet.."""
    request = SearchSpreadsheetAllTextItemsRequest(
        spreadsheet="testdata/EmployeeSalesSummary.xlsx",
    )

    response = client.do(request)
    assert response is not None
