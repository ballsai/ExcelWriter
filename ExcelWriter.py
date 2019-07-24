import os
import re
import pandas as pd 
from tabulate import tabulate

from FileReader import FileReader
from DataFrameBuilder import DataFrameBuilder
from ExcelBuilder import ExcelBuilder

def main():
    log = []
    directory = '../All Configure/'
    except_file = 'THCBSLSUIN08,no-ip,console,4_log,.txt'

    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.name == except_file:
                    continue

                f = FileReader(directory + entry.name)
                f.readFile()

                hostname = f.requiredHostname()
                model = f.requiredModel()
                serial = f.requiredSerial()
                version = f.requiredVersion()

                interface_description = f.requiredInterfaceDescription()
                interface_status = f.requiredInterfaceStatus()

                required_file = f.isRequired(interface_description) # if '.*#show interface description' exist (interface_description is not an empty list), it is a required file

                if required_file:

                    description = pd.DataFrame(interface_description)   # create dataframe
                    description_frame = DataFrameBuilder(description)   # dataframe object
                    description_frame.newHeader()                       # set first row to header/column name 

                    status = pd.DataFrame(interface_status)             # create dataframe
                    status_frame = DataFrameBuilder(status)             # dataframe object
                    status_frame.newHeader()                            # set first row to header/column name

                    merge_frame = description_frame + status_frame      # merge description_dataframe and status_frame
                    merge_frame.insertColumn(hostname, model, serial, version)
                   
                    # print(tabulate(merge_frame.df, headers='keys', tablefmt='psql'))  # display table

                    excel = ExcelBuilder(merge_frame.df, hostname)      # create object
                    excel.writeExcel()                                  # dataframe to excel file

                    # log.append(hostname+' : '+version)
            
    except IOError:
        print('cannot open directory name ',directory )
    
    try:
        with open("./Log/log.txt", "w") as output:
            output.write('\n'.join(log))
    except IOError:
        print('cannot write file name log.txt')

main()        