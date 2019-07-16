import os
import re
from glob import glob
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

cols = []
cols2 = []
cells = []
cells2 = []

filename = '../All Configure/LS_3560_02,no-ip,console,1_all,.txt'



try:
    with open(filename, 'r') as f:
        lines = [line for line in f.readlines() if line.strip()]
except IOError as exc:
    if exc.errno != errno.EISDIR:
        raise

for i in range(0, len(lines)):
    if not lines[i]:
        break 
    if re.search('.*#sh.*int.*desc.*', lines[i]):
        i += 1
        cols.extend(lines[i].split())
        i += 1
        while not re.search('.*#show.*', lines[i]):
            cells.append(re.split(r'\s{2,}',lines[i])) 
            i += 1

    if re.search('.*#sh.*int.*status$', lines[i]):
        i += 1
        cols2.extend(lines[i].split())
        i += 1
        while not re.search('.*#show.*', lines[i]):
            cells2.append(re.split(r'\s{2,}',lines[i])) 
            i += 1   

df1 = pd.DataFrame(cells)
df2 = pd.DataFrame(cells2)

df1.rename(columns = {0:'Interface',
                    1:'Status',
                    2:'Protocol',
                    3:'Description' }, 
            inplace=True)
df2.rename(columns = {0:'Port',
                    1:'Name',
                    2:'Status',
                    3:'Vlan',
                    4:'Duplex',
                    5:'Speed',
                    6:'Type' }, 
            inplace=True)

df3 = pd.merge(df1, df2, left_on='Interface', right_on='Port')
print(df3)
writer = ExcelWriter('test0.xlsx')
df3.to_excel(writer,'Sheet1',index=False)
writer.save()

