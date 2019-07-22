import os
import re
import glob as glob
import pandas as pd 
from tabulate import tabulate

from FileReader import FileReader
from DataFrameBuilder import DataFrameBuilder

class ExcelWriter:
    
    def __init__(self, frame, filename):
        self.frame = frame
        self.filename = filename

    def writeExcel(self):
        try:
            writer = pd.ExcelWriter('../ExcelFile/'+ self.filename +'.xlsx', engine='xlsxwriter')
            self.frame.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.save()
            print('successful writing file name %s '%self.filename)
        except:
            print('cannot writing file name %s'%self.filename )

def main():

    directory = '../All Configure/'
    column = []
    detail = []
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                f = FileReader(directory + entry.name)
                f.readFile()
                # search section in text by substring
                hostname = f.requiredHostname()
                model = f.requiredModel()
                serial = f.requiredSerial()
                version = f.requiredVersion()

                interface_description = f.requiredInterfaceDescription()
                interface_status = f.requiredInterfaceStatus()

                required_file = f.isRequired(interface_description) # if '.*#show interface description' exist (section_1 is not an empty list), it is a required file
                # log.append(entry.name + ' : %r' %required_file)
                
                if required_file:
                    # if not version:
                    #     detail.append(hostname)

                    desc = pd.DataFrame(interface_description)
                    desc_df = DataFrameBuilder(desc)
                    status = pd.DataFrame(interface_status)
                    status_df = DataFrameBuilder(status)

                    # frame = desc_df + status_df

                    # if len(frame.dataframe.columns) == 4:
                    #     frame.addColumn(cols =  ['Interface','Status','Protocol','Description']) 
                    # elif len(frame.dataframe.columns) == 10:
                    #     frame.dropColumn(cols =[5,6])
                    #     frame.addColumn(cols =  ['Interface','Status','Protocol','Description','Vlan','Dupex','Speed','Type']) 
 
                    # else: 
                    #     column.append(hostname+': %d' %len(frame.dataframe.columns)) 
                    
                    # frame.insertColumn(col_index = 0, col_name = 'Sotfware Version', value = [version]+['']*(len(frame.dataframe)-1))
                    # frame.insertColumn(col_index = 0, col_name = 'Serial No.', value = [serial]+['']*(len(frame.dataframe)-1))
                    # frame.insertColumn(col_index = 0, col_name = 'Model No.', value = [model]+['']*(len(frame.dataframe)-1))
                    # frame.insertColumn(col_index = 0, col_name = 'Hostname', value = [hostname]+['']*(len(frame.dataframe)-1))
                    # print(hostname) 
                    # print(tabulate(status_df.dataframe, headers='keys', tablefmt='psql'))
                    # print(hostname+' %d'%len(status_df.dataframe.columns))
                    # excel = ExcelWriter(frame.dataframe, hostname)
                    # excel.writeExcel()
                    if len(status_df.dataframe.columns) != 0 and len(status_df.dataframe.columns) != 5:
                        detail.append("%s : %d"%(hostname, len(status_df.dataframe.columns)))
                        
    except IOError:
        print('cannot open directory name ',directory )

    # try:
    #     with open("columns.txt", "w") as output:
    #         output.write('\n'.join(column))
    #     print('successful writing')
    # except IOError:
    #     print('cannot write file name log.txt')
    
    try:
        with open("details.txt", "w") as output:
            output.write('\n'.join(detail))
    except IOError:
        print('cannot write file name log.txt')

main()        