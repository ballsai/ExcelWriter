import os
import pandas as pd 

class ExcelBuilder:
    
    def __init__(self, frame, filename, dst):
        self.frame = frame
        self.filename = filename
        self.dst = dst + '/'
        self.format = '.xlsx'

    def writeExcel(self):
        file_path = self.dst+self.filename+self.format
        try:
            if os.path.exists(file_path):                          # check if file path is exist in folder
                self.filename += '(copy)'                          # then do not overwrite but make a copy file 
                file_path = self.dst+self.filename+self.format
            
            writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
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
            worksheet.set_column('M:M', 20)

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
            
            print('successful writing file name %s '%self.filename)
        except:
            print('cannot writing file name %s'%self.filename )
