import pandas as pd

class DataFrameBuilder:

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.columns = []

    def __add__(self, inp):
        if not (self.dataframe.empty or inp.dataframe.empty):
            self.dataframe = self.dataframe.merge(inp.dataframe, how = 'left', on=0)
        return DataFrameBuilder(self.dataframe)

    def dropColumn(self, cols):
        self.dataframe.drop(columns = cols, inplace = True)
    
    def addColumn(self, cols):
        self.dataframe.columns = cols
    
    def insertColumn(self, col_index, col_name, value):
        self.dataframe.insert(col_index, col_name, value)

   
