import os
import re
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from FileReader import FileReader    
from DataFrameWriter import DataFrameWriter
from FileList import FileList

dic = {}
ls = []
directory = '../All Configure/'
KEYWORD = ['.*#show interface description','.*#show interface status$','.*#show interface status.*i connected$']

        
def main():
    # files = FileList(directory,'Zafin_Rack_C5_Switch,no-ip,console,1_all,.txt')
    # # files = FileList(directory,'*.txt')
    # fileList = files.listOfFiles()
    # initDict(fileList)

    # for fl in fileList:
    #     hostname  = getHostname(fl)
    #     f = FileReader(fl)
    #     f.readFile()
    #     f.getStringList('.*#show interface description', '.*#show interface status$')
    #     f.splitString(r'\s{2,}')
    #     dic[hostname].extend(f.stringList)

    # for i in dic['Zafin_Rack_C5_Switch']:
    #     print(i)
    files = FileList(directory, '*Zafin_Rack_C5_Switch*')
    fileList = files.listOfFiles()
    i = 0
    for fl in fileList:
        f = FileReader(fl)
        f.getHostname()
        f.initDict()
        f._dict[f.hostname].append(i)
        i += 1
    
    # f = FileReader('1_Platform_Switch,10.255.11.9,SSH,1_all,.txt')
    f.getHostname()
    # f = FileReader('1_Platform_Switch,10.255.11.9,SSH,1_all,.txt')
    # f.getHostname()
    # f._dict[f.hostname] = ''
    # print(f._dict)
        
main()