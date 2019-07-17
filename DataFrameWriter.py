import pandas as pd

class DataFrameWriter:
    def __init__(self, ls):
        self.ls = ls
        self.df = ''
        self.empty_df = []
    
    def listToDataFrame(self):
        self.df = pd.DataFrame(self.ls)
    
    def transposeDataFrame(self):
        self.df = self.df.T

    def concatDataFrame(self, df_x):
        self.df = pd.concat([self.df, df_x], axis = 1)

    def mergeDataFrame(self, df_x):
        if (not self.df.empty) and (not df_x.empty) and ('Port' in df_x.columns):
            self.df = self.df.merge(df_x, left_on = 'Interface', right_on = 'Port' )
    
    def isEmptyDataFrame(self, f):
        if self.df.empty:
            self.empty_df.append(f.path)
        
    def newHeader(self):
        if not self.df.empty:
            new_header = self.df.iloc[0]
            self.df = self.df[1:] 
            self.df.columns = new_header
            return self.df