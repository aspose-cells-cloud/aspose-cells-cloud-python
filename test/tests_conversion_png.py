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

class TestConversionPngApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_convert_workbook_html(self):
        remote_folder = 'TestData/In'

        local_name = 'cloud.png'
        remote_name = 'cloud.png'

        format = 'html'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_mhtml(self):
        remote_folder = 'TestData/In'

        local_name = 'cloud.png'
        remote_name = 'cloud.png'

        format = 'mhtml'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_ods(self):
        remote_folder = 'TestData/In'

        local_name = 'cloud.png'
        remote_name = 'cloud.png'

        format = 'ods'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_pdf(self):
        remote_folder = 'TestData/In'

        local_name = 'cloud.png'
        remote_name = 'cloud.png'

        format = 'pdf'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_xml(self):
        remote_folder = 'TestData/In'

        local_name = 'cloud.png'
        remote_name = 'cloud.png'

        format = 'xml'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_tif(self):
        remote_folder = 'TestData/In'

        local_name = 'cloud.png'
        remote_name = 'cloud.png'

        format = 'tif'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_xps(self):
        remote_folder = 'TestData/In'

        local_name = 'cloud.png'
        remote_name = 'cloud.png'

        format = 'xps'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_jpg(self):
        remote_folder = 'TestData/In'

        local_name = 'cloud.png'
        remote_name = 'cloud.png'

        format = 'jpg'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_md(self):
        remote_folder = 'TestData/In'

        local_name = 'cloud.png'
        remote_name = 'cloud.png'

        format = 'md'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_numbers(self):
        remote_folder = 'TestData/In'

        local_name = 'cloud.png'
        remote_name = 'cloud.png'

        format = 'numbers'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_svg(self):
        remote_folder = 'TestData/In'

        local_name = 'cloud.png'
        remote_name = 'cloud.png'

        format = 'svg'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


    def test_convert_workbook_docx(self):
        remote_folder = 'TestData/In'

        local_name = 'cloud.png'
        remote_name = 'cloud.png'

        format = 'docx'

        mapFiles = { 
            local_name: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +local_name             
        }
        result = AuthUtil.Ready(self.api, local_name, remote_folder + '/' + remote_name ,  '')
        self.assertTrue(len(result.uploaded)>0) 
     
        request =  PutConvertWorkbookRequest( mapFiles,format= format)
        self.api.put_convert_workbook(request)


if __name__ == '__main__':
    unittest.main()