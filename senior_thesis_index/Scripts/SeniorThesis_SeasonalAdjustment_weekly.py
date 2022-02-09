#Seasonal Adjustment 

"""
2	CEIC	Fuel_Price_Ethanol	ID: 255784002 SR Code: SR4964096
"""

STATES_CODES = ['Brazil']

def add_columns(df_path, df1_path):
    df = pd.read_csv(df_path)
    df = df[df['date'] >= '1996-01-01']
    df = df.reset_index()

    del df['index']

    col_names = df.columns.tolist()
    col_names.pop(0)

    df1 = pd.read_csv(df1_path, names=col_names, header=None)
    df1.insert(0, 'date', df['date']) 
    df1 = df1.fillna('NaN')
    df1.to_csv(folder1 + '/Spreadsheets/SeasonalAdjustment/Fuel_Price_Ethanol_RealValues_SA.csv', index=False)   




#WEEKLY 

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os
import sys

folder1 = os.getcwd()


sys.path.append("/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/matlab")
import matlab.engine


os.chdir(os.getcwd())

#2- Fuel_Price_Ethanol
#print('initial


result = pd.read_csv(folder1 + '/Spreadsheets/RealValues/Fuel_Price_Ethanol_RealValues.csv')
result.to_csv(folder1 + '/Weekly_Seasonal_Adjustment/Spreadsheets/RealValues/Fuel_Price_Ethanol_RealValues_T.csv', index = False)

#Seasonal Adjustment

os.chdir(folder1 + '/Scripts/' )

eng = matlab.engine.start_matlab()
eng.Weekly_Adjustment(nargout=0)

os.remove(folder1 + r'Weekly_Seasonal_Adjustment/Spreadsheets/RealValues/Fuel_Price_Ethanol_RealValues_T.csv')
print('-----------------')


#NEED TO ADD ARIZONA AND COLUMNS

add_columns(folder1 + '/Spreadsheets/RealValues/Fuel_Price_Ethanol_RealValues.csv', folder1 + '/Weekly_Seasonal_Adjustment/Fuel_Price_Ethanol_RealValues_SA.csv')
