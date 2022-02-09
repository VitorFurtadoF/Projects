#Seasonal Adjustment 

"""
Index	Source	Series_Code	Link/Code

2	CEIC	Fuel_Price_Ethanol ID: 255784002 SR Code: SR4964096 (WEEKLY FREQUENCY)

4	CEIC	Unemployment_Rate	ID: 475685597 SR Code: SR157483527
5	CEIC	Unemployment_Claims	ID: 458692687 SR Code: SR143241917

7	CEIC	Automobile_Sales	ID: 205388802 SR Code: SR4266819

12	CEIC	Petroleum_Product_Sales	ID: 229230402 SR Code: SR4326341
13	CEIC	Energy_Generation	ID: 365246102 SR Code: SR6741274

27	CEIC	Foreign_Trade_Index	ID: 234305103 SR Code: SR4270471
28	CEIC	Average_Real_Income	ID: 376266557 SR Code: SR98321397
"""

def add_columns(df_path, df1_path):
    df = pd.read_csv(df_path)
    df = df[df['date'] >= '1986-03-01']
    df = df.reset_index()

    del df['index']

    col_names = df.columns.tolist()
    col_names.pop(0)

    df1 = pd.read_csv(df1_path, names=col_names, header=None)
    df1.insert(0, 'date', df['date']) 

    df1 = df1.fillna('NaN')
    df1.to_csv(df1_path, index=False)   

#MONTHLY
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os
import sys

folder1 = os.getcwd()
os.environ["PATH"] += os.pathsep + folder1 + '/Weekly_Seasonal_Adjustment/x13asall_V1.1_B39/x13as/'


def seasonal_adjustment(df):
    df = df[df['date'] >= '1996-01-01']
    df["date"] = df["date"].str.replace("-31", "")
    df["date"] = df["date"].str.replace("-30", "")
    df["date"] = df["date"].str.replace("-29", "")
    df["date"] = df["date"].str.replace("-28", "")
    df["date"] = df["date"].str.replace("-27", "")
    df["date"] = df["date"].str.replace("-26", "")
    df["date"] = df["date"].str.replace("-25", "")
    df["date"] = df["date"].str.replace("-24", "")
    df["date"] = df["date"].str.replace("-23", "")
    df["date"] = df["date"].str.replace("-22", "")
    df["date"] = df["date"].str.replace("-21", "")
    df['date'] = pd.to_datetime(df['date'])


    df4 = pd.DataFrame(index=df['date'])

    df0 = df[['date', 'Brazil']]
    df0 = df0.set_index('date')
    df1 = df0.dropna()

    res = pd.DataFrame(sm.tsa.x13_arima_analysis(df1).seasadj)
    df4['Brazil'] = res['seasadj']

    return df4


"""
#3- Air_Traffic_(Domestic)
df = pd.read_csv(folder1 + '/Spreadsheets/Air_Traffic_(Domestic).csv')
seasonal_adjustment(df).to_csv(folder1 + '/Spreadsheets/SeasonalAdjustment/Air_Traffic_(Domestic)_SA.csv', index_label='date')
"""
#5- Unemployment_Rate
df = pd.read_csv(folder1 + '/Spreadsheets/Unemployment_Rate.csv')
seasonal_adjustment(df).to_csv(folder1 + '/Spreadsheets/SeasonalAdjustment/Unemployment_Rate_SA.csv', index_label='date')

#5- Unemployment_Claims
df = pd.read_csv(folder1 + '/Spreadsheets/Unemployment_Claims.csv')
seasonal_adjustment(df).to_csv(folder1 + '/Spreadsheets/SeasonalAdjustment/Unemployment_Claims_SA.csv', index_label='date')
"""
#7- Automobile_Sales
df = pd.read_csv(folder1 + '/Spreadsheets/Automobile_Sales.csv')
seasonal_adjustment(df).to_csv(folder1 + '/Spreadsheets/SeasonalAdjustment/Automobile_Sales_SA.csv', index_label='date')
"""

#12- Petroleum_Product_Sales
df = pd.read_csv(folder1 + '/Spreadsheets/Petroleum_Product_Sales.csv')
seasonal_adjustment(df).to_csv(folder1 + '/Spreadsheets/SeasonalAdjustment/Petroleum_Product_Sales_SA.csv', index_label='date')

"""
#13- Energy_Generation
df = pd.read_csv(folder1 + '/Spreadsheets/Energy_Generation.csv')
seasonal_adjustment(df).to_csv(folder1 + '/Spreadsheets/SeasonalAdjustment/Energy_Generation_SA.csv', index_label='date')

#27- Foreign_Trade_Index
df = pd.read_csv(folder1 + '/Spreadsheets/Foreign_Trade_Index.csv')
seasonal_adjustment(df).to_csv(folder1 + '/Spreadsheets/SeasonalAdjustment/Foreign_Trade_Index_SA.csv', index_label='date')

#28- Average_Real_Income
df = pd.read_csv(folder1 + '/Spreadsheets/Average_Real_Income.csv')
seasonal_adjustment(df).to_csv(folder1 + '/Spreadsheets/SeasonalAdjustment/Average_Real_Income_SA.csv', index_label='date')
"""