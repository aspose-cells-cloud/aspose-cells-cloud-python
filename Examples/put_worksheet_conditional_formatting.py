  """
        Test case for cells_conditional_formattings_put_worksheet_conditional_formatting
        Add a condition formatting.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cellArea = "A1:C10"         
        formatcondition = FormatCondition()
        formatcondition.type = "CellValue"
        formatcondition.operator = "Between"
        formatcondition.formula1 = "v1"
        formatcondition.formula2 = "v2"
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_conditional_formattings_put_worksheet_conditional_formatting(name, sheet_name,cellArea,formatcondition=formatcondition,folder=folder)