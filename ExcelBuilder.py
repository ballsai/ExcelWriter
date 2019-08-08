import os
import pandas as pd 

class ExcelBuilder:
    
    def __init__(self, frame, filename, dst):
        self.frame = frame
        self.filename = filename
        self.dst = '%s\\'%(dst)
        self.format = '.xlsx'

    def writeExcel(self):
        path_name = '%s%s%s'%(self.dst, self.filename, self.format)
        try:
            if os.path.exists(path_name):                          # check if file path is exist in folder
                string = '_(2)'                          # then do not overwrite but make a copy file 
                path_name = '%s%s%s%s'%(self.dst, self.filename, string, self.format)
            
            writer = pd.ExcelWriter(path_name, engine='xlsxwriter')
            self.frame.to_excel(writer, sheet_name='Sheet1', index=False) 
            
            workbook  = writer.book
            worksheet = writer.sheets['Sheet1']

            # set columns width
            worksheet.set_column('A:D', 18)
            worksheet.set_column('E:E', 10)
            worksheet.set_column('F:F', 13)
            worksheet.set_column('G:G', 10)
            worksheet.set_column('H:H', 35)
            worksheet.set_column('I:L', 10)
            worksheet.set_column('M:M', 23)

            # set header column
            header_format = workbook.add_format({
                            'bold': True,
                            'text_wrap': True,
                            'valign': 'top',
                            'bg_color': '#000000',
                            'font_color': '#FFFFFF',
                            'border': 1,
                            'border_color': '#828282'})
            
            for col_num, value in enumerate(self.frame.columns.values):
                worksheet.write(0, col_num, value, header_format)

            writer.save()   # save as .xlsx file
            
            print('%s  Completed'%self.filename)
        except:
            print('%s Failed'%self.filename )
