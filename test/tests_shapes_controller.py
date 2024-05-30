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

class TestShapesControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_worksheet_shapes(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetShapesRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_shapes(request)
        time.sleep(1)

    def test_get_worksheet_shape(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetShapeRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.get_worksheet_shape(request)
        time.sleep(1)

    def test_put_worksheet_shape(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        shapeDTO = Shape()
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetShapeRequest( remote_name, 'Sheet1',shape_dto= shapeDTO,drawing_type= 'arc',upper_left_row= 1,upper_left_column= 1,top= 10,left= 10,width= 100,height= 100,folder= remote_folder,storage_name= '')
        self.api.put_worksheet_shape(request)
        time.sleep(1)

    def test_delete_worksheet_shapes(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetShapesRequest( remote_name, 'Sheet1',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_shapes(request)
        time.sleep(1)

    def test_delete_worksheet_shape(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetShapeRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_shape(request)
        time.sleep(1)

    def test_post_worksheet_shape(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        dto = Shape(lower_right_column= 10 )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetShapeRequest( remote_name, 'Sheet1', 0, dto,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_shape(request)
        time.sleep(1)

    def test_post_worksheet_group_shape(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        listShape = [
            0,
            1
        ]
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetGroupShapeRequest( remote_name, 'Sheet6', listShape,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_group_shape(request)
        time.sleep(1)

    def test_post_worksheet_ungroup_shape(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetUngroupShapeRequest( remote_name, 'Sheet1', 0,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_ungroup_shape(request)
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()