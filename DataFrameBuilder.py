import pandas as pd

class DataFrameBuilder():

    def __init__(self, df):            # df = dataframe
        self.df = df

    def __add__(self, inp):             # merge dataframe by + operator, inp = input
        side = ''
        try: 
            # if not (self.df.empty or inp.df.empty):
            if len(self.df.index) > len(inp.df.index):
                side = 'left'
            else: 
                side = 'right'
            self.df = self.df.merge(inp.df, how = side, left_on='Interface', right_on='Port')
        except:
            print('cannot merge two dataframes')
        else:
            print('can merge two dataframes')        
        
        return DataFrameBuilder(self.df)

    def newHeader(self):
        try:
        # if not self.df.empty:               
            new_header = self.df.iloc[0]    # shift first row up
            self.df = self.df[1:]
            self.df.columns = new_header
        except:
            print('cannot shift first row up')     
   
    def insertColumn(self, hostname, model, serial, version):
        # insert column with value only one row
        factor = ['']*(len(self.df)-1)
        self.df.insert( 0,'SW Version', [version]+factor)
        self.df.insert( 0,'Serial No.', [serial]+factor)
        self.df.insert( 0,'Model', [model]+factor)
        self.df.insert( 0,'Hostname', [hostname]+factor)

