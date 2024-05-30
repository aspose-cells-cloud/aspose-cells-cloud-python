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

class TestSparklineGroupsControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_worksheet_sparkline_groups(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetSparklineGroupsRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_sparkline_groups(request)
        time.sleep(1)

    def test_get_worksheet_sparkline_group(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetSparklineGroupRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_sparkline_group(request)
        time.sleep(1)

    def test_delete_worksheet_sparkline_groups(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetSparklineGroupsRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_sparkline_groups(request)
        time.sleep(1)

    def test_delete_worksheet_sparkline_group(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetSparklineGroupRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_sparkline_group(request)
        time.sleep(1)

    def test_put_worksheet_sparkline_group(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetSparklineGroupRequest( remote_name, 'Sheet1', 'Line', 'C6:E13', False, 'G6:G13',folder= remote_folder,storage_name= '')
        self.api.put_worksheet_sparkline_group(request)
        time.sleep(1)

    def test_post_worksheet_sparkline_group(self):
        remote_folder = 'TestData/In'

        local_name = 'TestCase.xlsx'
        remote_name = 'TestCase.xlsx'

        sparklineGroup = SparklineGroup(display_hidden= True ,plot_right_to_left= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetSparklineGroupRequest( remote_name, 'Sheet1', 0, sparklineGroup,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_sparkline_group(request)
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()