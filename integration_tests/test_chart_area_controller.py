"""Integration tests for ChartAreaController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import GetChartAreaBorderRequest
from aspose.cells.cloud.request import GetChartAreaFillFormatRequest
from aspose.cells.cloud.request import GetChartAreaRequest


def test_get_chart_area(client):
    """Test for GetChartArea of ChartAreaController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetChartAreaRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_chart_area_fill_format(client):
    """Test for GetChartAreaFillFormat of ChartAreaController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetChartAreaFillFormatRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_chart_area_border(client):
    """Test for GetChartAreaBorder of ChartAreaController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetChartAreaBorderRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
