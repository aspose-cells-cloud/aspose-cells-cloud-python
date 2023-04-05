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

class TestHypelinksControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_work_sheet_hyperlinks(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkSheetHyperlinksRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_work_sheet_hyperlinks(request)


    def test_get_work_sheet_hyperlink(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorkSheetHyperlinkRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.get_work_sheet_hyperlink(request)


    def test_delete_work_sheet_hyperlink(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorkSheetHyperlinkRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.delete_work_sheet_hyperlink(request)


    def test_post_work_sheet_hyperlink(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        hyperlink = Hyperlink(address= 'https://products.aspose.cloud/cells/' )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkSheetHyperlinkRequest( remote_name, 'Sheet1', 0, hyperlink,folder= remote_folder,storage_name= '')
        self.api.post_work_sheet_hyperlink(request)


    def test_put_work_sheet_hyperlink(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorkSheetHyperlinkRequest( remote_name, 'Sheet1', 1, 1, 2, 3, 'https://products.aspose.cloud/cells/',folder= remote_folder,storage_name= '')
        self.api.put_work_sheet_hyperlink(request)


    def test_delete_work_sheet_hyperlinks(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorkSheetHyperlinksRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.delete_work_sheet_hyperlinks(request)


if __name__ == '__main__':
    unittest.main()