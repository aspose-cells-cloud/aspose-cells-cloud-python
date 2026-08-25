"""Integration tests for StorageController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import GetDiscUsageRequest
from aspose.cells.cloud.request import GetFileVersionsRequest
from aspose.cells.cloud.request import ObjectExistsRequest
from aspose.cells.cloud.request import StorageExistsRequest


def test_storage_exists(client):
    """Test for StorageExists of StorageController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = StorageExistsRequest(
        storage_name="Default",
    )

    response = client.do(request)
    assert response is not None


def test_object_exists(client):
    """Test for ObjectExists of StorageController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = ObjectExistsRequest(
        path="TestData/In/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_get_disc_usage(client):
    """Test for GetDiscUsage of StorageController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetDiscUsageRequest(
    )

    response = client.do(request)
    assert response is not None


def test_get_file_versions(client):
    """Test for GetFileVersions of StorageController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetFileVersionsRequest(
        path="TestData/In/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None
