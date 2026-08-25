"""Integration tests for FileController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import CopyFileRequest
from aspose.cells.cloud.request import DownloadFileRequest
from aspose.cells.cloud.request import UploadFileRequest


def test_download_file(client):
    """Test for DownloadFile of FileController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DownloadFileRequest(
        path="TestData/In/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_upload_file(client):
    """Test for UploadFile of FileController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = UploadFileRequest(
        upload_files="testdata/Book1.xlsx",
        path="TestData/In/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_copy_file(client):
    """Test for CopyFile of FileController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = CopyFileRequest(
        src_path="TestData/In/Book1.xlsx",
        dest_path="OutResult/Book1.xlsx",
    )

    response = client.do(request)
