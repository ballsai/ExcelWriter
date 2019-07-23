import os
import pandas as pd 
from openpyxl import load_workbook

class ExcelWriter:
    
    def __init__(self, frame, filename):
        self.frame = frame
        self.filename = filename
        self.path = '../ExcelFile/'
        self.format = '.xlsx'

    def writeExcel(self):
        file_path = self.path+self.filename+self.format
        try:
            if os.path.exists(file_path):
                self.filename += '_new'
                file_path = self.path+self.filename+self.format
            
            writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
            self.frame.to_excel(writer, sheet_name='Sheet1', index=False)
            
            workbook  = writer.book
            worksheet = writer.sheets['Sheet1']

            worksheet.set_column('A:D', 18)
            worksheet.set_column('E:E', 10)
            worksheet.set_column('F:F', 13)
            worksheet.set_column('G:G', 10)
            worksheet.set_column('H:H', 44)
            worksheet.set_column('I:L', 10)
            worksheet.set_column('M:M', 20)

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

            writer.save()
            
            print('successful writing file name %s '%self.filename)
        except:
            print('cannot writing file name %s'%self.filename )
