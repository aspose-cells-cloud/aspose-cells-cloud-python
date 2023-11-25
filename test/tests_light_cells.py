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

class TestLightCellsApi(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_post_split_csv(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'csv'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_xls(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xls'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_html(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'html'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_mhtml(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'mhtml'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_ods(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'ods'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_pdf(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'pdf'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_xml(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xml'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_txt(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'txt'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_tif(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'tif'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_xlsb(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xlsb'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_xlsm(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xlsm'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_xlsx(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xlsx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_xltm(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xltm'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_xltx(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xltx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_xps(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xps'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_png(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'png'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_jpg(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'jpg'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_gif(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'gif'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_emf(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'emf'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_bmp(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'bmp'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_md(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'md'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_numbers(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'numbers'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_wmf(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'wmf'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_svg(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'svg'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_docx(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'docx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_pptx(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'pptx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_json(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'json'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_split_sql(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'sql'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSplitRequest( mapFiles, format)
        self.api.post_split(request)


    def test_post_assemble_csv(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'csv'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_xls(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xls'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_html(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'html'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_mhtml(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'mhtml'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_ods(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'ods'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_pdf(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'pdf'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_xml(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xml'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_txt(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'txt'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_tif(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'tif'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_xlsb(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xlsb'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_xlsm(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xlsm'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_xlsx(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xlsx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_xltm(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xltm'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_xltx(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xltx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_xps(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xps'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_png(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'png'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_jpg(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'jpg'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_gif(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'gif'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_emf(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'emf'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_bmp(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'bmp'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_md(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'md'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_numbers(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'numbers'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_wmf(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'wmf'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_svg(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'svg'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_docx(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'docx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_pptx(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'pptx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_json(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'json'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_assemble_sql(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'sql'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostAssembleRequest( mapFiles, 'ds',format= format)
        self.api.post_assemble(request)


    def test_post_export_csv_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'csv'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xls_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xls'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_html_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'html'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_mhtml_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'mhtml'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_ods_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'ods'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_pdf_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'pdf'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xml_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xml'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_txt_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'txt'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_tif_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'tif'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xlsb_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xlsb'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xlsm_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xlsm'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xlsx_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xlsx'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xltm_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xltm'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xltx_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xltx'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xps_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xps'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_png_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'png'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_jpg_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'jpg'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_gif_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'gif'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_emf_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'emf'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_bmp_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'bmp'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_md_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'md'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_numbers_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'numbers'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_wmf_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'wmf'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_svg_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'svg'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_docx_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'docx'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_pptx_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'pptx'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_json_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'json'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_sql_workbook(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'sql'
        object_type = 'workbook'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_csv_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'csv'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xls_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xls'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_html_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'html'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_mhtml_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'mhtml'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_ods_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'ods'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_pdf_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'pdf'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xml_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xml'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_txt_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'txt'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_tif_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'tif'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xlsb_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xlsb'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xlsm_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xlsm'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xlsx_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xlsx'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xltm_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xltm'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xltx_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xltx'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xps_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xps'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_png_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'png'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_jpg_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'jpg'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_gif_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'gif'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_emf_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'emf'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_bmp_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'bmp'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_md_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'md'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_numbers_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'numbers'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_wmf_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'wmf'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_svg_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'svg'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_docx_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'docx'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_pptx_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'pptx'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_json_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'json'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_sql_worksheet(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'sql'
        object_type = 'worksheet'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_pdf_chart(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'pdf'
        object_type = 'chart'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_tif_chart(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'tif'
        object_type = 'chart'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_png_chart(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'png'
        object_type = 'chart'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_jpg_chart(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'jpg'
        object_type = 'chart'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_gif_chart(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'gif'
        object_type = 'chart'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_emf_chart(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'emf'
        object_type = 'chart'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_bmp_chart(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'bmp'
        object_type = 'chart'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_png_picture(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'png'
        object_type = 'picture'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_jpg_picture(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'jpg'
        object_type = 'picture'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_gif_picture(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'gif'
        object_type = 'picture'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_emf_picture(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'emf'
        object_type = 'picture'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_bmp_picture(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'bmp'
        object_type = 'picture'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_csv_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'csv'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xls_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xls'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_html_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'html'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_mhtml_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'mhtml'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_ods_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'ods'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_pdf_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'pdf'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xml_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xml'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_txt_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'txt'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_tif_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'tif'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xlsb_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xlsb'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xlsm_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xlsm'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xlsx_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xlsx'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xltm_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xltm'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xltx_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xltx'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_xps_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'xps'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_png_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'png'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_jpg_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'jpg'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_gif_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'gif'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_emf_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'emf'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_bmp_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'bmp'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_md_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'md'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_numbers_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'numbers'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_wmf_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'wmf'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_svg_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'svg'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_docx_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'docx'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_pptx_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'pptx'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_json_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'json'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_sql_listobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'sql'
        object_type = 'listobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_png_oleobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'png'
        object_type = 'oleobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_jpg_oleobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'jpg'
        object_type = 'oleobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_gif_oleobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'gif'
        object_type = 'oleobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_emf_oleobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'emf'
        object_type = 'oleobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_export_bmp_oleobject(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        book1_xlsx = 'Book1.xlsx'

        format = 'bmp'
        object_type = 'oleobject'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostExportRequest( mapFiles,object_type= object_type,format= format)
        self.api.post_export(request)


    def test_post_compress_50(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        compress_level = 50

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostCompressRequest( mapFiles,compress_level= compress_level)
        self.api.post_compress(request)


    def test_post_compress_90(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        compress_level = 90

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostCompressRequest( mapFiles,compress_level= compress_level)
        self.api.post_compress(request)


    def test_post_merge_csv_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'csv'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_xls_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xls'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_html_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'html'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_mhtml_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'mhtml'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_ods_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'ods'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_pdf_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'pdf'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_xml_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xml'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_txt_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'txt'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_tif_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'tif'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_xlsb_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xlsb'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_xlsm_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xlsm'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_xlsx_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xlsx'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_xltm_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xltm'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_xltx_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xltx'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_xps_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'xps'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_png_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'png'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_jpg_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'jpg'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_gif_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'gif'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_emf_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'emf'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_bmp_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'bmp'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_md_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'md'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_numbers_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'numbers'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_wmf_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'wmf'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_svg_true(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'svg'
        merge_to_one_sheet = True

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_docx_false(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'docx'
        merge_to_one_sheet = False

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_pptx_false(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'pptx'
        merge_to_one_sheet = False

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_json_false(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'json'
        merge_to_one_sheet = False

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_merge_sql_false(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        format = 'sql'
        merge_to_one_sheet = False

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostMergeRequest( mapFiles,format= format,merge_to_one_sheet= merge_to_one_sheet)
        self.api.post_merge(request)


    def test_post_unlock(self):
        need_unlock_xlsx = 'needUnlock.xlsx'

        mapFiles = { 
            need_unlock_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +need_unlock_xlsx             
        }
     
        request =  PostUnlockRequest( mapFiles, '123456')
        self.api.post_unlock(request)


    def test_post_protect(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
        protectWorkbookRequest = ProtectWorkbookRequest(aways_open_read_only= True ,encrypt_with_password= '123456' )


     
        request =  PostProtectRequest( mapFiles, protectWorkbookRequest,password= '123456')
        self.api.post_protect(request)


    def test_post_protect__protect_workbook_request(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
        protectWorkbookRequest = ProtectWorkbookRequest(aways_open_read_only= True ,encrypt_with_password= '123456' )


     
        request =  PostProtectRequest( mapFiles, protectWorkbookRequest)
        self.api.post_protect(request)


    def test_post_search(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostSearchRequest( mapFiles, '12')
        self.api.post_search(request)


    def test_post_replace(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostReplaceRequest( mapFiles, '12', 'newtext')
        self.api.post_replace(request)


    def test_post_replace_only_sheetname(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostReplaceRequest( mapFiles, '12', 'newtext',sheetname= 'Sheet1')
        self.api.post_replace(request)


    def test_post_watermark(self):
        assembly_test_xlsx = 'assemblytest.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        mapFiles = { 
            assembly_test_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +assembly_test_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostWatermarkRequest( mapFiles, 'aspose.cells cloud sdk', '#773322')
        self.api.post_watermark(request)


    def test_post_clear_objects_chart(self):
        book1_xlsx = 'Book1.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        objecttype = 'chart'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostClearObjectsRequest( mapFiles, objecttype)
        self.api.post_clear_objects(request)


    def test_post_clear_objects_comment(self):
        book1_xlsx = 'Book1.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        objecttype = 'comment'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostClearObjectsRequest( mapFiles, objecttype)
        self.api.post_clear_objects(request)


    def test_post_clear_objects_picture(self):
        book1_xlsx = 'Book1.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        objecttype = 'picture'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostClearObjectsRequest( mapFiles, objecttype)
        self.api.post_clear_objects(request)


    def test_post_clear_objects_shape(self):
        book1_xlsx = 'Book1.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        objecttype = 'shape'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostClearObjectsRequest( mapFiles, objecttype)
        self.api.post_clear_objects(request)


    def test_post_clear_objects_listobject(self):
        book1_xlsx = 'Book1.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        objecttype = 'listobject'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostClearObjectsRequest( mapFiles, objecttype)
        self.api.post_clear_objects(request)


    def test_post_clear_objects_hyperlink(self):
        book1_xlsx = 'Book1.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        objecttype = 'hyperlink'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostClearObjectsRequest( mapFiles, objecttype)
        self.api.post_clear_objects(request)


    def test_post_clear_objects_oleobject(self):
        book1_xlsx = 'Book1.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        objecttype = 'oleobject'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostClearObjectsRequest( mapFiles, objecttype)
        self.api.post_clear_objects(request)


    def test_post_clear_objects_pivottable(self):
        book1_xlsx = 'Book1.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        objecttype = 'pivottable'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostClearObjectsRequest( mapFiles, objecttype)
        self.api.post_clear_objects(request)


    def test_post_clear_objects_validation(self):
        book1_xlsx = 'Book1.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        objecttype = 'validation'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostClearObjectsRequest( mapFiles, objecttype)
        self.api.post_clear_objects(request)


    def test_post_clear_objects__background(self):
        book1_xlsx = 'Book1.xlsx'
        data_source_xlsx = 'datasource.xlsx'

        objecttype = 'Background'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx ,data_source_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +data_source_xlsx             
        }
     
        request =  PostClearObjectsRequest( mapFiles, objecttype)
        self.api.post_clear_objects(request)


    def test_post_repair_xlsx(self):
        book1_xlsx = 'Book1.xlsx'

        format = 'xlsx'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostRepairRequest( mapFiles,format= format)
        self.api.post_repair(request)


    def test_post_repair_pdf(self):
        book1_xlsx = 'Book1.xlsx'

        format = 'pdf'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostRepairRequest( mapFiles,format= format)
        self.api.post_repair(request)


    def test_post_repair_csv(self):
        book1_xlsx = 'Book1.xlsx'

        format = 'csv'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostRepairRequest( mapFiles,format= format)
        self.api.post_repair(request)


    def test_post_repair_png(self):
        book1_xlsx = 'Book1.xlsx'

        format = 'png'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostRepairRequest( mapFiles,format= format)
        self.api.post_repair(request)


    def test_post_reverse_rows_pdf(self):
        book1_xlsx = 'Book1.xlsx'

        rotate_type = 'rows'
        format = 'pdf'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostReverseRequest( mapFiles, rotate_type,format= format)
        self.api.post_reverse(request)


    def test_post_reverse_cols_pdf(self):
        book1_xlsx = 'Book1.xlsx'

        rotate_type = 'cols'
        format = 'pdf'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostReverseRequest( mapFiles, rotate_type,format= format)
        self.api.post_reverse(request)


    def test_post_reverse_both_pdf(self):
        book1_xlsx = 'Book1.xlsx'

        rotate_type = 'both'
        format = 'pdf'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostReverseRequest( mapFiles, rotate_type,format= format)
        self.api.post_reverse(request)


    def test_post_reverse_rows_csv(self):
        book1_xlsx = 'Book1.xlsx'

        rotate_type = 'rows'
        format = 'csv'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostReverseRequest( mapFiles, rotate_type,format= format)
        self.api.post_reverse(request)


    def test_post_reverse_cols_png(self):
        book1_xlsx = 'Book1.xlsx'

        rotate_type = 'cols'
        format = 'png'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostReverseRequest( mapFiles, rotate_type,format= format)
        self.api.post_reverse(request)


    def test_post_reverse_both_xlsx(self):
        book1_xlsx = 'Book1.xlsx'

        rotate_type = 'both'
        format = 'xlsx'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  PostReverseRequest( mapFiles, rotate_type,format= format)
        self.api.post_reverse(request)


    def test_get_metadata(self):
        book1_xlsx = 'Book1.xlsx'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  GetMetadataRequest( mapFiles,type= 'all')
        self.api.get_metadata(request)


    def test_delete_metadata(self):
        book1_xlsx = 'Book1.xlsx'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
     
        request =  DeleteMetadataRequest( mapFiles,type= 'all')
        self.api.delete_metadata(request)


    def test_post_metadata(self):
        book1_xlsx = 'Book1.xlsx'

        mapFiles = { 
            book1_xlsx: os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" +book1_xlsx             
        }
        cellsDocumentscellsDocument0 = CellsDocumentProperty(name= 'Author' ,value= 'roy.wang' )
        cellsDocuments = [
            cellsDocumentscellsDocument0
        ]

     
        request =  PostMetadataRequest( mapFiles, cellsDocuments)
        self.api.post_metadata(request)


if __name__ == '__main__':
    unittest.main()