import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from FileReader import FileReader    
from DataFrameWriter import DataFrameWriter
from FileList import FileList

PATH = '../All Configure/'
FILE_PATTERN = '*1_all*'
KEYWORD = ['.*#show interface description','.*#show interface status$','.*#show interface status.*i connected$']
def getLines(f, start, end):
    return f.findText(start,end)

def main():
    files = FileList(PATH,FILE_PATTERN)
    filelist = files.listOfFiles()

    for fl in filelist:

        f = FileReader(fl)
        
        f.readLines()
        f.getField('Name','(#.*show ver.*|(>|#)enable$)')
        f.getField('Model','^Model ([n]|[N])umber.*:')

        data_0 = DataFrameWriter(f.fields)
        data_0.listToDataFrame()
        data_0.transposeDataFrame()
        data_0.newHeader()

        lines_1 = getLines(f, KEYWORD[0], KEYWORD[1])
        lines_2 = getLines(f, KEYWORD[1], KEYWORD[2])

        data_1 = DataFrameWriter(lines_1)
        data_1.listToDataFrame()
        data_1.newHeader()

        data_2 = DataFrameWriter(lines_2)
        data_2.listToDataFrame()
        data_2.newHeader()
    
        # data_1.mergeDataFrame(data_2.df)
        print(data_2.df)

        # data_0.concatDataFrame(data_1.df)
        # print(data_0.df)


main()