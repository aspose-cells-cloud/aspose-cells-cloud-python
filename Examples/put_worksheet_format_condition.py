     """
        Test case for cells_conditional_formattings_put_worksheet_format_condition
        Add a format condition.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0     
        cellArea = "A1:C10"     
        type = "CellValue"     
        operatorType = "Between"     
        formula1 = "v1"     
        formula2 = "v2"         
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_conditional_formattings_put_worksheet_format_condition(name, sheet_name,index , cellArea,   type,  operatorType ,formula1,formula2, folder=folder)