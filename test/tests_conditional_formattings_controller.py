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

class TestConditionalFormattingsControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_worksheet_conditional_formattings(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetConditionalFormattingsRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_conditional_formattings(request)


    def test_get_worksheet_conditional_formatting(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetConditionalFormattingRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_conditional_formatting(request)


    def test_put_worksheet_conditional_formatting(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        formatcondition = FormatCondition(type= 'CellValue' ,operator= 'Between' ,formula1= 'v1' ,formula2= 'v2' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetConditionalFormattingRequest( remote_name, 'Sheet1', formatcondition, 'A1:C10',folder= remote_folder,storage_name= '')
        self.api.put_worksheet_conditional_formatting(request)


    def test_put_worksheet_format_condition(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetFormatConditionRequest( remote_name, 'Sheet1', 0, 'A1:C10', 'CellValue', 'Between', 'v1', 'v2',folder= remote_folder,storage_name= '')
        self.api.put_worksheet_format_condition(request)


    def test_put_worksheet_format_condition_area(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetFormatConditionAreaRequest( remote_name, 'Sheet1', 0, 'A1:C10',folder= remote_folder,storage_name= '')
        self.api.put_worksheet_format_condition_area(request)


    def test_put_worksheet_format_condition_condition(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetFormatConditionConditionRequest( remote_name, 'Sheet1', 0, 'CellValue', 'Between', 'v1', 'v2',folder= remote_folder,storage_name= '')
        self.api.put_worksheet_format_condition_condition(request)


    def test_delete_worksheet_conditional_formattings(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetConditionalFormattingsRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_conditional_formattings(request)


    def test_delete_worksheet_conditional_formatting(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetConditionalFormattingRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_conditional_formatting(request)


    def test_delete_worksheet_conditional_formatting_area(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetConditionalFormattingAreaRequest( remote_name, 'Sheet1', 1, 1, 4, 6,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_conditional_formatting_area(request)


if __name__ == '__main__':
    unittest.main()