import os
import sys
import re
import pandas as pd 
import time

from FileReader import FileReader
from DataFrameBuilder import DataFrameBuilder
from ExcelBuilder import ExcelBuilder

class ExcelWriter:

    def __init__(self, source, destination):
        self.src = source
        self.dst = destination
        self.log = []

    def incomplete(self, model, serial, version):
        temp = ''
        if not model:
            temp += 'model, '
        if not serial:
            temp += 'serial, '
        if not verison:
            temp += 'version'
        return temp  

    def writer(self):
        try:
            with os.scandir(self.src) as entries:
                for entry in entries:
                    path_name = '%s\\%s'%(self.src, entry.name)
                    # print(path_name)
                    f = FileReader(path_name)
                    f.readFile()
                    
                    hostname = f.requiredHostname()
                    interface_description = f.requiredInterfaceDescription()
                    required_file = f.isRequired(interface_description) # if '.*#show interface description' exist (interface_description is not an empty list), it is a required file
                    
                    if required_file:

                        model = f.requiredModel()
                        serial = f.requiredSerial()
                        version = f.requiredVersion()
                
                        interface_status = f.requiredInterfaceStatus()
                        
                        description = pd.DataFrame(interface_description)           # create dataframe
                        description_frame = DataFrameBuilder(description)           # dataframe object
                        description_frame.newHeader()                               # set first row to header/column name 

                        status = pd.DataFrame(interface_status)                     # create dataframe
                        status_frame = DataFrameBuilder(status)                     # dataframe object
                        status_frame.newHeader()                                    # set first row to header/column name

                        merge_frame = description_frame.mergeFrame(status_frame)    # merge description_dataframe and status_frame
                        merge_frame.insertColumn(hostname, model, serial, version)  # insert column and value 
                        merge_frame.deleteColumn()                                  # delete column and value            
                
                        excel = ExcelBuilder(merge_frame.df, hostname, self.dst)      # create object
                        excel.writeExcel()                                  # dataframe to excel file

                        if hostname == '' or model == '' or serial == '' or version == '':
                            self.log.append('%s Incomplete'%(hostname)) # if incomplete fill then append to log.txt
                    
        except IOError:
            print('cannot open ', self.src )
        
        try:
            with open("./log/log.txt", "w") as output:
                output.write('\n'.join(self.log))
        except IOError:
            print('log.txt Failed')
        else:
            print('log.txt Completed')

def main():
    try:
        # start = time.time()
        # source = 'C:\\Users\\jarun\\OneDrive\\Desktop\\Assignment\\All Configure'
        # destination = 'C:\\Users\\jarun\\OneDrive\\Desktop\\Assignment\\ExcelFile'
        excel = ExcelWriter(source, destination)
        excel.writer()
        # end = time.time()
    except NameError:
        print('NameError')
    else:
        # print('run time: %f s'%(end-start))
        pass
main()
