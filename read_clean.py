import os
import pandas as pd
import numpy as np
import datetime 
from calendar import monthrange 
import calendar
pd.options.mode.chained_assignment = None

#Function that helps identify the month

def consider_first(d1: datetime.date, d2: datetime.date) -> bool:   
    number_of_days = monthrange(d1.year, d1.month)[1]
    return number_of_days - d1.day + 1 > d2.day

#Initializing the class that reads and renames file, appending them into a dataframe

class FileClean:
    
    def __init__(self, year):
        self.year = str(year)
        self.frames = []
        self.master_df = pd.DataFrame()
    #Function to rename files
    
    def rename_files(self):
        for file in os.listdir(f'import/{self.year}'):
            df = pd.read_excel(f'import/{self.year}/{file}', engine='openpyxl')
            new_filename = df['Unnamed: 0'][2].split(':')[2].split('\n')[0].strip()
            if new_filename != file:
                os.rename(f"import/{self.year}/{file}", f"import/{self.year}/{new_filename}.xlsx")
            else:
                continue
    
    #Function for determining the month based on the week
    
        
    #Converting the excel files into dataframes
    def clean_export(self):
        self.rename_files()
        master_df = pd.DataFrame()
        #Storing each sheet into a different dataframe while performing:
        #1. Basic Cleaning
        #2. Adding a week start column to correspond to the week each book's info was collected in
        #3. Adding a month column to correspond to the month (will be needed in time series analysis)
        #4. Adding a week number column
        
        for file in os.listdir(f'import/{self.year}'):
            df = pd.read_excel(f'import/{self.year}/{file}', engine = 'openpyxl')
            week_start = df['Unnamed: 0'][2].split(':')[2].split('\n')[0].split('-')[0].strip()
            week_end = df['Unnamed: 0'][2].split(':')[2].split('\n')[0].split('-')[1].strip()
            df = pd.read_excel(f'import/{self.year}/{file}', engine = 'openpyxl', skiprows=8, skipfooter=2)
            df.dropna(axis=1, inplace=True)
            df.rename(columns = lambda x:x.strip(), inplace=True)
            week_start = datetime.datetime.strptime(week_start, "%b %d %Y")
            week_end = datetime.datetime.strptime(week_end, "%b %d %Y")
            df['Week Start'] = week_start
            df['Week End'] = week_end
            if week_start.month != week_end.month:
                _consider_first = consider_first(week_start, week_end)
                if _consider_first:
                    df['Month'] = df['Week Start'].dt.month
                else:
                    df['Month'] = df['Week End'].dt.month
            else: 
                df['Month'] = df['Week Start'].dt.month 
            
            df.drop(['LW Rank', '#Weeks on List', 'YTD Sales'], axis=1, inplace=True)
            self.frames.append(df)
            
        self.master_df = pd.concat(self.frames)
        self.master_df.sort_values(['Week Start', 'TW Rank'], inplace=True)
        k=1 
        c=0
        last_row = None
        self.master_df['Week No.'] = np.nan
        for idx, row in self.master_df.iterrows():
            if last_row is not None:
                if row['Week Start'] == last_row['Week Start']:
                    self.master_df['Week No.'].iloc[c] = k
                else:
                    k+=1
                    self.master_df['Week No.'].iloc[c] = k
            else:
                self.master_df['Week No.'].iloc[c] = k
            last_row=row 
            c+=1
        return self.master_df
    
    
    
