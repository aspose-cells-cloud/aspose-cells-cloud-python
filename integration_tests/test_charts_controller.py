"""Integration tests for ChartsController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteWorksheetChartLegendRequest
from aspose.cells.cloud.request import DeleteWorksheetChartRequest
from aspose.cells.cloud.request import DeleteWorksheetChartTitleRequest
from aspose.cells.cloud.request import DeleteWorksheetChartsRequest
from aspose.cells.cloud.request import GetWorksheetChartLegendRequest
from aspose.cells.cloud.request import GetWorksheetChartRequest
from aspose.cells.cloud.request import GetWorksheetChartTitleRequest
from aspose.cells.cloud.request import GetWorksheetChartsRequest
from aspose.cells.cloud.request import PostWorksheetChartLegendRequest
from aspose.cells.cloud.request import PostWorksheetChartRequest
from aspose.cells.cloud.request import PostWorksheetChartTitleRequest
from aspose.cells.cloud.request import PutWorksheetChartLegendRequest
from aspose.cells.cloud.request import PutWorksheetChartRequest
from aspose.cells.cloud.request import PutWorksheetChartTitleRequest

from aspose.cells.cloud.model import Chart
from aspose.cells.cloud.model import Legend
from aspose.cells.cloud.model import Title


def test_get_worksheet_charts(client):
    """Test for GetWorksheetCharts of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetChartsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_chart(client):
    """Test for GetWorksheetChart of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetChartRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_number=0,
        format_="png",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_put_worksheet_chart(client):
    """Test for PutWorksheetChart of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetChartRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_type="Pie",
        upper_left_row=5,
        upper_left_column=5,
        lower_right_row=10,
        lower_right_column=10,
        area="C7:D11",
        is_vertical=True,
        title="Aspose Chart",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_chart(client):
    """Test for DeleteWorksheetChart of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetChartRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_chart(client):
    """Test for PostWorksheetChart of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetChartRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        chart=Chart(show_legend=True, show_data_table=True),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_chart_legend(client):
    """Test for GetWorksheetChartLegend of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetChartLegendRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_chart_legend(client):
    """Test for PostWorksheetChartLegend of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetChartLegendRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        legend=Legend(position='Top'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_chart_legend(client):
    """Test for PutWorksheetChartLegend of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetChartLegendRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_chart_legend(client):
    """Test for DeleteWorksheetChartLegend of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetChartLegendRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_charts(client):
    """Test for DeleteWorksheetCharts of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetChartsRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_chart_title(client):
    """Test for GetWorksheetChartTitle of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetChartTitleRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_chart_title(client):
    """Test for PostWorksheetChartTitle of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetChartTitleRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        title=Title(is_visible=True),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_chart_title(client):
    """Test for PutWorksheetChartTitle of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetChartTitleRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        title=Title(is_visible=True),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_chart_title(client):
    """Test for DeleteWorksheetChartTitle of ChartsController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetChartTitleRequest(
        name="Book1.xlsx",
        sheet_name="Sheet4",
        chart_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
