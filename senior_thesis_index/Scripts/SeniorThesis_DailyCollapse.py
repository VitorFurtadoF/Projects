#Convert daily to weekly

"""
Index	Source	Series_Code	Link/Code
1	Apple	Apple_Mobility_Index	https://www.apple.com/covid19/mobility
22	CEIC	Dollar_Rate	ID: 1326501 SR Code: SR4690985

23	IPEA DATA	3_months_bond_yield	Taxa de juros pré fixada - estrutura a termo - LTN - 3 meses



24	CEIC	Ibov	ID: 40774401 SR Code: SR4685374
25	CEIC	Savings_Deposits	ID: 455322477 SR Code: SR141339927

"""

import pandas as pd
from collections import defaultdict
import datetime
import os
import numpy
from datetime import timedelta

folder1 = os.getcwd()


def daily_collapse(df):
          
    last_row = len(df.index)
    last_column = len(df.columns)

    values = defaultdict(dict) 
    dates = defaultdict(int)
    df_test = pd.isnull(df)

    for j in range(1,last_column):
        
        state = df.columns[j]

        value = 0
        x = 0

        for i in range(0,last_row):
            year = int(df.iloc[i][0][0:4])
            month = int(df.iloc[i][0][5:7])
            day = int(df.iloc[i][0][8:])

            if (df_test.iloc[i][j] == True):
                dates[str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)] = 1
            else:            
                x = x + 1
                value = float(value) + float(df.iloc[i][j])
            
            if (datetime.datetime(year, month, day).weekday() == 5):
                #thursday = datetime.datetime(year,month,day)
                #saturday = thursday + datetime.timedelta(days=2) 
                #year_saturday = saturday.year
                #month_saturday = saturday.month
                #day_saturday = saturday.day
                if (x != 0):  
                    values[str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)][state] = value/float(x)
                value = 0
                x = 0

    if (len(dates) != 0):
        print('It has some missing dates:')
        for x in dates: 
            print(x)

    return pd.DataFrame(values).transpose()

def daily_collapse_modified(df_weekly):

    df_weekly['date'] = pd.to_datetime(df_weekly['date'])
    df_weekly = df_weekly.set_index('date')
    df_weekly = df_weekly[df_weekly['Brazil'] != 0.0]
    df_weekly = df_weekly.resample('W').agg('mean')
    df_weekly = df_weekly.reset_index()


    df_weekly['date'] = df_weekly['date'] - timedelta(days=1)
    df_weekly['date'] = df_weekly['date'].dt.strftime('%Y-%m-%d')
    df_weekly = df_weekly.set_index('date').dropna(how='all')

    return df_weekly

#1- Apple_Mobility_Index
print("#Apple_Mobility_Index")
df = pd.read_csv('Spreadsheets/Apple_Mobility_Index.csv')
daily_collapse(df).to_csv(folder1 + '/Spreadsheets/DailyCollapse/Apple_Movility_Index_DailyCollapse.csv', index_label='date')

#22	Dollar_Rate
print("#Dollar_Rate")
df = pd.read_csv('Spreadsheets/Dollar_Rate.csv')
daily_collapse_modified(df).to_csv(folder1 + '/Spreadsheets/DailyCollapse/Dollar_Rate_DailyCollapse.csv', index_label='date')

#24	Ibov
print("#Ibov")
df = pd.read_csv('Spreadsheets/Ibov.csv')
daily_collapse_modified(df).to_csv(folder1 + '/Spreadsheets/DailyCollapse/Ibov_DailyCollapse.csv', index_label='date')

#25	Savings_Deposits
print("#Savings_Deposits")
df = pd.read_csv('Spreadsheets/Savings_Deposits.csv')
daily_collapse_modified(df).to_csv(folder1 + '/Spreadsheets/DailyCollapse/Savings_Deposits_DailyCollapse.csv', index_label='date')