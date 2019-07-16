import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from FileReader import FileReader    
from DataFrameWriter import DataFrameWriter
from FileList import FileList

_file = []
PATH = './All Configure/'
FILE_PATTERN = '*1_all*'
KEYWORD = ['.*#show interface description','.*#show interface status$','.*#show interface status | i connected']

def initList(_file, filelist):
    for i in range(0, len(filelist)):
        _file.append(0)

files = FileList(PATH,FILE_PATTERN)
filelist = files.listOfFiles()
initList(_file, filelist)

for i in range(0, len(filelist)):
    _file[i] = FileReader(filelist[i])
    _file[i].readLines()
    list1 = _file[i].findText(KEYWORD[0],KEYWORD[1])
    list2 = _file[i].findText(KEYWORD[1],KEYWORD[2])
    d1 = DataFrameWriter(list1)
    d1.listToDataFrame()
    d1.newHeader()
    d2 = DataFrameWriter(list2)
    d2.listToDataFrame()
    d2.newHeader()