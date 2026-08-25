"""Integration tests for LightCells (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteMetadataRequest
from aspose.cells.cloud.request import GetMetadataRequest
from aspose.cells.cloud.request import PostAssembleRequest
from aspose.cells.cloud.request import PostClearObjectsRequest
from aspose.cells.cloud.request import PostCompressRequest
from aspose.cells.cloud.request import PostExportRequest
from aspose.cells.cloud.request import PostLockRequest
from aspose.cells.cloud.request import PostMergeRequest
from aspose.cells.cloud.request import PostMetadataRequest
from aspose.cells.cloud.request import PostProtectRequest
from aspose.cells.cloud.request import PostRepairRequest
from aspose.cells.cloud.request import PostReplaceRequest
from aspose.cells.cloud.request import PostReverseRequest
from aspose.cells.cloud.request import PostSearchRequest
from aspose.cells.cloud.request import PostSplitRequest
from aspose.cells.cloud.request import PostUnlockRequest
from aspose.cells.cloud.request import PostWatermarkRequest

from aspose.cells.cloud.model import CellsDocumentProperty
from aspose.cells.cloud.model import ProtectWorkbookRequest


def test_post_split_0(client):
    """Test for save workbook as one of the available formats. (parameter set 1 of 2)."""
    request = PostSplitRequest(
        out_format="pdf",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response.body


def test_post_split_1(client):
    """Test for save workbook as one of the available formats. (parameter set 2 of 2)."""
    request = PostSplitRequest(
        out_format="xps",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response.body


def test_post_assemble(client):
    """Test for save workbook as one of the available formats.."""
    request = PostAssembleRequest(
        out_format="html",
        datasource="ds",
        file="testdata/assemblytest.xlsx",
    )

    response = client.do(request)
    assert response.body


def test_post_export_0(client):
    """Test for save workbook as one of the available formats. (parameter set 1 of 2)."""
    request = PostExportRequest(
        format_="pdf",
        object_type="listobject",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response.body


def test_post_export_1(client):
    """Test for save workbook as one of the available formats. (parameter set 2 of 2)."""
    request = PostExportRequest(
        format_="md",
        object_type="listobject",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response.body


def test_post_compress_0(client):
    """Test for save workbook as one of the available formats. (parameter set 1 of 2)."""
    request = PostCompressRequest(
        compress_level=50,
        file="testdata/datasource.xlsx",
    )

    response = client.do(request)
    assert response.body


def test_post_compress_1(client):
    """Test for save workbook as one of the available formats. (parameter set 2 of 2)."""
    request = PostCompressRequest(
        compress_level=90,
        file="testdata/datasource.xlsx",
    )

    response = client.do(request)
    assert response.body


def test_post_merge_0(client):
    """Test for save workbook as one of the available formats. (parameter set 1 of 4)."""
    request = PostMergeRequest(
        out_format="html",
        merge_to_one_sheet=True,
        file="testdata/assemblytest.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_merge_1(client):
    """Test for save workbook as one of the available formats. (parameter set 2 of 4)."""
    request = PostMergeRequest(
        out_format="pdf",
        merge_to_one_sheet=True,
        file="testdata/assemblytest.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_merge_2(client):
    """Test for save workbook as one of the available formats. (parameter set 3 of 4)."""
    request = PostMergeRequest(
        out_format="xlsx",
        merge_to_one_sheet=True,
        file="testdata/assemblytest.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_merge_3(client):
    """Test for save workbook as one of the available formats. (parameter set 4 of 4)."""
    request = PostMergeRequest(
        out_format="json",
        merge_to_one_sheet=False,
        file="testdata/assemblytest.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_unlock(client):
    """Test for save workbook as one of the available formats.."""
    request = PostUnlockRequest(
        password="123456",
        file="testdata/needUnlock.xlsx",
    )

    response = client.do(request)
    assert response.body


def test_post_lock(client):
    """Test for lock an Excel file.."""
    request = PostLockRequest(
        password="123456",
        file="testdata/needlock.xlsx",
    )

    response = client.do(request)
    assert response.body


def test_post_protect(client):
    """Test for save workbook as one of the available formats.."""
    request = PostProtectRequest(
        protect_workbook_request=ProtectWorkbookRequest(aways_open_read_only=True, encrypt_with_password='123456'),
        password="123456",
        file="testdata/assemblytest.xlsx",
    )

    response = client.do(request)
    assert response.body


def test_post_protect__protect_workbook_request(client):
    """Test for save workbook as one of the available formats.."""
    request = PostProtectRequest(
        protect_workbook_request=ProtectWorkbookRequest(aways_open_read_only=True, encrypt_with_password='123456'),
        file="testdata/datasource.xlsx",
    )

    response = client.do(request)
    assert response.body


def test_post_search(client):
    """Test for save workbook as one of the available formats.."""
    request = PostSearchRequest(
        text="12",
        file="testdata/datasource.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_replace(client):
    """Test for save workbook as one of the available formats.."""
    request = PostReplaceRequest(
        text="12",
        newtext="newtext",
        file="testdata/datasource.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_replace_only_sheetname(client):
    """Test for save workbook as one of the available formats.."""
    request = PostReplaceRequest(
        text="12",
        newtext="newtext",
        sheetname="Sheet1",
        file="testdata/datasource.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_watermark(client):
    """Test for save workbook as one of the available formats.."""
    request = PostWatermarkRequest(
        text="aspose.cells cloud sdk",
        color="#773322",
        file="testdata/datasource.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_clear_objects_0(client):
    """Test for save workbook as one of the available formats. (parameter set 1 of 10)."""
    request = PostClearObjectsRequest(
        objecttype="chart",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_clear_objects_1(client):
    """Test for save workbook as one of the available formats. (parameter set 2 of 10)."""
    request = PostClearObjectsRequest(
        objecttype="comment",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_clear_objects_2(client):
    """Test for save workbook as one of the available formats. (parameter set 3 of 10)."""
    request = PostClearObjectsRequest(
        objecttype="picture",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_clear_objects_3(client):
    """Test for save workbook as one of the available formats. (parameter set 4 of 10)."""
    request = PostClearObjectsRequest(
        objecttype="shape",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_clear_objects_4(client):
    """Test for save workbook as one of the available formats. (parameter set 5 of 10)."""
    request = PostClearObjectsRequest(
        objecttype="listobject",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_clear_objects_5(client):
    """Test for save workbook as one of the available formats. (parameter set 6 of 10)."""
    request = PostClearObjectsRequest(
        objecttype="hyperlink",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_clear_objects_6(client):
    """Test for save workbook as one of the available formats. (parameter set 7 of 10)."""
    request = PostClearObjectsRequest(
        objecttype="oleobject",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_clear_objects_7(client):
    """Test for save workbook as one of the available formats. (parameter set 8 of 10)."""
    request = PostClearObjectsRequest(
        objecttype="pivottable",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_clear_objects_8(client):
    """Test for save workbook as one of the available formats. (parameter set 9 of 10)."""
    request = PostClearObjectsRequest(
        objecttype="validation",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_clear_objects_9(client):
    """Test for save workbook as one of the available formats. (parameter set 10 of 10)."""
    request = PostClearObjectsRequest(
        objecttype="Background",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_repair_0(client):
    """Test for repair workbook as one of the available formats. (parameter set 1 of 2)."""
    request = PostRepairRequest(
        out_format="xlsx",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_repair_1(client):
    """Test for repair workbook as one of the available formats. (parameter set 2 of 2)."""
    request = PostRepairRequest(
        out_format="pdf",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_reverse_0(client):
    """Test for save workbook as one of the available formats. (parameter set 1 of 2)."""
    request = PostReverseRequest(
        rotate_type="rows",
        out_format="pdf",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_reverse_1(client):
    """Test for save workbook as one of the available formats. (parameter set 2 of 2)."""
    request = PostReverseRequest(
        rotate_type="cols",
        out_format="pdf",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_get_metadata(client):
    """Test for save workbook as one of the available formats.."""
    request = GetMetadataRequest(
        type_="all",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_delete_metadata(client):
    """Test for save workbook as one of the available formats.."""
    request = DeleteMetadataRequest(
        type_="all",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_post_metadata(client):
    """Test for save workbook as one of the available formats.."""
    request = PostMetadataRequest(
        cells_documents=[CellsDocumentProperty(name='Author', value='roy.wang')],
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None
