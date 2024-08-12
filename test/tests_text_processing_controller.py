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

class TestTextProcessingControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_post_add_text_content(self):
        remote_folder = 'TestData/In'

        local_name = 'BookText.xlsx'
        remote_name = 'BookText.xlsx'

        addTextOptionsDataSource = DataSource(data_source_type= 'CloudFileSystem' ,data_path= 'BookText.xlsx' )
        addTextOptions = AddTextOptions(data_source= addTextOptionsDataSource ,text= 'Aspose.Cells Cloud is an excellent product.' ,worksheet= '202401' ,select_poistion= 'AtTheBeginning' ,skip_empty_cells= True )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostAddTextContentRequest( addTextOptions)
        self.api.post_add_text_content(request)
        

    def test_post_trim_content(self):
        remote_folder = 'TestData/In'

        local_name = 'BookText.xlsx'
        remote_name = 'BookText.xlsx'

        trimContentOptionsDataSource = DataSource(data_source_type= 'CloudFileSystem' ,data_path= 'BookText.xlsx' )
        trimContentOptionsScopeOptions = ScopeOptions(scope= 'EntireWorkbook',scope_items=[] )
        trimContentOptions = TrimContentOptions(data_source= trimContentOptionsDataSource ,trim_leading= True ,trim_trailing= True ,trim_space_between_word_to1= True ,remove_all_line_breaks= True ,scope_options= trimContentOptionsScopeOptions )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostTrimContentRequest( trimContentOptions)
        self.api.post_trim_content(request)
        

if __name__ == '__main__':
    unittest.main()