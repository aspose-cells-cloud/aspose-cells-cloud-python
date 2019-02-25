        """
        Test case for cells_auto_filter_put_worksheet_dynamic_filter
        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range ='A1:C10'
        fieldIndex = 0  
        dynamicFilterType = "May"        
        matchBlanks =True
        refresh =True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_put_worksheet_dynamic_filter(name, sheet_name, range,fieldIndex, dynamicFilterType,match_blanks=matchBlanks, refresh=refresh,folder=folder)