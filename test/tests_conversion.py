# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest
import warnings

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import *
from asposecellscloud.requests import *

global_api = None

class TestConversionApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_workbook_save_as_csv__dot_net_sdk_out_result_post_excel_save_ascsv(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'csv'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.csv'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_xls__dot_net_sdk_out_result_post_excel_save_asxls(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xls'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.xls'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_html__dot_net_sdk_out_result_post_excel_save_ashtml(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'html'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.html'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_mhtml__dot_net_sdk_out_result_post_excel_save_asmhtml(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'mhtml'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.mhtml'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_ods__dot_net_sdk_out_result_post_excel_save_asods(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'ods'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.ods'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_pdf__dot_net_sdk_out_result_post_excel_save_aspdf(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'pdf'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.pdf'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_xml__dot_net_sdk_out_result_post_excel_save_asxml(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xml'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.xml'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_txt__dot_net_sdk_out_result_post_excel_save_astxt(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'txt'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.txt'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_tif__dot_net_sdk_out_result_post_excel_save_astif(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'tif'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.tif'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_xlsb__dot_net_sdk_out_result_post_excel_save_asxlsb(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xlsb'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.xlsb'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_xlsm__dot_net_sdk_out_result_post_excel_save_asxlsm(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xlsm'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.xlsm'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_xlsx__dot_net_sdk_out_result_post_excel_save_asxlsx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xlsx'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.xlsx'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_xltm__dot_net_sdk_out_result_post_excel_save_asxltm(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xltm'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.xltm'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_xltx__dot_net_sdk_out_result_post_excel_save_asxltx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xltx'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.xltx'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_xps__dot_net_sdk_out_result_post_excel_save_asxps(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xps'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.xps'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_png__dot_net_sdk_out_result_post_excel_save_aspng(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'png'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.png'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_jpg__dot_net_sdk_out_result_post_excel_save_asjpg(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'jpg'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.jpg'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_gif__dot_net_sdk_out_result_post_excel_save_asgif(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'gif'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.gif'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_emf__dot_net_sdk_out_result_post_excel_save_asemf(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'emf'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.emf'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_bmp__dot_net_sdk_out_result_post_excel_save_asbmp(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'bmp'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.bmp'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_md__dot_net_sdk_out_result_post_excel_save_asmd(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'md'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.md'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_numbers__dot_net_sdk_out_result_post_excel_save_asnumbers(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'numbers'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.numbers'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_wmf__dot_net_sdk_out_result_post_excel_save_aswmf(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'wmf'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.wmf'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_svg__dot_net_sdk_out_result_post_excel_save_assvg(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'svg'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.svg'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_docx__dot_net_sdk_out_result_post_excel_save_asdocx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'docx'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.docx'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_pptx__dot_net_sdk_out_result_post_excel_save_aspptx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'pptx'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.pptx'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_json__dot_net_sdk_out_result_post_excel_save_asjson(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'json'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.json'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_workbook_save_as_sql__dot_net_sdk_out_result_post_excel_save_assql(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'sql'
        newfilename = 'DotNetSDK/OutResult/PostExcelSaveAs.sql'

        saveOptions = PdfSaveOptions(save_format= format )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSaveAsRequest( remote_name, newfilename,save_options= saveOptions,folder= remote_folder)
        self.api.post_workbook_save_as(request)


    def test_get_workbook_format_csv(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'csv'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_xls(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xls'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_html(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'html'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_mhtml(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'mhtml'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_ods(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'ods'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_pdf(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'pdf'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_xml(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xml'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_txt(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'txt'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_tif(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'tif'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_xlsb(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xlsb'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_xlsm(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xlsm'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_xlsx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_xltm(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xltm'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_xltx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xltx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_xps(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xps'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_png(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'png'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_jpg(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'jpg'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_gif(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'gif'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_emf(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'emf'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_bmp(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'bmp'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_md(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'md'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_numbers(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'numbers'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_wmf(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'wmf'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_svg(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'svg'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_docx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'docx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_pptx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'pptx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_json(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'json'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_get_workbook_format_sql(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'sql'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookRequest( remote_name,format= format,folder= remote_folder)
        self.api.get_workbook(request)


    def test_convert_workbook_csv(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'csv'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_xls(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xls'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_html(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'html'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_mhtml(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'mhtml'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_ods(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'ods'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_pdf(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'pdf'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_xml(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xml'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_txt(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'txt'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_tif(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'tif'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_xlsb(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xlsb'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_xlsm(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xlsm'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_xlsx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xlsx'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_xltm(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xltm'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_xltx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xltx'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_xps(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xps'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_png(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'png'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_jpg(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'jpg'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_gif(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'gif'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_emf(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'emf'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_bmp(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'bmp'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_md(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'md'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_numbers(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'numbers'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_wmf(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'wmf'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_svg(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'svg'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_docx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'docx'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_pptx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'pptx'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_json(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'json'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_sql(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'sql'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_csv__dot_net_sdk_out_result_convert_workbookcsv(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'csv'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.csv'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_xls__dot_net_sdk_out_result_convert_workbookxls(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xls'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.xls'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_html__dot_net_sdk_out_result_convert_workbookhtml(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'html'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.html'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_mhtml__dot_net_sdk_out_result_convert_workbookmhtml(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'mhtml'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.mhtml'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_ods__dot_net_sdk_out_result_convert_workbookods(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'ods'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.ods'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_pdf__dot_net_sdk_out_result_convert_workbookpdf(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'pdf'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.pdf'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_xml__dot_net_sdk_out_result_convert_workbookxml(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xml'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.xml'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_txt__dot_net_sdk_out_result_convert_workbooktxt(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'txt'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.txt'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_tif__dot_net_sdk_out_result_convert_workbooktif(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'tif'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.tif'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_xlsb__dot_net_sdk_out_result_convert_workbookxlsb(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xlsb'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.xlsb'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_xlsm__dot_net_sdk_out_result_convert_workbookxlsm(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xlsm'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.xlsm'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_xlsx__dot_net_sdk_out_result_convert_workbookxlsx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xlsx'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.xlsx'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_xltm__dot_net_sdk_out_result_convert_workbookxltm(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xltm'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.xltm'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_xltx__dot_net_sdk_out_result_convert_workbookxltx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xltx'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.xltx'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_xps__dot_net_sdk_out_result_convert_workbookxps(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'xps'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.xps'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_png__dot_net_sdk_out_result_convert_workbookpng(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'png'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.png'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_jpg__dot_net_sdk_out_result_convert_workbookjpg(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'jpg'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.jpg'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_gif__dot_net_sdk_out_result_convert_workbookgif(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'gif'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.gif'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_emf__dot_net_sdk_out_result_convert_workbookemf(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'emf'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.emf'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_bmp__dot_net_sdk_out_result_convert_workbookbmp(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'bmp'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.bmp'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_md__dot_net_sdk_out_result_convert_workbookmd(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'md'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.md'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_numbers__dot_net_sdk_out_result_convert_workbooknumbers(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'numbers'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.numbers'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_wmf__dot_net_sdk_out_result_convert_workbookwmf(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'wmf'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.wmf'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_svg__dot_net_sdk_out_result_convert_workbooksvg(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'svg'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.svg'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_docx__dot_net_sdk_out_result_convert_workbookdocx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'docx'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.docx'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_pptx__dot_net_sdk_out_result_convert_workbookpptx(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'pptx'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.pptx'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_json__dot_net_sdk_out_result_convert_workbookjson(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'json'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.json'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_save_cloud_sql__dot_net_sdk_out_result_convert_workbooksql(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        format = 'sql'
        out_path = 'DotNetSDK/OutResult/ConvertWorkbook.sql'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format,out_path= out_path)
        self.api.put_convert_workbook(request)


if __name__ == '__main__':
    unittest.main()