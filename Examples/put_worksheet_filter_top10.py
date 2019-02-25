        """
        Test case for cells_auto_filter_put_worksheet_filter_top10
        Filter the top 10 item in the list
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range ='A1:C10'
        fieldIndex = 0  
        isTop =True
        isPercent =True
        itemCount =1        
        matchBlanks =True
        refresh =True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_put_worksheet_filter_top10(name, sheet_name, range,fieldIndex, isTop,isPercent, itemCount,match_blanks= matchBlanks,refresh= refresh,folder=folder)