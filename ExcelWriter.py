import os
import re   # pip install re
import pandas as pd # pip install pandas
from tabulate import tabulate  # pip install tabulate 
from pandas import ExcelWriter
from pandas import ExcelFile
from FileReader import FileReader    
from DataFrameWriter import DataFrameWriter
from FileList import FileList

_dir = '../All Configure/'  # directory or folder name
def main():
    file_list = FileList(_dir, '*.*') # 
    file_list.getFileList()
    fl = file_list.path_list

    data_frame = pd.DataFrame([])

    for file_name in fl:

        _file = FileReader(file_name)
        _file.getHostname()
        _file.readFile()
        hostname = _file.hostname
        model = _file.getModel('^Model (n|N)umber.*:')
        version = _file.getModel('Cisco IOS Software.*Version')
        version = re.sub('(,.*|RE.*)','',version)
        serial = _file.getModel('.*(S|s)erial (N|n)umber.*:')

        _file.getStringList('.*#show interface description','.*#show.*')
        string1 = _file.splitString(r'\s{2,}')
        data1 = DataFrameWriter(string1)
        data1.getDataFrame()
        # data1.newHeader()

        _file2 = FileReader(file_name)
        _file2.readFile()
        _file2.getStringList('.*#show interface status$','.*#show.*')
        rmstring = _file2.removeSubstring('\s{2,}.*(connected|notconnect|disabled)')
        _file2.string_list = rmstring
        string2 = _file2.splitString(r'\s{1,}')
        data2 = DataFrameWriter(string2)
        data2.getDataFrame()
        # data2.newHeader()

        data1.mergeDataFrame(data2)
        # data1.mergeDataFrame(data2)
        # data_frame = data2.df
        # data_frame = data_frame.iloc[1:]
        # data_frame.drop(columns=1)
        if not data1.df.empty:
            data1.df.insert(0, 'Serial','')
            data1.df.insert(0, 'Version','')
            data1.df.insert(0, 'Model','')
            data1.df.insert(0, 'Name','')
            # print(data1.df)
            data1.df['Name'] = [hostname]+['']*(len(data1.df)-1)
            data1.df['Model'] = [model]+['']*(len(data1.df)-1)
            data1.df['Version'] = [version]+['']*(len(data1.df)-1)
            data1.df['Serial'] = [serial]+['']*(len(data1.df)-1)
            print(tabulate(data1.df, headers='keys', tablefmt='psql'))

        # print(tabulate(data2.df, headers='keys', tablefmt='psql'))
        if not data1.df.empty:
            writer = pd.ExcelWriter('ExcelFile/'+ hostname +'.xlsx', engine='xlsxwriter')
            data1.df.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.save()

main()