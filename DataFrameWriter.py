import pandas as pd

class DataFrameWriter:
    def __init__(self, _list):
        self._list = _list
        self.df = ''
        self.empty_df = []
    
    def getDataFrame(self):
        self.df = pd.DataFrame(self._list)

    def concatDataFrame(self, df_x):
        self.df = pd.concat([self.df, df_x], axis = 1)

    def mergeDataFrame(self, data):
        if (not self.df.empty) and (not data.df.empty) :
            self.df = self.df.merge(data.df, on = 0)
    
    def isEmptyDataFrame(self, f):
        if self.df.empty:
            self.empty_df.append(f.path)
        
    def newHeader(self):
        if not self.df.empty:
            new_header = self.df.iloc[0]
            self.df = self.df[1:] 
            self.df.columns = new_header
            return self.df