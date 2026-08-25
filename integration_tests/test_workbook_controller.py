"""Integration tests for WorkbookController (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import DeleteDecryptWorkbookRequest
from aspose.cells.cloud.request import DeleteDocumentUnProtectFromChangesRequest
from aspose.cells.cloud.request import DeleteUnProtectWorkbookRequest
from aspose.cells.cloud.request import DeleteWorkbookBackgroundRequest
from aspose.cells.cloud.request import DeleteWorkbookNameRequest
from aspose.cells.cloud.request import DeleteWorkbookNamesRequest
from aspose.cells.cloud.request import GetPageCountRequest
from aspose.cells.cloud.request import GetWorkbookDefaultStyleRequest
from aspose.cells.cloud.request import GetWorkbookNameRequest
from aspose.cells.cloud.request import GetWorkbookNameValueRequest
from aspose.cells.cloud.request import GetWorkbookNamesRequest
from aspose.cells.cloud.request import GetWorkbookSettingsRequest
from aspose.cells.cloud.request import GetWorkbookTextItemsRequest
from aspose.cells.cloud.request import PostAutofitWorkbookColumnsRequest
from aspose.cells.cloud.request import PostAutofitWorkbookRowsRequest
from aspose.cells.cloud.request import PostDigitalSignatureRequest
from aspose.cells.cloud.request import PostEncryptWorkbookRequest
from aspose.cells.cloud.request import PostImportDataRequest
from aspose.cells.cloud.request import PostProtectWorkbookRequest
from aspose.cells.cloud.request import PostWorkbookCalculateFormulaRequest
from aspose.cells.cloud.request import PostWorkbookGetSmartMarkerResultRequest
from aspose.cells.cloud.request import PostWorkbookNameRequest
from aspose.cells.cloud.request import PostWorkbookSettingsRequest
from aspose.cells.cloud.request import PostWorkbookSplitRequest
from aspose.cells.cloud.request import PostWorkbookTextReplaceRequest
from aspose.cells.cloud.request import PostWorkbooksMergeRequest
from aspose.cells.cloud.request import PostWorkbooksTextSearchRequest
from aspose.cells.cloud.request import PutDocumentProtectFromChangesRequest
from aspose.cells.cloud.request import PutWorkbookBackgroundRequest
from aspose.cells.cloud.request import PutWorkbookCreateRequest
from aspose.cells.cloud.request import PutWorkbookNameRequest
from aspose.cells.cloud.request import PutWorkbookWaterMarkerRequest

from aspose.cells.cloud.model import CalculationOptions
from aspose.cells.cloud.model import ImportIntArrayOption
from aspose.cells.cloud.model import Name
from aspose.cells.cloud.model import PasswordRequest
from aspose.cells.cloud.model import ProtectWorkbookRequest
from aspose.cells.cloud.model import TextWaterMarkerRequest
from aspose.cells.cloud.model import WorkbookEncryptionRequest
from aspose.cells.cloud.model import WorkbookSettings


def test_post_digital_signature(client):
    """Test for PostDigitalSignature of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/roywang.pfx", "TestData/In/roywang.pfx", storage_name=None)

    request = PostDigitalSignatureRequest(
        name="Book1.xlsx",
        digitalsignaturefile="TestData/In/roywang.pfx",
        password="123456",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_encrypt_workbook(client):
    """Test for PostEncryptWorkbook of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostEncryptWorkbookRequest(
        name="Book1.xlsx",
        encryption=WorkbookEncryptionRequest(password='123456', encryption_type='XOR', key_length=128),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_decrypt_workbook(client):
    """Test for DeleteDecryptWorkbook of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteDecryptWorkbookRequest(
        name="Book1.xlsx",
        encryption=WorkbookEncryptionRequest(password='123456', encryption_type='XOR', key_length=128),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_protect_workbook(client):
    """Test for PostProtectWorkbook of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostProtectWorkbookRequest(
        name="Book1.xlsx",
        protect_workbook_request=ProtectWorkbookRequest(encrypt_with_password='123456', protect_workbook_structure='ALL'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_un_protect_workbook(client):
    """Test for DeleteUnProtectWorkbook of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteUnProtectWorkbookRequest(
        name="Book1.xlsx",
        password="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_workbook_default_style(client):
    """Test for GetWorkbookDefaultStyle of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookDefaultStyleRequest(
        name="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_workbook_text_items(client):
    """Test for GetWorkbookTextItems of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookTextItemsRequest(
        name="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_workbook_names(client):
    """Test for GetWorkbookNames of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookNamesRequest(
        name="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_workbook_name(client):
    """Test for PutWorkbookName of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorkbookNameRequest(
        name="Book1.xlsx",
        new_name=Name(text='name_1804', comment='KeepSourceFormatting', refers_to='=Sheet1!$I$4'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_workbook_name(client):
    """Test for GetWorkbookName of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookNameRequest(
        name="Book1.xlsx",
        name_name="Name_2",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_workbook_name(client):
    """Test for PostWorkbookName of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookNameRequest(
        name="Book1.xlsx",
        name_name="Name_2",
        new_name=Name(text='name_1804', comment='KeepSourceFormatting', refers_to='=Sheet1!$I$4'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_workbook_name_value(client):
    """Test for GetWorkbookNameValue of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookNameValueRequest(
        name="Book1.xlsx",
        name_name="Name_2",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_workbook_names(client):
    """Test for DeleteWorkbookNames of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorkbookNamesRequest(
        name="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_workbook_name(client):
    """Test for DeleteWorkbookName of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorkbookNameRequest(
        name="Book1.xlsx",
        name_name="Name_2",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_document_protect_from_changes(client):
    """Test for PutDocumentProtectFromChanges of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutDocumentProtectFromChangesRequest(
        name="Book1.xlsx",
        password=PasswordRequest(password='123456'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_document_un_protect_from_changes(client):
    """Test for DeleteDocumentUnProtectFromChanges of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteDocumentUnProtectFromChangesRequest(
        name="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_workbooks_merge(client):
    """Test for PostWorkbooksMerge of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/myDocument.xlsx", "TestData/In/myDocument.xlsx", storage_name=None)

    request = PostWorkbooksMergeRequest(
        name="Book1.xlsx",
        merge_with="TestData/In/myDocument.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_workbooks_text_search(client):
    """Test for PostWorkbooksTextSearch of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbooksTextSearchRequest(
        name="Book1.xlsx",
        text="1234",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_workbook_text_replace(client):
    """Test for PostWorkbooksTextReplace of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookTextReplaceRequest(
        name="Book1.xlsx",
        old_value="1234",
        new_value="5678",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_workbook_get_smart_marker_result(client):
    """Test for PostWorkbookGetSmartMarkerResult of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/ReportData.xml", "TestData/In/ReportData.xml", storage_name=None)

    request = PostWorkbookGetSmartMarkerResultRequest(
        name="Book1.xlsx",
        xml_file="TestData/In/ReportData.xml",
        folder="TestData/In",
        out_path="OutResult/SmartMarkerResult.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_put_workbook_create(client):
    """Test for PutWorkbookCreate of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/ReportData.xml", "TestData/In/ReportData.xml", storage_name=None)

    request = PutWorkbookCreateRequest(
        name="PutWorkbookCreate.xlsx",
        template_file="TestData/In/Book1.xlsx",
        data_file="TestData/In/ReportData.xml",
        is_write_over=True,
        folder="TestData/In",
        check_excel_restriction=True,
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_workbook_split(client):
    """Test for PostWorkbookSplit of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSplitRequest(
        name="Book1.xlsx",
        format_="png",
        out_folder="OutResult",
        from_=1,
        to=5,
        horizontal_resolution=96,
        vertical_resolution=96,
        split_name_rule="sheetname",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_import_data(client):
    """Test for PostImportData of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostImportDataRequest(
        import_option=ImportIntArrayOption(destination_worksheet='Sheet1', first_column=1, first_row=3, import_data_type='IntArray', is_insert=True, is_vertical=True, data=[1, 2, 3, 4]),
        name="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_workbook_calculate_formula(client):
    """Test for PostWorkbookCalculateFormula of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookCalculateFormulaRequest(
        name="Book1.xlsx",
        options=CalculationOptions(ignore_error=True, recursive=True),
        ignore_error=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_autofit_workbook_rows(client):
    """Test for PostAutofitWorkbookRows of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostAutofitWorkbookRowsRequest(
        name="Book1.xlsx",
        start_row=1,
        end_row=100,
        only_auto=True,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_autofit_workbook_columns(client):
    """Test for PostAutofitWorkbookColumns of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostAutofitWorkbookColumnsRequest(
        name="Book1.xlsx",
        start_column=1,
        end_column=20,
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_workbook_settings(client):
    """Test for GetWorkbookSettings of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookSettingsRequest(
        name="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_post_workbook_settings(client):
    """Test for PostWorkbookSettings of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSettingsRequest(
        name="Book1.xlsx",
        settings=WorkbookSettings(auto_compress_pictures=True, hide_pivot_field_list=True),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_workbook_background(client):
    """Test for PutWorkbookBackground of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    client.upload_file("testdata/WaterMark.png", "TestData/In/WaterMark.png", storage_name=None)

    request = PutWorkbookBackgroundRequest(
        name="Book1.xlsx",
        pic_path="TestData/In/WaterMark.png",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_delete_workbook_background(client):
    """Test for DeleteWorkbookBackground of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = DeleteWorkbookBackgroundRequest(
        name="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_put_workbook_water_marker(client):
    """Test for PutWorkbookWaterMarker of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PutWorkbookWaterMarkerRequest(
        name="Book1.xlsx",
        text_water_marker_request=TextWaterMarkerRequest(text='Aspose Cells Cloud', font_size=12),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_page_count(client):
    """Test for GetPageCount of WorkbookController.."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetPageCountRequest(
        name="Book1.xlsx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None
