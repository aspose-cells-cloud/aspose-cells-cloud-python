
        """
        Test case for cells_auto_filter_put_worksheet_custom_filter
        Filters a list with a custom criteria.             
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range ='A1:C10'
        fieldIndex = 0  
        operatorType1 = "LessOrEqual"
        criteria1 = "test"
        isAnd = True
        operatorType2 = "LessOrEqual"
        criteria2 = "test"
        matchBlanks = True
        refresh = True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_put_worksheet_custom_filter(name, sheet_name,range ,fieldIndex, operatorType1 , criteria1,is_and=isAnd, operator_type2=operatorType2 , criteria2=criteria2,match_blanks=matchBlanks, refresh=refresh, folder=folder)