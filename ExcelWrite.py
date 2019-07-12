import os
import re
from glob import glob
import pandas as pd
files_list = []
device_detail = []

def readEachLine(file):
    device_name = ''
    device_model = ''
    col = []
    # for line in file:
    #     if re.search('.*#show ver.*', line):
    #         device_name = re.sub('#show ver.*','',line)
    #     if re.search('^Model ([n]|[N])umber.*:', line):
    #         device_model = re.sub('^Model ([n]|[N])umber.*:','',line)
    #         # print(device_name + device_model)
    #     if re.search('.*#sh.*int.*desc.*', line):
    #         lineSection = True:
    while True:
        line = file.readline()
        if not line:
            break
        if re.search('.*#sh.*int.*desc.*', line):
            line = file.readline()
            col = line.split()
            # print(col)
            device_detail.append(col)  
            continue
        if re.search('^[FGVTP]', line) and col :      
            element = re.split(r'\s{2,}',line)        # split into list as an element at least 2 whitespaces
            device_detail.append(element)    
            if not re.search('^[FGVTP]', file.readline()):
                break
    # for detail in device_detail:
    #     print(detail)

def readEachFile(files_list):
    for file_name in files_list:
        try:
            with open(file_name, 'r') as file: 
                readEachLine(file)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise


def matchFilename(path, pattern_list):
    for pattern in pattern_list:
        files_list.extend( glob( path + pattern ))


path = '../All Configure/'                                     # enter path name here
# pattern_list = ['LS_3560_02,no-ip,console,1_all,.txt']         # enter filename pattern here
pattern_list = ['*1_all*', '*step1*']         # enter filename pattern here
matchFilename(path, pattern_list)       # search matching filename
readEachFile(files_list)                # read each matching file

for detail in device_detail:
    print(detail)
