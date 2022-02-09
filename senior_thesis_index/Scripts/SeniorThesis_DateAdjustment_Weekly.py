#Adjust dates of monthly series

"""
Index	Source	Series_Code	Link/Code

6	CEIC	Agriculture_Price:Soybean	ID: 455427917 SR Code: SR143496007

26	CEIC	Foreign_Trade_Balance	ID: 245232002 SR Code: SR4641526
"""

import pandas as pd
import datetime 
import calendar
import os
from collections import defaultdict
from dateutil.relativedelta import relativedelta
import numpy as np

LAST_DATE_IF_LEAP = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
LAST_DATE = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} 

folder1 = os.getcwd()
values = defaultdict(dict)

def change_dates_fridays(df):

    last_row = len(df.index)
    last_column = len(df.columns)
    values.clear()

    for i in range(0,last_row):

        
        year = int(df.iloc[i]['date'][0:4])
        month = int(df.iloc[i]['date'][5:7])
        day = int(df.iloc[i]['date'][8:10])
        date = datetime.datetime(year,month,day)

        k = 5 - date.weekday()
        
        date = date + relativedelta(days=k)

        year = date.year
        month = date.month
        day = date.day

        for j in range (1,last_column):    
            values[str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)][df.columns[j]] = df.iloc[i][j]            
        
    return pd.DataFrame(values).transpose()


#26- Foreign_Trade_Balance
df1 = pd.read_csv('Spreadsheets/Foreign_Trade_Balance.csv')
change_dates_fridays(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Foreign_Trade_Balance_DA.csv',  index_label='date')

#6- Agriculture_Price:Soybean
df1 = pd.read_csv('Spreadsheets/Agriculture_Price:Soybean.csv')
change_dates_fridays(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Agriculture_Price:Soybean_DA.csv',  index_label='date')