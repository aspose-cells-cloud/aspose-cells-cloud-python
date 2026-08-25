"""Integration tests for Calculate (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import AggregateCellsByColorRequest
from aspose.cells.cloud.request import MathCalculateRequest


def test_aggregate_cells_by_color(client):
    """Test for aggregate cells by color in local spreadsheet file.."""
    request = AggregateCellsByColorRequest(
        spreadsheet="testdata/AggregateCellsByColor.xlsx",
        worksheet="Sheet1",
    )

    response = client.do(request)
    assert response is not None


def test_math_calculate(client):
    """Test for match calculate spreadsheet file.."""
    request = MathCalculateRequest(
        spreadsheet="testdata/EmployeeSalesSummary-BlankWorksheet.xlsx",
        operation="add",
        value="12.3",
    )

    response = client.do(request)
    assert response is not None
