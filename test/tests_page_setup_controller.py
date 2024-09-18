# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest
import warnings
import time

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import *
from asposecellscloud.requests import *

global_api = None

class TestPageSetupControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_page_setup(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetPageSetupRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_page_setup(request)

    def test_post_page_setup(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        pageSetup = PageSetup(black_and_white= True ,center_horizontally= True ,center_vertically= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostPageSetupRequest( remote_name, 'Sheet1', pageSetup,folder= remote_folder,storage_name= '')
        self.api.post_page_setup(request)

    def test_delete_header_footer(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteHeaderFooterRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.delete_header_footer(request)

    def test_get_header(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetHeaderRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_header(request)

    def test_post_header(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostHeaderRequest( remote_name, 'Sheet1', 1, 'Update add header', True,folder= remote_folder,storage_name= '')
        self.api.post_header(request)

    def test_get_footer(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetFooterRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_footer(request)

    def test_post_footer(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostFooterRequest( remote_name, 'Sheet1', 1, 'add footer script', True,folder= remote_folder,storage_name= '')
        self.api.post_footer(request)

    def test_post_fit_wide_to_pages(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostFitWideToPagesRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.post_fit_wide_to_pages(request)

    def test_post_fit_tall_to_pages(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostFitTallToPagesRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.post_fit_tall_to_pages(request)

if __name__ == '__main__':
    unittest.main()