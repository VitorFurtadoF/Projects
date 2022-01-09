#Collapsing daily data into weekly frequency
#Selecting only dates starting in 1995

import os
import pandas as pd
import datetime
from datetime import timedelta
from collections import defaultdict
import calendar
import numpy as np

folder1 = os.getcwd()

df_base = pd.read_csv(folder1 + '/SeniorThesis_OutputBase_Sample.csv')
df = pd.read_csv(folder1 + '/Sample_data.csv')

#I will need to separate in two columns types: weekly/daily and monthly

#######
#Monthly frequency

df_monthly = df[['date','Monthly_CPI','Unemployment_Claims','Air_Traffic_(Domestic)','Soy_(Volume)','Automobile_Sales','Aluminium_Production(Volume)','Energy_Generation',
'Retail_Trade_Index'
]].set_index('date').dropna(how="all").reset_index()
values = defaultdict(dict)

#This function change the format of the date column
def change_dates(df1):
    #print(df1)
    last_row = len(df1.index)
    last_column = len(df1.columns)
    #print(last_row,last_column)

    for i in range(0,last_row):

        year = int(df1.iloc[i]['date'][0:4])
        month = int(df1.iloc[i]['date'][5:7])
        day = int(df1.iloc[i]['date'][8:10])

        date = datetime.datetime(year,month,day)
        #print(date)
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
            values[str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)][df1.columns[j]] = df1.iloc[i][j]            
        
    return pd.DataFrame(values).transpose()

df_monthly = change_dates(df_monthly).dropna(how='all')

########
#Weekly frequency
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

#Transform daily to weekly
df_weekly = df[['Ibov','Agriculture_Price:Soybean']]
df_weekly = df_weekly.resample('W').agg('mean')
df_weekly = df_weekly.reset_index()
df_weekly['date'] = df_weekly['date'] - timedelta(days=1)
df_weekly['date'] = df_weekly['date'].dt.strftime('%Y-%m-%d')
df_weekly = df_weekly.set_index('date').dropna(how='all')

########
#Merge both Monthly and Weekly
frames_x = [df_weekly,df_monthly]
df = pd.concat(frames_x, axis=1).sort_index()
df.index.name = 'date'
df = df.reset_index()
df['date'] = pd.to_datetime(df['date'])

#Only include data after 1995
df = df[df['date'] >= '1995-01-01']
df = df[df['date'] <= datetime.datetime.now()]

#For the analysis, I will take this line out. 

df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))

frames = [df_base,df]
result = pd.concat(frames)
result = result.set_index('date')

#Add data information to columns
year_li = [0,0,0,0]
quarter_li = [0,0,0,0]
month_li = [0,0,0,0]

for i in range(4,len(result.index)-1):
    if (result.index[i][5:7]) != (result.index[i+1][5:7]):
        if (result.index[i][5:7]) in ('03', '06', '09', '12'): 
            month_li.append(1)
            quarter_li.append(1)
            if(result.index[i][5:7]) in ('12'):
                year_li.append(1)
            else:
                year_li.append(0)
        else:
            month_li.append(1)
            quarter_li.append(0) 
            year_li.append(0)
    else: 
        month_li.append(0)
        quarter_li.append(0)
        year_li.append(0)


#append last indicators
last_date = datetime.datetime.strptime(result.iloc[len(result) - 1].name, "%Y-%m-%d")
last_date_plus_7 = last_date + datetime.timedelta(days=7) 
if last_date.year != last_date_plus_7.year:
    year_li.append(1)
else: 
    year_li.append(0)

if last_date.month != last_date_plus_7.month:
    month_li.append(1)
else: 
    month_li.append(0)

if ((last_date.month - 1) // 3) != ((last_date_plus_7.month - 1) // 3):
    quarter_li.append(1)
else: 
    quarter_li.append(0)

result.insert(0, 'year', year_li)
result.insert(1, 'quarter', quarter_li)
result.insert(2, 'month', month_li)

result.to_csv(folder1 + '/Sample_Data_Treated.csv')