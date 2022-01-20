# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest
import warnings

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.light_cells_api import LightCellsApi
import AuthUtil

global_api = None
class TestCellsUnlockApi(unittest.TestCase):
    """ CellsApi unit test stubs """
    
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.light_cells_api.LightCellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_unlock(self):
        needUnlock = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "needUnlock.xlsx"
        result = self.api.post_unlock({ "needUnlock.xlsx" :needUnlock},"123456")
        # print(result)
        pass
if __name__ == '__main__':
    unittest.main()
