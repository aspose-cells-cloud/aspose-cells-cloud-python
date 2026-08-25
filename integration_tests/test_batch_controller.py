"""Integration tests for BatchController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import PostBatchConvertRequest
from aspose.cells.cloud.request import PostBatchLockRequest
from aspose.cells.cloud.request import PostBatchProtectRequest
from aspose.cells.cloud.request import PostBatchSplitRequest
from aspose.cells.cloud.request import PostBatchUnlockRequest

from aspose.cells.cloud.model import BatchConvertRequest
from aspose.cells.cloud.model import BatchLockRequest
from aspose.cells.cloud.model import BatchProtectRequest
from aspose.cells.cloud.model import BatchSplitRequest
from aspose.cells.cloud.model import MatchConditionRequest


def test_post_batch_convert(client):
    """Test for PostBatchConvert of BatchController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/myDocument.xlsx", "TestData/In/myDocument.xlsx", storage_name=None)

    request = PostBatchConvertRequest(
        batch_convert_request=BatchConvertRequest(source_folder='TestData/In', format_='pdf', out_folder='OutResult', match_condition=MatchConditionRequest(regex_pattern='(^Book)(.+)(xlsx$)')),
    )

    response = client.do(request)
    assert response is not None


def test_post_batch_protect(client):
    """Test for PostBatchProtect of BatchController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/myDocument.xlsx", "TestData/In/myDocument.xlsx", storage_name=None)

    request = PostBatchProtectRequest(
        batch_protect_request=BatchProtectRequest(source_folder='TestData/In', protection_type='All', password='123456', out_folder='OutResult', match_condition=MatchConditionRequest(regex_pattern='(^Book)(.+)(xlsx$)')),
    )

    response = client.do(request)
    assert response is not None


def test_post_batch_lock(client):
    """Test for PostBatchLock of BatchController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/myDocument.xlsx", "TestData/In/myDocument.xlsx", storage_name=None)

    request = PostBatchLockRequest(
        batch_lock_request=BatchLockRequest(source_folder='TestData/In', password='123456', out_folder='OutResult', match_condition=MatchConditionRequest(regex_pattern='(^Book)(.+)(xlsx$)')),
    )

    response = client.do(request)
    assert response is not None


def test_post_batch_unlock(client):
    """Test for PostBatchUnlock of BatchController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/myDocument.xlsx", "TestData/In/myDocument.xlsx", storage_name=None)

    request = PostBatchUnlockRequest(
        batch_lock_request=BatchLockRequest(source_folder='TestData/In', password='123456', out_folder='OutResult', match_condition=MatchConditionRequest(regex_pattern='(^Book)(.+)(xlsx$)')),
    )

    response = client.do(request)
    assert response is not None


def test_post_batch_split(client):
    """Test for PostBatchSplit of BatchController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/myDocument.xlsx", "TestData/In/myDocument.xlsx", storage_name=None)

    request = PostBatchSplitRequest(
        batch_split_request=BatchSplitRequest(source_folder='TestData/In', format_='Pdf', out_folder='OutResult', match_condition=MatchConditionRequest(regex_pattern='(^Book)(.+)(xlsx$)')),
    )

    response = client.do(request)
    assert response is not None
