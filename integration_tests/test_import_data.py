"""Integration tests for ImportData (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import ImportDataIntoSpreadsheetRequest


def test_import_data_into_spreadsheet(client):
    """Test for importing data in a spreadsheet file.."""
    request = ImportDataIntoSpreadsheetRequest(
        spreadsheet="testdata/Book1.xlsx",
        datafile="testdata/BookCsvDuplicateData.csv",
        worksheet="Sheet1",
        startcell="E3",
    )

    response = client.do(request)
    assert response is not None
