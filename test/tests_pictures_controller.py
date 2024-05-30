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

class TestPicturesControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_worksheet_pictures(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetPicturesRequest( remote_name, 'Sheet6',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_pictures(request)
        time.sleep(1)

    def test_get_worksheet_picture_with_format(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  GetWorksheetPictureWithFormatRequest( remote_name, 'Sheet6', 0, 'png',folder= remote_folder,storage_name= '')
        self.api.get_worksheet_picture_with_format(request)
        time.sleep(1)

    def test_put_worksheet_add_picture(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        water_mark_png = 'WaterMark.png'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, water_mark_png, remote_folder + '/WaterMark.png' ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutWorksheetAddPictureRequest( remote_name, 'Sheet6',upper_left_row= 1,upper_left_column= 1,lower_right_row= 10,lower_right_column= 10,picture_path= remote_folder + '/WaterMark.png',folder= remote_folder,storage_name= '')
        self.api.put_worksheet_add_picture(request)
        time.sleep(1)

    def test_post_worksheet_picture(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        picture = Picture(left= 10 ,bottom= 10 )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorksheetPictureRequest( remote_name, 'Sheet6', 0, picture,folder= remote_folder,storage_name= '')
        self.api.post_worksheet_picture(request)
        time.sleep(1)

    def test_delete_worksheet_picture(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetPictureRequest( remote_name, 'Sheet6', 0,folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_picture(request)
        time.sleep(1)

    def test_delete_worksheet_pictures(self):
        remote_folder = 'TestData/In'

        local_name = 'Book1.xlsx'
        remote_name = 'Book1.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  DeleteWorksheetPicturesRequest( remote_name, 'Sheet6',folder= remote_folder,storage_name= '')
        self.api.delete_worksheet_pictures(request)
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()