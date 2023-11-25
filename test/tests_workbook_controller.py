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

class TestWorkbookControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_post_digital_signature(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        roywang_pfx = 'roywang.pfx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, roywang_pfx, remote_folder + '/roywang.pfx' ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostDigitalSignatureRequest( remote_name, remote_folder + '/roywang.pfx', '123456',folder= remote_folder,storage_name= '')
        self.api.post_digital_signature(request)


    def test_post_encrypt_workbook(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        encryption = WorkbookEncryptionRequest(password= '123456' ,encryption_type= 'XOR' ,key_length= 128 )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostEncryptWorkbookRequest( remote_name, encryption,folder= remote_folder,storage_name= '')
        self.api.post_encrypt_workbook(request)


    def test_delete_decrypt_workbook(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        encryption = WorkbookEncryptionRequest(password= '123456' ,encryption_type= 'XOR' ,key_length= 128 )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteDecryptWorkbookRequest( remote_name, encryption,folder= remote_folder,storage_name= '')
        self.api.delete_decrypt_workbook(request)


    def test_post_protect_workbook(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        protectWorkbookRequest = ProtectWorkbookRequest(encrypt_with_password= '123456' ,protect_workbook_structure= 'ALL' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostProtectWorkbookRequest( remote_name, protectWorkbookRequest,folder= remote_folder,storage_name= '')
        self.api.post_protect_workbook(request)


    def test_delete_un_protect_workbook(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteUnProtectWorkbookRequest( remote_name, remote_name,folder= remote_folder,storage_name= '')
        self.api.delete_un_protect_workbook(request)


    def test_get_workbook_default_style(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookDefaultStyleRequest( remote_name,folder= remote_folder,storage_name= '')
        self.api.get_workbook_default_style(request)


    def test_get_workbook_text_items(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookTextItemsRequest( remote_name,folder= remote_folder,storage_name= '')
        self.api.get_workbook_text_items(request)


    def test_get_workbook_names(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookNamesRequest( remote_name,folder= remote_folder,storage_name= '')
        self.api.get_workbook_names(request)


    def test_put_workbook_name(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        newName = Name(text= 'name_1804' ,comment= 'KeepSourceFormatting' ,refers_to= '=Sheet1!$I$4' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorkbookNameRequest( remote_name, newName,folder= remote_folder,storage_name= '')
        self.api.put_workbook_name(request)


    def test_get_workbook_name(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookNameRequest( remote_name, 'Name_2',folder= remote_folder,storage_name= '')
        self.api.get_workbook_name(request)


    def test_post_workbook_name(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        newName = Name(text= 'name_1804' ,comment= 'KeepSourceFormatting' ,refers_to= '=Sheet1!$I$4' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookNameRequest( remote_name, 'Name_2', newName,folder= remote_folder,storage_name= '')
        self.api.post_workbook_name(request)


    def test_get_workbook_name_value(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookNameValueRequest( remote_name, 'Name_2',folder= remote_folder,storage_name= '')
        self.api.get_workbook_name_value(request)


    def test_delete_workbook_names(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorkbookNamesRequest( remote_name,folder= remote_folder,storage_name= '')
        self.api.delete_workbook_names(request)


    def test_delete_workbook_name(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorkbookNameRequest( remote_name, 'Name_2',folder= remote_folder,storage_name= '')
        self.api.delete_workbook_name(request)


    def test_put_document_protect_from_changes(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        password = PasswordRequest(password= '123456' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutDocumentProtectFromChangesRequest( remote_name, password,folder= remote_folder,storage_name= '')
        self.api.put_document_protect_from_changes(request)


    def test_delete_document_un_protect_from_changes(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteDocumentUnProtectFromChangesRequest( remote_name,folder= remote_folder,storage_name= '')
        self.api.delete_document_un_protect_from_changes(request)


    def test_post_workbooks_merge(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        my_document_xlsx = 'myDocument.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, my_document_xlsx, remote_folder + '/myDocument.xlsx' ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbooksMergeRequest( remote_name, remote_folder + '/myDocument.xlsx',folder= remote_folder,storage_name= '',merged_storage_name= '')
        self.api.post_workbooks_merge(request)


    def test_post_workbooks_text_search(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbooksTextSearchRequest( remote_name, '1234',folder= remote_folder,storage_name= '')
        self.api.post_workbooks_text_search(request)


    def test_post_workbook_text_replace(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookTextReplaceRequest( remote_name, '1234', '5678',folder= remote_folder,storage_name= '')
        self.api.post_workbook_text_replace(request)


    def test_post_workbook_get_smart_marker_result(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        report_data_xml = 'ReportData.xml'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, report_data_xml, remote_folder + '/ReportData.xml' ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookGetSmartMarkerResultRequest( remote_name,xml_file= remote_folder + '/ReportData.xml',folder= remote_folder,out_path= 'OutResult/SmartMarkerResult.xlsx',storage_name= '',out_storage_name= '')
        self.api.post_workbook_get_smart_marker_result(request)


    def test_put_workbook_create(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        report_data_xml = 'ReportData.xml'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, report_data_xml, remote_folder + '/ReportData.xml' ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorkbookCreateRequest( 'PutWorkbookCreate.xlsx',template_file= remote_folder + '/' + remote_name,data_file= remote_folder + '/ReportData.xml',is_write_over= True,folder= remote_folder,storage_name= '',check_excel_restriction= True)
        self.api.put_workbook_create(request)


    def test_post_workbook_split(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSplitRequest( remote_name,format= 'png',out_folder= 'OutResult',_from= 1,to= 5,split_name_rule= 'sheetname',folder= remote_folder,storage_name= '',out_storage_name= '')
        self.api.post_workbook_split(request)


    def test_post_import_data(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        importOptionData = [
            1,
            2,
            3,
            4
        ]
        importOption = ImportIntArrayOption(destination_worksheet= 'Sheet1' ,first_column= 1 ,first_row= 3 ,import_data_type= 'IntArray' ,is_insert= True ,is_vertical= True ,data= importOptionData )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostImportDataRequest( remote_name,import_option= importOption,folder= remote_folder,storage_name= '')
        self.api.post_import_data(request)


    def test_post_workbook_calculate_formula(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        options = CalculationOptions(ignore_error= True ,recursive= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookCalculateFormulaRequest( remote_name,options= options,ignore_error= True,folder= remote_folder,storage_name= '')
        self.api.post_workbook_calculate_formula(request)


    def test_post_autofit_workbook_rows(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostAutofitWorkbookRowsRequest( remote_name,start_row= 1,end_row= 100,only_auto= True,folder= remote_folder,storage_name= '')
        self.api.post_autofit_workbook_rows(request)


    def test_post_autofit_workbook_columns(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostAutofitWorkbookColumnsRequest( remote_name,start_column= 1,end_column= 20,folder= remote_folder,storage_name= '')
        self.api.post_autofit_workbook_columns(request)


    def test_get_workbook_settings(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkbookSettingsRequest( remote_name,folder= remote_folder,storage_name= '')
        self.api.get_workbook_settings(request)


    def test_post_workbook_settings(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        settings = WorkbookSettings(auto_compress_pictures= True ,hide_pivot_field_list= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookSettingsRequest( remote_name, settings,folder= remote_folder,storage_name= '')
        self.api.post_workbook_settings(request)


    def test_put_workbook_background(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        water_mark_png = 'WaterMark.png'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, water_mark_png, remote_folder + '/WaterMark.png' ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorkbookBackgroundRequest( remote_name,pic_path= remote_folder + '/WaterMark.png',folder= remote_folder,storage_name= '')
        self.api.put_workbook_background(request)


    def test_delete_workbook_background(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorkbookBackgroundRequest( remote_name,folder= remote_folder,storage_name= '')
        self.api.delete_workbook_background(request)


    def test_put_workbook_water_marker(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        textWaterMarkerRequest = TextWaterMarkerRequest(text= 'Aspose Cells Cloud' ,font_size= 12 )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorkbookWaterMarkerRequest( remote_name, textWaterMarkerRequest,folder= remote_folder,storage_name= '')
        self.api.put_workbook_water_marker(request)


    def test_get_page_count(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetPageCountRequest( remote_name,folder= remote_folder,storage_name= '')
        self.api.get_page_count(request)


if __name__ == '__main__':
    unittest.main()