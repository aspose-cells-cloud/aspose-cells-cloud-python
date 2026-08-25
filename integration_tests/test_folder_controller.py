"""Integration tests for FolderController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import CopyFolderRequest
from aspose.cells.cloud.request import CreateFolderRequest
from aspose.cells.cloud.request import DeleteFolderRequest
from aspose.cells.cloud.request import GetFilesListRequest
from aspose.cells.cloud.request import MoveFolderRequest


def test_get_files_list(client):
    """Test for GetFilesList of FolderController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetFilesListRequest(
        path="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_create_folder(client):
    """Test for CreateFolder of FolderController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = CreateFolderRequest(
        path="OutResult/NewFolder",
    )

    response = client.do(request)


def test_copy_folder(client):
    """Test for CopyFolder of FolderController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = CopyFolderRequest(
        src_path="TestData/In",
        dest_path="OutResult/Create",
    )

    response = client.do(request)


def test_move_folder(client):
    """Test for MoveFolder of FolderController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = MoveFolderRequest(
        src_path="OutResult/Create",
        dest_path="OutResult/Move",
    )

    response = client.do(request)


def test_delete_folder(client):
    """Test for DeleteFolder of FolderController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteFolderRequest(
        path="OutResult/Create",
        recursive=True,
    )

    response = client.do(request)
