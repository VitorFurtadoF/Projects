#Deflate series


"""
Index	Source	Series_Code	Link/Code

2	CEIC	Fuel_Price_Ethanol	ID: 255784002 SR Code: SR4964096 (WEEKLY FREQUENCY)

6	CEIC	Agriculture_Price:Soybean	ID: 455427917 SR Code: SR143496007

14	CEIC	Nominal_Revenue_Tourism_Index	ID: 385720717 SR Code: SR105578867
15	CEIC	Retail_Trade_Index	ID: 385726277 SR Code: SR105535237

22	CEIC	Dollar_Rate	ID: 1326501 SR Code: SR4690985 (NEED TO DEFLATE BY BRAZIL AND US)

24	CEIC	Ibov	ID: 40774401 SR Code: SR4685374
25	CEIC	Savings_Deposits	ID: 455322477 SR Code: SR141339927
26	CEIC	Foreign_Trade_Balance	ID: 245232002 SR Code: SR4641526
27	CEIC	Foreign_Trade_Index	ID: 471295677 SR Code: SR153983837

29	FRED	Household_credit	https://fred.stlouisfed.org/series/QBRHAMUSDA#0

"""

#REGULAR DEFLATION USING MONTHLY CPI
#MONTHLY

import pandas as pd
from collections import defaultdict
import datetime
import os
from dateutil.relativedelta import relativedelta
import numpy as np

folder1 = os.getcwd()


#Get Monthly Deflator
df = pd.read_csv(folder1 + '/Spreadsheets/Monthly_Inflation.csv')
last_row = len(df.index)
monthly_deflator = defaultdict(float)
for i in range(0,last_row):
    monthly_deflator[df.iloc[i][0]] = df.iloc[i][1]   

#Get US Deflator
df = pd.read_csv(folder1 + '/Spreadsheets/Monthly_Inflation_US.csv')
last_row = len(df.index)
monthly_deflator_US = defaultdict(float)
for i in range(0,last_row):
    monthly_deflator_US[df.iloc[i][0]] = df.iloc[i][1]  

#Get Weekly Deflator
df = pd.read_csv(folder1 + '/Spreadsheets/Monthly_Inflation_weekly.csv')
last_row = len(df.index)
weekly_deflator = defaultdict(float)
for i in range(0,last_row):
    weekly_deflator[df.iloc[i][0]] = df.iloc[i][1]  

#Get Weekly US Deflator
df = pd.read_csv(folder1 + '/Spreadsheets/Monthly_Inflation_US_weekly.csv')
last_row = len(df.index)
weekly_deflator_US = defaultdict(float)
for i in range(0,last_row):
    weekly_deflator_US[df.iloc[i][0]] = df.iloc[i][1]  

#Define function for regular deflation
def USDeflation(df):
    last_row = len(df.index)
    last_column = len(df.columns)

    values = defaultdict(dict)
    for i in range(0,last_row):
        date = df.iloc[i]['date']
        year = int(df.iloc[i]['date'][0:4])
        month = int(df.iloc[i]['date'][5:7])
        date1 = str(year) + '-' + str(month).zfill(2) + '-01'

        if date1 in monthly_deflator_US.keys():
            monthly_deflator_US1 = float(monthly_deflator_US[date1]) / float(100)

        for j in range(1,last_column):
            if df.iloc[i][j] == 0:
                values[date][df.columns[j]] = np.nan
                continue
            try:
                values[date][df.columns[j]] = float(df.iloc[i][j]) / float(monthly_deflator_US1)
            except: 
                continue


    return pd.DataFrame(values).transpose()

def weeklyDeflation(df):
    last_row = len(df.index)
    last_column = len(df.columns)

    values = defaultdict(dict)
    for i in range(0,last_row):
        date = df.iloc[i]['date']
        year = int(df.iloc[i]['date'][0:4])
        month = int(df.iloc[i]['date'][5:7])
        day = int(df.iloc[i]['date'][8:10])
        date1 = str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)

        if date1 in weekly_deflator:
            weekly_deflator1 = float(weekly_deflator[date1]) / float(100)            

        for j in range(1,last_column):
            if df.iloc[i][j] == 0:
                values[date][df.columns[j]] = np.nan
                continue
            try:
                values[date][df.columns[j]] = float(df.iloc[i][j]) / float(weekly_deflator1)
            except: 
                continue


    return pd.DataFrame(values).transpose()


def monthlyDeflation(df):
    last_row = len(df.index)
    last_column = len(df.columns)

    values = defaultdict(dict)
    for i in range(0,last_row):
        date = df.iloc[i]['date']
        year = int(df.iloc[i]['date'][0:4])
        month = int(df.iloc[i]['date'][5:7])
        date1 = str(year) + '-' + str(month).zfill(2) + '-01'

        if date1 in weekly_deflator.keys():
            monthly_deflator1 = float(monthly_deflator[date1]) / float(100)

        for j in range(1,last_column):
            if df.iloc[i][j] == 0:
                values[date][df.columns[j]] = np.nan
                continue
            try:
                values[date][df.columns[j]] = float(df.iloc[i][j]) / float(monthly_deflator1)
            except: 
                continue


    return pd.DataFrame(values).transpose()


#Deflate as Usual
#2- Fuel_Price_Ethanol
df = pd.read_csv(folder1 + '/Spreadsheets/Fuel_Price_Ethanol.csv')
df_real = weeklyDeflation(df).reset_index()
df_real['index'] = pd.to_datetime(df_real['index'])
df_real = df_real.set_index('index')
df_real = df_real[df_real.index.weekday==5]
df_real.to_csv(folder1 + '/Spreadsheets/RealValues/Fuel_Price_Ethanol_RealValues.csv', index_label='date')

#6- Agriculture_Price:Soybean
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Agriculture_Price:Soybean_DA.csv')
weeklyDeflation(df).to_csv(folder1 + '/Spreadsheets/RealValues/Agriculture_Price:Soybean_DA_RealValues.csv', index_label='date')

#14	CEIC	Nominal_Revenue_Tourism_Index	ID: 385720717 SR Code: SR105578867
df = pd.read_csv(folder1 + '/Spreadsheets/Nominal_Revenue_Tourism_Index.csv')
monthlyDeflation(df).to_csv(folder1 + '/Spreadsheets/RealValues/Nominal_Revenue_Tourism_Index_RealValues.csv', index_label='date')

#15	CEIC	Retail_Trade_Index	ID: 385726277 SR Code: SR105535237
df = pd.read_csv(folder1 + '/Spreadsheets/Retail_Trade_Index.csv')
monthlyDeflation(df).to_csv(folder1 + '/Spreadsheets/RealValues/Retail_Trade_Index_RealValues.csv', index_label='date')

#24	CEIC	Ibov	ID: 40774401 SR Code: SR4685374
df = pd.read_csv(folder1 + '/Spreadsheets/DailyCollapse/Ibov_DailyCollapse.csv')
weeklyDeflation(df).to_csv(folder1 + '/Spreadsheets/RealValues/Ibov_DailyCollapse_RealValues.csv', index_label='date')

#25	CEIC	Savings_Deposits	ID: 455322477 SR Code: SR141339927
df = pd.read_csv(folder1 + '/Spreadsheets/DailyCollapse/Savings_Deposits_DailyCollapse.csv')
weeklyDeflation(df).to_csv(folder1 + '/Spreadsheets/RealValues/Savings_Deposits_DailyCollapse_RealValues.csv', index_label='date')

#26	CEIC	Foreign_Trade_Balance	ID: 245232002 SR Code: SR4641526
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Foreign_Trade_Balance_DA.csv')
USDeflation(df).to_csv(folder1 + '/Spreadsheets/RealValues/Foreign_Trade_Balance_DA_RealValues.csv', index_label='date')

#27	CEIC	Foreign_Trade_Index	ID: 471295677 SR Code: SR153983837
df = pd.read_csv(folder1 + '/Spreadsheets/Foreign_Trade_Index.csv')
USDeflation(df).to_csv(folder1 + '/Spreadsheets/RealValues/Foreign_Trade_Index_RealValues.csv', index_label='date')


#DEFLATION USING CPI FROM BRAZIL AND USA

def exchangeDeflation(df):
    last_row = len(df.index)
    last_column = len(df.columns)

    values = defaultdict(dict)
    for i in range(0,last_row):
        date = df.iloc[i]['date']
        year = int(df.iloc[i]['date'][0:4])
        month = int(df.iloc[i]['date'][5:7])
        day = int(df.iloc[i]['date'][8:10])
        date1 = str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)

        if date1 in monthly_deflator.keys():
            weekly_deflator1 = float(weekly_deflator[date1]) / float(100)
        if date1 in monthly_deflator_US.keys():
            weekly_deflator_US1 = float(weekly_deflator_US[date1]) / float(100)
            print

        for j in range(1,last_column):
            if df.iloc[i][j] == 0:
                values[date][df.columns[j]] = np.nan
                continue
            try:
                values[date][df.columns[j]] = (float(df.iloc[i][j]) * weekly_deflator_US1) / float(weekly_deflator1)
            except: 
                continue


    return pd.DataFrame(values).transpose()


#22	Dollar_Rate	
df_crude = pd.read_csv(folder1 + '/Spreadsheets/DailyCollapse/Dollar_Rate_DailyCollapse.csv')
df = exchangeDeflation(df_crude)
df1 = df[df.index >= '1999-01-01']
df1.to_csv(folder1 + '/Spreadsheets/RealValues/Dollar_Rate_DailyCollapse_RealValues.csv', index_label='date')

#Get REAL EXCHANGE RATE
#get quarterly
df = df.reset_index().rename(columns={'index': 'date'})
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df_quarterly = df.resample('QS').mean().reset_index()
df_quarterly['date'] = df_quarterly['date'].dt.strftime('%Y-%m-%d')
#df_quarterly.to_csv('test.csv')
last_row = len(df_quarterly.index)
real_exchange_rate = defaultdict(float)
for i in range(0,last_row):
    real_exchange_rate[df_quarterly.iloc[i][0]] = df_quarterly.iloc[i][1] 


def deflate_to_real(df):
    last_row = len(df.index)
    last_column = len(df.columns)

    values = defaultdict(dict)
    for i in range(0,last_row):
        date = df.iloc[i]['date']
        year = int(df.iloc[i]['date'][0:4])
        month = int(df.iloc[i]['date'][5:7])
        date1 = str(year) + '-' + str(month).zfill(2) + '-01'

        if date1 in real_exchange_rate.keys():
            real_exchange_rate1 = float(real_exchange_rate[date1]) / float(100)

        for j in range(1,last_column):
            if df.iloc[i][j] == 0:
                values[date][df.columns[j]] = np.nan
                continue
            try:
                values[date][df.columns[j]] = float(df.iloc[i][j]) * float(real_exchange_rate1)
            except: 
                continue


    return pd.DataFrame(values).transpose()


#22	29	FRED	Household_credit	https://fred.stlouisfed.org/series/QBRHAMUSDA#0
df = pd.read_csv(folder1 + '/Spreadsheets/Household_credit.csv')
deflate_to_real(df).to_csv(folder1 + '/Spreadsheets/RealValues/Household_credit_RealValues.csv', index_label='date') 