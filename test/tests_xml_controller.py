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

class TestXmlControllerApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_post_workbook_export_xml(self):
        remote_folder = 'TestData/In'

        local_name = 'Template.xlsx'
        remote_name = 'Template.xlsx'

        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookExportXMLRequest( remote_name,folder= remote_folder,storage_name= '')
        self.api.post_workbook_export_xml(request)


    def test_post_workbook_import_xml(self):
        remote_folder = 'TestData/In'

        local_name = 'Template.xlsx'
        data_xml = 'data.xml'
        remote_name = 'Template.xlsx'

        importXMLRequestXMLFileSource = FileSource(file_source_type= 'CloudFileSystem' ,file_path= remote_folder + '/data.xml' )
        importXMLRequestImportPosition = ImportPosition(sheet_name= 'Sheet1' ,row_index= 3 ,column_index= 4 )
        importXMLRequest = ImportXMLRequest(xml_file_source= importXMLRequestXMLFileSource ,import_position= importXMLRequestImportPosition )
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
        result = AuthUtil.Ready(self.api, data_xml, remote_folder + '/data.xml' ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PostWorkbookImportXMLRequest( remote_name, import_xml_request =   importXMLRequest , folder= remote_folder,storage_name= '')
        self.api.post_workbook_import_xml(request)


if __name__ == '__main__':
    unittest.main()