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

class TestPageBreaksControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_vertical_page_breaks(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetVerticalPageBreaksRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_vertical_page_breaks(request)


    def test_get_horizontal_page_breaks(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetHorizontalPageBreaksRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_horizontal_page_breaks(request)


    def test_get_vertical_page_break(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetVerticalPageBreakRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.get_vertical_page_break(request)


    def test_get_horizontal_page_break(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetHorizontalPageBreakRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.get_horizontal_page_break(request)


    def test_put_vertical_page_break(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutVerticalPageBreakRequest( remote_name, 'Sheet1',cellname= 'A1',column= 1,row= 1,start_row= 1,end_row= 1,folder= remote_folder,storage_name= '')
        self.api.put_vertical_page_break(request)


    def test_put_horizontal_page_break(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutHorizontalPageBreakRequest( remote_name, 'Sheet1',cellname= 'A1',row= 1,column= 1,start_column= 1,end_column= 1,folder= remote_folder,storage_name= '')
        self.api.put_horizontal_page_break(request)


    def test_delete_vertical_page_breaks(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteVerticalPageBreaksRequest( remote_name, 'Sheet1',column= 0,folder= remote_folder,storage_name= '')
        self.api.delete_vertical_page_breaks(request)


    def test_delete_horizontal_page_breaks(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteHorizontalPageBreaksRequest( remote_name, 'Sheet1',row= 0,folder= remote_folder,storage_name= '')
        self.api.delete_horizontal_page_breaks(request)


    def test_delete_vertical_page_break(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteVerticalPageBreakRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.delete_vertical_page_break(request)


    def test_delete_horizontal_page_break(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteHorizontalPageBreakRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.delete_horizontal_page_break(request)


if __name__ == '__main__':
    unittest.main()