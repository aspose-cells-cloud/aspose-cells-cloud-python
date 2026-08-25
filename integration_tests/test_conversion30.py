"""Integration tests for Conversion30 (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import GetWorkbookRequest
from aspose.cells.cloud.request import PostWorkbookSaveAsRequest
from aspose.cells.cloud.request import PutConvertWorkbookRequest

from aspose.cells.cloud.model import SaveOptions


def test_workbook_save_as_0(client):
    """Test for save workbook as one of the available formats. (parameter set 1 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.csv",
        save_options=SaveOptions(save_format='csv'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_1(client):
    """Test for save workbook as one of the available formats. (parameter set 2 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.html",
        save_options=SaveOptions(save_format='html'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_2(client):
    """Test for save workbook as one of the available formats. (parameter set 3 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.mhtml",
        save_options=SaveOptions(save_format='mhtml'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_3(client):
    """Test for save workbook as one of the available formats. (parameter set 4 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.ods",
        save_options=SaveOptions(save_format='ods'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_4(client):
    """Test for save workbook as one of the available formats. (parameter set 5 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.pdf",
        save_options=SaveOptions(save_format='pdf'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_5(client):
    """Test for save workbook as one of the available formats. (parameter set 6 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.xml",
        save_options=SaveOptions(save_format='xml'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_6(client):
    """Test for save workbook as one of the available formats. (parameter set 7 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.txt",
        save_options=SaveOptions(save_format='txt'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_7(client):
    """Test for save workbook as one of the available formats. (parameter set 8 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.tif",
        save_options=SaveOptions(save_format='tif'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_8(client):
    """Test for save workbook as one of the available formats. (parameter set 9 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.xlsb",
        save_options=SaveOptions(save_format='xlsb'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_9(client):
    """Test for save workbook as one of the available formats. (parameter set 10 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.xps",
        save_options=SaveOptions(save_format='xps'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_10(client):
    """Test for save workbook as one of the available formats. (parameter set 11 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.png",
        save_options=SaveOptions(save_format='png'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_11(client):
    """Test for save workbook as one of the available formats. (parameter set 12 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.md",
        save_options=SaveOptions(save_format='md'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_12(client):
    """Test for save workbook as one of the available formats. (parameter set 13 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.svg",
        save_options=SaveOptions(save_format='svg'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_13(client):
    """Test for save workbook as one of the available formats. (parameter set 14 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.docx",
        save_options=SaveOptions(save_format='docx'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_14(client):
    """Test for save workbook as one of the available formats. (parameter set 15 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.pptx",
        save_options=SaveOptions(save_format='pptx'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_15(client):
    """Test for save workbook as one of the available formats. (parameter set 16 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.json",
        save_options=SaveOptions(save_format='json'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_workbook_save_as_16(client):
    """Test for save workbook as one of the available formats. (parameter set 17 of 17)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = PostWorkbookSaveAsRequest(
        name="Book1.xlsx",
        newfilename="OutResult/PostExcelSaveAs.sql",
        save_options=SaveOptions(save_format='sql'),
        folder="TestData/In",
    )

    response = client.do(request)
    assert response.status_code == 200


def test_get_workbook_format_0(client):
    """Test for get workbook as one of the available formats. (parameter set 1 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="csv",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_1(client):
    """Test for get workbook as one of the available formats. (parameter set 2 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="html",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_2(client):
    """Test for get workbook as one of the available formats. (parameter set 3 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="mhtml",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_3(client):
    """Test for get workbook as one of the available formats. (parameter set 4 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="ods",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_4(client):
    """Test for get workbook as one of the available formats. (parameter set 5 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="pdf",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_5(client):
    """Test for get workbook as one of the available formats. (parameter set 6 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="xml",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_6(client):
    """Test for get workbook as one of the available formats. (parameter set 7 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="txt",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_7(client):
    """Test for get workbook as one of the available formats. (parameter set 8 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="tif",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_8(client):
    """Test for get workbook as one of the available formats. (parameter set 9 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="xps",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_9(client):
    """Test for get workbook as one of the available formats. (parameter set 10 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="png",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_10(client):
    """Test for get workbook as one of the available formats. (parameter set 11 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="md",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_11(client):
    """Test for get workbook as one of the available formats. (parameter set 12 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="svg",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_12(client):
    """Test for get workbook as one of the available formats. (parameter set 13 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="docx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_13(client):
    """Test for get workbook as one of the available formats. (parameter set 14 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="pptx",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_14(client):
    """Test for get workbook as one of the available formats. (parameter set 15 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="json",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_get_workbook_format_15(client):
    """Test for get workbook as one of the available formats. (parameter set 16 of 16)."""
    client.upload_file("testdata/Book1.xlsx", "TestData/In/Book1.xlsx", storage_name=None)

    request = GetWorkbookRequest(
        name="Book1.xlsx",
        format_="sql",
        folder="TestData/In",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_0(client):
    """Test for get workbook as one of the available formats. (parameter set 1 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="csv",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_1(client):
    """Test for get workbook as one of the available formats. (parameter set 2 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="xls",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_2(client):
    """Test for get workbook as one of the available formats. (parameter set 3 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="html",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_3(client):
    """Test for get workbook as one of the available formats. (parameter set 4 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="mhtml",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_4(client):
    """Test for get workbook as one of the available formats. (parameter set 5 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="ods",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_5(client):
    """Test for get workbook as one of the available formats. (parameter set 6 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="pdf",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_6(client):
    """Test for get workbook as one of the available formats. (parameter set 7 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="xml",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_7(client):
    """Test for get workbook as one of the available formats. (parameter set 8 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="txt",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_8(client):
    """Test for get workbook as one of the available formats. (parameter set 9 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="tif",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_9(client):
    """Test for get workbook as one of the available formats. (parameter set 10 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="xlsb",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_10(client):
    """Test for get workbook as one of the available formats. (parameter set 11 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="xps",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_11(client):
    """Test for get workbook as one of the available formats. (parameter set 12 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="png",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_12(client):
    """Test for get workbook as one of the available formats. (parameter set 13 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="md",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_13(client):
    """Test for get workbook as one of the available formats. (parameter set 14 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="svg",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_14(client):
    """Test for get workbook as one of the available formats. (parameter set 15 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="docx",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_15(client):
    """Test for get workbook as one of the available formats. (parameter set 16 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="pptx",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_16(client):
    """Test for get workbook as one of the available formats. (parameter set 17 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="json",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_17(client):
    """Test for get workbook as one of the available formats. (parameter set 18 of 18)."""
    request = PutConvertWorkbookRequest(
        format_="sql",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_0(client):
    """Test for converting workbook to one of the available formats. (parameter set 1 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="csv",
        out_path="OutResult/ConvertWorkbook.csv",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_1(client):
    """Test for converting workbook to one of the available formats. (parameter set 2 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="xls",
        out_path="OutResult/ConvertWorkbook.xls",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_2(client):
    """Test for converting workbook to one of the available formats. (parameter set 3 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="html",
        out_path="OutResult/ConvertWorkbook.html",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_3(client):
    """Test for converting workbook to one of the available formats. (parameter set 4 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="mhtml",
        out_path="OutResult/ConvertWorkbook.mhtml",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_4(client):
    """Test for converting workbook to one of the available formats. (parameter set 5 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="ods",
        out_path="OutResult/ConvertWorkbook.ods",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_5(client):
    """Test for converting workbook to one of the available formats. (parameter set 6 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="pdf",
        out_path="OutResult/ConvertWorkbook.pdf",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_6(client):
    """Test for converting workbook to one of the available formats. (parameter set 7 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="xml",
        out_path="OutResult/ConvertWorkbook.xml",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_7(client):
    """Test for converting workbook to one of the available formats. (parameter set 8 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="txt",
        out_path="OutResult/ConvertWorkbook.txt",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_8(client):
    """Test for converting workbook to one of the available formats. (parameter set 9 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="tif",
        out_path="OutResult/ConvertWorkbook.tif",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_9(client):
    """Test for converting workbook to one of the available formats. (parameter set 10 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="xlsb",
        out_path="OutResult/ConvertWorkbook.xlsb",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_10(client):
    """Test for converting workbook to one of the available formats. (parameter set 11 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="xltm",
        out_path="OutResult/ConvertWorkbook.xltm",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_11(client):
    """Test for converting workbook to one of the available formats. (parameter set 12 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="xps",
        out_path="OutResult/ConvertWorkbook.xps",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_12(client):
    """Test for converting workbook to one of the available formats. (parameter set 13 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="png",
        out_path="OutResult/ConvertWorkbook.png",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_13(client):
    """Test for converting workbook to one of the available formats. (parameter set 14 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="md",
        out_path="OutResult/ConvertWorkbook.md",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_14(client):
    """Test for converting workbook to one of the available formats. (parameter set 15 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="svg",
        out_path="OutResult/ConvertWorkbook.svg",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_15(client):
    """Test for converting workbook to one of the available formats. (parameter set 16 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="docx",
        out_path="OutResult/ConvertWorkbook.docx",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_16(client):
    """Test for converting workbook to one of the available formats. (parameter set 17 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="pptx",
        out_path="OutResult/ConvertWorkbook.pptx",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_17(client):
    """Test for converting workbook to one of the available formats. (parameter set 18 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="json",
        out_path="OutResult/ConvertWorkbook.json",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_convert_workbook_save_cloud_18(client):
    """Test for converting workbook to one of the available formats. (parameter set 19 of 19)."""
    request = PutConvertWorkbookRequest(
        format_="sql",
        out_path="OutResult/ConvertWorkbook.sql",
        file="testdata/Book1.xlsx",
    )

    response = client.do(request)
    assert response is not None
