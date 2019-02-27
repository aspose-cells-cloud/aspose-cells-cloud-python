        """
        Test case for cells_conditional_formattings_put_worksheet_format_condition_area
        add a cell area for format condition             
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0       
        cellArea = "A1:C10"       
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_conditional_formattings_put_worksheet_format_condition_area(name, sheet_name, index, cellArea , folder=folder)