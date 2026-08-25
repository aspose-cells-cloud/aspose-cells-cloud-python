"""Integration tests for AutoFilterController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteWorksheetDateFilterRequest
from aspose.cells.cloud.request import DeleteWorksheetFilterRequest
from aspose.cells.cloud.request import GetWorksheetAutoFilterRequest
from aspose.cells.cloud.request import PostWorksheetAutoFilterRefreshRequest
from aspose.cells.cloud.request import PostWorksheetMatchBlanksRequest
from aspose.cells.cloud.request import PostWorksheetMatchNonBlanksRequest
from aspose.cells.cloud.request import PutWorksheetColorFilterRequest
from aspose.cells.cloud.request import PutWorksheetCustomFilterRequest
from aspose.cells.cloud.request import PutWorksheetDateFilterRequest
from aspose.cells.cloud.request import PutWorksheetDynamicFilterRequest
from aspose.cells.cloud.request import PutWorksheetFilterRequest
from aspose.cells.cloud.request import PutWorksheetFilterTop10Request
from aspose.cells.cloud.request import PutWorksheetIconFilterRequest

from aspose.cells.cloud.model import CellsColor
from aspose.cells.cloud.model import Color
from aspose.cells.cloud.model import ColorFilterRequest


def test_get_worksheet_auto_filter(client):
    """Test for GetWorksheetAutoFilter of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorksheetAutoFilterRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_date_filter(client):
    """Test for PutWorksheetDateFilter of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetDateFilterRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:B1",
        field_index=0,
        date_time_grouping_type="Year",
        year=1920,
        match_blanks=False,
        refresh=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_filter(client):
    """Test for PutWorksheetFilter of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetFilterRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:B1",
        field_index=0,
        criteria="Year",
        match_blanks=False,
        refresh=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_icon_filter(client):
    """Test for PutWorksheetIconFilter of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetIconFilterRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:B1",
        field_index=0,
        icon_set_type="ArrowsGray3",
        icon_id=1,
        match_blanks=False,
        refresh=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_custom_filter(client):
    """Test for PutWorksheetCustomFilter of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetCustomFilterRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:B1",
        field_index=0,
        operator_type1="LessOrEqual",
        criteria1="1",
        match_blanks=False,
        refresh=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_dynamic_filter(client):
    """Test for PutWorksheetDynamicFilter of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetDynamicFilterRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:B1",
        field_index=0,
        dynamic_filter_type="BelowAverage",
        match_blanks=False,
        refresh=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_filter_top10(client):
    """Test for PutWorksheetFilterTop10 of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetFilterTop10Request(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:B1",
        field_index=0,
        is_top=True,
        is_percent=True,
        item_count=1,
        match_blanks=False,
        refresh=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_color_filter(client):
    """Test for PutWorksheetColorFilter of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorksheetColorFilterRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        range_="A1:B1",
        field_index=0,
        color_filter=ColorFilterRequest(pattern='Solid', foreground_color=CellsColor(type_='Automatic', color=Color(r=48, g=48, b=48))),
        match_blanks=True,
        refresh=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_match_blanks(client):
    """Test for PostWorksheetMatchBlanks of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetMatchBlanksRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        field_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_match_non_blanks(client):
    """Test for PostWorksheetMatchNonBlanks of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetMatchNonBlanksRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        field_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_auto_filter_refresh(client):
    """Test for PostWorksheetAutoFilterRefresh of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorksheetAutoFilterRefreshRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_date_filter(client):
    """Test for DeleteWorksheetDateFilter of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetDateFilterRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        field_index=0,
        date_time_grouping_type="Year",
        year=1920,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_filter(client):
    """Test for DeleteWorksheetFilter of AutoFilterController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorksheetFilterRequest(
        name="Book1.xlsx",
        sheet_name="Sheet1",
        field_index=0,
        criteria="year",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
