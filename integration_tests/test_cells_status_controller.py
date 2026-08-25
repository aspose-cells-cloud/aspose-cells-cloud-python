"""Integration tests for CellsStatusController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import GetCellsCloudServiceStatusRequest


def test_get_cells_cloud_service_status(client):
    """Test for GetCellsCloudServiceStatus of CellsStatusController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetCellsCloudServiceStatusRequest(
    )

    response = client.do(request)
    assert response.get_json() == "OK"
