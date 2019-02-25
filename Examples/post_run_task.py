import os
import sys

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import CalculationOptions
from asposecellscloud.models import FontSetting
from asposecellscloud.models import Font
from asposecellscloud.models import Style


api_client = AuthUtil.GetApiClient()
api = asposecellscloud.apis.cells_api.CellsApi(api_client)
        name ='Book1.xlsx'
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        task1 = TaskDescription()
        task1.task_type = 'SplitWorkbook'
        param1 = SplitWorkbookTaskParameter()
        param1.destination_file_format = 'xlsx'
        fileSource = FileSource()
        fileSource.file_path = folder
        fileSource.file_source_type = 'CloudFileSystem'
        param1.destination_file_position = fileSource
        param1.split_name_rule = 'sheetname'
        workbook = FileSource()
        workbook.file_path = folder + "\\" + name
        workbook.file_source_type = 'CloudFileSystem'
        param1.workbook = workbook
        task1.task_parameter = param1
        taskData = TaskData()
        tasks = [task1]
        taskData.tasks = tasks
        result = self.api.cells_task_post_run_task(taskData)