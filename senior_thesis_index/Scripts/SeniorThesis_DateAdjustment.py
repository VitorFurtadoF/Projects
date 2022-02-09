#Adjust dates of monthly series

"""
Index	Source	Series_Code	Link/Code

3	CEIC	Air_Traffic_(Domestic)	ID: 292262901 SR Code: SR4338520
4	CEIC	Unemployment_Rate	ID: 475685597 SR Code: SR157483527
5	CEIC	Unemployment_Claims	ID: 458692687 SR Code: SR143241917
6	CEIC	Agriculture_Price:Soybean	ID: 455427917 SR Code: SR143496007
7	CEIC	Automobile_Sales	ID: 205388802 SR Code: SR4266819
8	CEIC	Manufacturing_Working_hours_index	ID: 356295407 SR Code: SR7300823
9	CEIC	Industrial_Capacity_Utilization_Index	ID: 283504504 SR Code: SR6658430
10	FRED	Industrial_Production_Index	https://fred.stlouisfed.org/series/BRAPROINDMISMEI#0
11	CEIC	Steel_Production	ID: 297371601 SR Code: SR4489914
12	CEIC	Petroleum_Product_Sales	ID: 229230402 SR Code: SR4326341
13	CEIC	Energy_Generation	ID: 365246102 SR Code: SR6741274
14	CEIC	Nominal_Revenue_Tourism_Index	ID: 385720717 SR Code: SR105578867
15	CEIC	Retail_Trade_Index	ID: 385726277 SR Code: SR105535237
16	FRED	Investment_goods_manufact	https://fred.stlouisfed.org/series/PRMNVG01BRQ661S
17	CEIC	Real_GDP_SA	ID: 366988057 SR Code: SR88309317
18	FRED	Tendancy_manufact_exports	https://fred.stlouisfed.org/series/BSXRLV02BRM086S
19	FRED	Tendancy_manufact_production	https://fred.stlouisfed.org/series/BSPRFT02BRM460S
20	FRED	Tendancy_employment	https://fred.stlouisfed.org/series/BSEMFT02BRM460S
21	FRED	Uncretainty_Index	https://fred.stlouisfed.org/series/WUIBRA

23	IPEA DATA	3_months_bond_yield	Taxa de juros pré fixada - estrutura a termo - LTN - 3 meses

26	CEIC	Foreign_Trade_Balance	ID: 245232002 SR Code: SR4641526
27	CEIC	Foreign_Trade_Index	ID: 234305103 SR Code: SR4270471
28	CEIC	Average_Real_Income	ID: 376266557 SR Code: SR98321397
29	FRED	Household_credit	https://fred.stlouisfed.org/series/QBRHAMUSDA#0
30	FRED	Residential_prices	https://fred.stlouisfed.org/series/QBRR368BIS

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

def change_dates(df):

    last_row = len(df.index)
    last_column = len(df.columns)
    values.clear()

    for i in range(0,last_row):

        year = int(df.iloc[i]['date'][0:4])
        month = int(df.iloc[i]['date'][5:7])
        if (calendar.isleap(year)):
            day = LAST_DATE_IF_LEAP[month]
        else:    
            day = LAST_DATE[month]

        date = datetime.datetime(year,month,day)
        if (date.weekday() != 5):
            for k in range(1, 7):
                new_date = date + datetime.timedelta(days=-k)
                if(new_date.weekday() == 5):
                    date = new_date
                    break 

        year = date.year
        month = date.month
        day = date.day

        for j in range (1,last_column):
            if df.iloc[i][j] == 0.0:
                values[str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)][df.columns[j]] = np.nan
            else: 
                values[str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)][df.columns[j]] = df.iloc[i][j]            
        
    return pd.DataFrame(values).transpose()

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

def change_dates_special(df):

    last_row = len(df.index)
    last_column = len(df.columns)
    values.clear()

    for i in range(0,last_row):

        year = int(df.iloc[i]['date'][0:4])
        month = int(df.iloc[i]['date'][5:7])

        month = month + 2

        if (calendar.isleap(year)):
            day = LAST_DATE_IF_LEAP[month]
        else:    
            day = LAST_DATE[month]

        date = datetime.datetime(year,month,day)
        
        if (date.weekday() != 5):
            for k in range(1, 7):
                new_date = date + datetime.timedelta(days=-k)
                if(new_date.weekday() == 5):
                    date = new_date
                    break 

        year = date.year
        month = date.month
        day = date.day

        for j in range (1,last_column):    
            values[str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)][df.columns[j]] = df.iloc[i][j]            
        
    return pd.DataFrame(values).transpose()

##3	Air_Traffic_(Domestic)_SA
#df1 = pd.read_csv('Spreadsheets/SeasonalAdjustment/Air_Traffic_(Domestic)_SA.csv')
#change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Air_Traffic_(Domestic)_SA_DA.csv',  index_label='date')
#4	Unemployment_Rate	
df1 = pd.read_csv('Spreadsheets/SeasonalAdjustment/Unemployment_Rate_SA.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Unemployment_Rate_SA_DA.csv',  index_label='date')
#5	Unemployment_Claims_SA
df1 = pd.read_csv('Spreadsheets/SeasonalAdjustment/Unemployment_Claims_SA.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Unemployment_Claims_SA_DA.csv',  index_label='date')
#7	Automobile_Sales_SA
df1 = pd.read_csv('Spreadsheets/Automobile_Sales.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Automobile_Sales_DA.csv',  index_label='date')
#8	Manufacturing_Working_hours_index	
df1 = pd.read_csv('Spreadsheets/Manufacturing_Working_hours_index.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Manufacturing_Working_hours_index_DA.csv',  index_label='date')
#9	Industrial_Capacity_Utilization_Index	
df1 = pd.read_csv('Spreadsheets/Industrial_Capacity_Utilization_Index.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Industrial_Capacity_Utilization_Index_DA.csv',  index_label='date')
#10	Industrial_Production_Index	
df1 = pd.read_csv('Spreadsheets/Industrial_Production_Index.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Industrial_Production_Index_DA.csv',  index_label='date')
#11	Steel_Production
df1 = pd.read_csv('Spreadsheets/Steel_Production.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Steel_Production_DA.csv',  index_label='date')
#12	Petroleum_Product_Sales	
df1 = pd.read_csv('Spreadsheets/Petroleum_Product_Sales.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Petroleum_Product_Sales_DA.csv',  index_label='date')
#13	Energy_Generation	
df1 = pd.read_csv('Spreadsheets/Energy_Generation.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Energy_Generation_DA.csv',  index_label='date')
#14	Nominal_Revenue_Tourism_Index	
df1 = pd.read_csv('Spreadsheets/RealValues/Nominal_Revenue_Tourism_Index_RealValues.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Nominal_Revenue_Tourism_Index_RealValues_DA.csv',  index_label='date')
#15	Retail_Trade_Index	
df1 = pd.read_csv('Spreadsheets/RealValues/Retail_Trade_Index_RealValues.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Retail_Trade_Index_RealValues_DA.csv',  index_label='date')
##16	Investment_goods_manufact	
#df1 = pd.read_csv('Spreadsheets/Investment_goods_manufact.csv')
#change_dates_special(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Investment_goods_manufact_DA.csv',  index_label='date')
#17	Real_GDP_SA	
df1 = pd.read_csv('Spreadsheets/Real_GDP_SA.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Real_GDP_SA_DA.csv',  index_label='date')
#18	Tendancy_manufact_exports
df1 = pd.read_csv('Spreadsheets/Tendancy_manufact_exports.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Tendancy_manufact_exports_DA.csv',  index_label='date')
#19	Tendancy_manufact_production
df1 = pd.read_csv('Spreadsheets/Tendancy_manufact_production.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Tendancy_manufact_production_DA.csv',  index_label='date')
#20	Tendancy_employment
df1 = pd.read_csv('Spreadsheets/Tendancy_employment.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Tendancy_employment_DA.csv',  index_label='date')
#21	Uncertainty_Index	
df1 = pd.read_csv('Spreadsheets/Uncertainty_Index.csv')
change_dates_special(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Uncertainty_Index_DA.csv',  index_label='date')
#23 3_months_bond_yield	
df1 = pd.read_csv('Spreadsheets/3_months_bond_yield.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/3_months_bond_yield_DA.csv',  index_label='date')
#27	Foreign_Trade_Index	
df1 = pd.read_csv('Spreadsheets/RealValues/Foreign_Trade_Index_RealValues.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Foreign_Trade_Index_RealValues_DA.csv',  index_label='date')
#28	Average_Real_Income	
df1 = pd.read_csv('Spreadsheets/Average_Real_Income.csv')
change_dates(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Average_Real_Income_DA.csv',  index_label='date')
#29	Household_credit	
df1 = pd.read_csv('Spreadsheets/RealValues/Household_credit_RealValues.csv')
change_dates_special(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Household_credit_RealValues_DA.csv',  index_label='date')
#30	Residential_prices	
df1 = pd.read_csv('Spreadsheets/Residential_prices.csv')
change_dates_special(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Residential_prices_DA.csv',  index_label='date')

"""
#26- Foreign_Trade_Balance
df1 = pd.read_csv('Spreadsheets/RealValues/Foreign_Trade_Balance_RealValues.csv')
change_dates_fridays(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Foreign_Trade_Balance_RealValues_DA.csv',  index_label='date')
#6- Agriculture_Price:Soybean
df1 = pd.read_csv('Spreadsheets/RealValues/Agriculture_Price:Soybean_RealValues.csv')
change_dates_fridays(df1).to_csv(folder1 + '/Spreadsheets/DateAdjustment/Agriculture_Price:Soybean_RealValues_DA.csv',  index_label='date')
"""