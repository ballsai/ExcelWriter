import os
import re
from glob import glob
import pandas as pd
files_list = []

def readFile(files_list):
    for file in files_list:
        try:
            with open(file, 'r') as f:
                line = f.readlines()
                if re.search('.*#show clock', line):
                    print(line)

        except IOError:
            print('An error occured trying to read the file.')

def matchFilename(path, pattern_list):
    for pattern in pattern_list:
        files_list( glob( path + pattern ))
        readFile(files_list)

path = '/'                 # enter path name here
pattern_list = ['*']         # enter pattern here
matchFilename(path, pattern_list)       # search matching filename
