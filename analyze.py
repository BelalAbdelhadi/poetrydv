import numpy as np
import pandas as pd
import datetime
import re
pd.options.mode.chained_assignment = None

class Analyzer:
    
    def __init__(self, dataframe, year):
        self.dataframe = dataframe 
        self.year = year
        
    def group(self, grouper):
        grouped_df = self.dataframe.groupby(grouper).sum()
        if grouper != 'Month' and grouper != 'Week Start':
            grouped_df.sort_values('TW Sales', inplace = True, ascending=False)
        grouped_df = grouped_df.filter(items=['TW Sales'])
        grouped_df.rename(columns = {'TW Sales': 'Total Sales'}, inplace=True)
        return grouped_df
    
    def top(self, grouper, rank):
        df = self.group(grouper)
        top_df = df.iloc[0:rank]
        return top_df
    
    def market_share(self, grouper, rank):
        df = self.group(grouper)
        df.filter(items = ['Total Sales'])
        shares_df = self.top(grouper, rank)
        rest = sum(df['Total Sales'].iloc[rank:-1])
        others = pd.Series(rest, index=['Others'])
        shares_df[str(grouper)] = shares_df.index
        shares_df = shares_df.append(others, ignore_index=True)
        shares_df['Total Sales'].iloc[rank] = rest
        shares_df[str(grouper)].iloc[rank] = 'Others'
        shares_df.drop(['Others'], axis=1, inplace=True)
        shares_df['Total Sales'] = shares_df['Total Sales'].astype(int)
        return shares_df
    
    @classmethod
    def export(cls, df, name):
        year = re.findall('\d{4}', name)[0]
        df.to_csv(r'export/{}/{}'.format(year, name))
        