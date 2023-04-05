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

class TestAutoFilterControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_worksheet_auto_filter(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetAutoFilterRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_auto_filter(request)


    def test_put_worksheet_date_filter(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetDateFilterRequest( remote_name, 'Sheet1', 'A1:B1', 0, 'Year',year= 1920,match_blanks= False,refresh= True,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_date_filter(request)


    def test_put_worksheet_filter(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetFilterRequest( remote_name, 'Sheet1', 'A1:B1', 0, 'Year',match_blanks= False,refresh= True,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_filter(request)


    def test_put_worksheet_icon_filter(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetIconFilterRequest( remote_name, 'Sheet1', 'A1:B1', 0, 'ArrowsGray3', 1,match_blanks= False,refresh= True,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_icon_filter(request)


    def test_put_worksheet_custom_filter(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetCustomFilterRequest( remote_name, 'Sheet1', 'A1:B1', 0, 'LessOrEqual', '1',match_blanks= False,refresh= True,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_custom_filter(request)


    def test_put_worksheet_dynamic_filter(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetDynamicFilterRequest( remote_name, 'Sheet1', 'A1:B1', 0, 'BelowAverage',match_blanks= False,refresh= True,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_dynamic_filter(request)


    def test_put_worksheet_filter_top10(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetFilterTop10Request( remote_name, 'Sheet1', 'A1:B1', 0, True, True, 1,match_blanks= False,refresh= True,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_filter_top10(request)


    def test_put_worksheet_color_filter(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        colorFilterForegroundColorColor = Color(r= 48 ,g= 48 ,b= 48 )
        colorFilterForegroundColor = CellsColor(type= 'Automatic' ,color= colorFilterForegroundColorColor )
        colorFilter = ColorFilterRequest(pattern= 'Solid' ,foreground_color= colorFilterForegroundColor )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetColorFilterRequest( remote_name, 'Sheet1', 'A1:B1', 0, colorFilter,match_blanks= True,refresh= True,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_color_filter(request)


    def test_post_worksheet_match_blanks(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetMatchBlanksRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_match_blanks(request)


    def test_post_worksheet_match_non_blanks(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetMatchNonBlanksRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_match_non_blanks(request)


    def test_post_worksheet_auto_filter_refresh(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetAutoFilterRefreshRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.post_worksheet_auto_filter_refresh(request)


    def test_delete_worksheet_date_filter(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetDateFilterRequest( remote_name, 'Sheet1', 0, 'Year',year= 1920,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_date_filter(request)


    def test_delete_worksheet_filter(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetFilterRequest( remote_name, 'Sheet1', 0,criteria= 'year',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_filter(request)


if __name__ == '__main__':
    unittest.main()