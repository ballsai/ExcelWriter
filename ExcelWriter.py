import os
import re
import pandas as pd
from tabulate import tabulate
from pandas import ExcelWriter
from pandas import ExcelFile
from FileReader import FileReader    
from DataFrameWriter import DataFrameWriter
from FileList import FileList

_dir = '../All Configure/'  # directory/folder name
# ! re.split() for string only not list !
def main():
    file_list = FileList(_dir, '*.*') # 
    file_list.getFileList()
    fl = file_list.path_list

    for file_name in fl:
        _file = FileReader(file_name)
        _file.readFile()
        _file.getStringList('.*#show interface description','.*#show interface status$')
        string1 = _file.splitString(r'\s{2,}')
        data1 = DataFrameWriter(string1)
        data1.getDataFrame()
        data1.newHeader()

        _file2 = FileReader(file_name)
        _file2.readFile()
        _file2.getStringList('.*#show interface status$','.*#show interface status.*i connected$')
        string2 = _file2.splitString(r'\s{2,}')
        data2 = DataFrameWriter(string2)
        data2.getDataFrame()
        data2.newHeader()

        data1.mergeDataFrame(data2)
        print(tabulate(data1.df, headers='keys', tablefmt='psql'))

        if data1.df.empty:
            continue
        else:
            writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
            data1.df.to_excel(writer, sheet_name='Sheet1')
            writer.save()

        if not data1.df.empty:
            break


main()