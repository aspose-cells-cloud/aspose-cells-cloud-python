"""Integration tests for SparklineGroupsController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteWorksheetSparklineGroupRequest
from aspose.cells.cloud.request import DeleteWorksheetSparklineGroupsRequest
from aspose.cells.cloud.request import GetWorksheetSparklineGroupRequest
from aspose.cells.cloud.request import GetWorksheetSparklineGroupsRequest
from aspose.cells.cloud.request import PostWorksheetSparklineGroupRequest
from aspose.cells.cloud.request import PutWorksheetSparklineGroupRequest

from aspose.cells.cloud.model import SparklineGroup


def test_get_worksheet_sparkline_groups(client):
    """Test for GetWorksheetSparklineGroups of SparklineGroupsController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = GetWorksheetSparklineGroupsRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_worksheet_sparkline_group(client):
    """Test for GetWorksheetSparklineGroup of SparklineGroupsController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = GetWorksheetSparklineGroupRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet1",
        sparkline_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_sparkline_groups(client):
    """Test for DeleteWorksheetSparklineGroups of SparklineGroupsController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = DeleteWorksheetSparklineGroupsRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet1",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_worksheet_sparkline_group(client):
    """Test for DeleteWorksheetSparklineGroup of SparklineGroupsController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = DeleteWorksheetSparklineGroupRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet1",
        sparkline_index=0,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_worksheet_sparkline_group(client):
    """Test for PutWorksheetSparklineGroup of SparklineGroupsController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = PutWorksheetSparklineGroupRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet1",
        type_="Line",
        data_range="C6:E13",
        is_vertical=False,
        location_range="G6:G13",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_worksheet_sparkline_group(client):
    """Test for PostWorksheetSparklineGroup of SparklineGroupsController.."""
    client.upload_file("testdata/TestCase.xlsx", "TestData/In/TestCase.xlsx", storage_name=None)

    request = PostWorksheetSparklineGroupRequest(
        name="TestCase.xlsx",
        sheet_name="Sheet1",
        sparkline_group_index=0,
        sparkline_group=SparklineGroup(display_hidden=True, plot_right_to_left=True),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200
