        """
        Test case for cells_auto_filter_put_worksheet_date_filter
        add date filter in worksheet 
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range ='A1:C10'
        fieldIndex = 0  
        dateTimeGroupingType ="Day"
        year = 2010
        month = 10
        day = 10
        hour = 10
        minute = 10
        second = 10
        matchBlanks =True
        refresh =True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_put_worksheet_date_filter(name, sheet_name, range,fieldIndex, dateTimeGroupingType,year=year,month=month,day=day,hour=hour,minute=minute,second=second,match_blanks=matchBlanks, refresh=refresh,folder=folder)
