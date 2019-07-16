import pandas as pd

class DataFrameWriter:
    def __init__(self, ls):
        self.ls = ls
        self.df = ''
    
    def listToDataFrame(self):
        self.df = pd.DataFrame(self.ls)

    def newHeader(self):
        if not self.df.empty:
            new_header = self.df.iloc[0]
            self.df = self.df[1:] 
            self.df.columns = new_header
            return self.df
