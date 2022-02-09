#BRAZILIAN DATASET
#Output

#####TUESDAYS#####
#Note: I am deleting the last row compared to the script "_saturday" because the daily series with entries 
#from Sunday to Tuesday are being collapsed to the next Saturday.

"""
Index	Source	Series_Code	Link/Code
1	Apple	Apple_Mobility_Index	/Spreadsheets/DailyCollapse/Apple_Movility_Index_DailyCollapse.csv
2	CEIC	Fuel_Price_Ethanol	ID: 255784002 SR Code: SR4964096
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
21	FRED	Uncertainty_Index	https://fred.stlouisfed.org/series/WUIBRA
22	CEIC	Dollar_Rate	ID: 1326501 SR Code: SR4690985
23	IPEA DATA	3_months_bond_yield	Taxa de juros pré fixada - estrutura a termo - LTN - 3 meses
24	CEIC	Ibov	ID: 40774401 SR Code: SR4685374
25	CEIC	Savings_Deposits	ID: 455322477 SR Code: SR141339927
26	CEIC	Foreign_Trade_Balance	ID: 245232002 SR Code: SR4641526
27	CEIC	Foreign_Trade_Index	ID: 234305103 SR Code: SR4270471
28	CEIC	Average_Real_Income	ID: 376266557 SR Code: SR98321397
29	FRED	Household_credit	https://fred.stlouisfed.org/series/QBRHAMUSDA#0
30	FRED	Residential_prices	https://fred.stlouisfed.org/series/QBRR368BIS
-   CEIC    Monthly_Inflation	ID: 273491403 SR Code: SR5814771
-   CEIC    Monthly_Inflation_US FRED https://fred.stlouisfed.org/series/CPIAUCSL  
"""

#from Scripts.DashboardProject_OutputByState import STATES_CODES, STATES_REGION
import pandas as pd
import numpy as np
from collections import defaultdict
from datetime import date
import sys
import os

folder1 = os.getcwd()

values = defaultdict(dict)
state = 'Brazil'
STATES_CODES = {'Brazil': 'Brazil'}
STATES_REGION = {'Brazil': 'Brazil'}    

df2 = pd.read_csv("Auxiliar/SeniorThesis_MainOutput_Base.csv").set_index('date')

#1- Apple_Mobility_Index
df = pd.read_csv(folder1 + '/Spreadsheets/DailyCollapse/Apple_Movility_Index_DailyCollapse.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Apple_Mobility_Index'] = df[state][ind]   
#2- Fuel_Price_Ethanol
df = pd.read_csv(folder1 + '/Spreadsheets/RealValues/Fuel_Price_Ethanol_RealValues.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Fuel_Price_Ethanol'] = df[state][ind]   
##3- Air_Traffic_(Domestic)
#df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Air_Traffic_(Domestic)_SA_DA.csv')
#for ind in df.index:
#    values[df[df.columns[0]][ind]]['Air_Traffic_(Domestic)'] = df[STATES_CODES[state]][ind]  
#4- Unemployment_Rate
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Unemployment_Rate_SA_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Unemployment_Rate'] = df[STATES_CODES[state]][ind]  
#5- Unemployment_Claims
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Unemployment_Claims_SA_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Unemployment_Claims'] = df[STATES_CODES[state]][ind] 
#6- Agriculture_Price:Soybean
df = pd.read_csv(folder1 + '/Spreadsheets/RealValues/Agriculture_Price:Soybean_DA_RealValues.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Agriculture_Price:Soybean'] = df[state][ind]  
#7- Automobile_Sales
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Automobile_Sales_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Automobile_Sales'] = df[state][ind]
#8- Manufacturing_Working_hours_index
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Manufacturing_Working_hours_index_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Manufacturing_Working_hours_index'] = df[STATES_CODES[state]][ind]
#9- Industrial_Capacity_Utilization_Index
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Industrial_Capacity_Utilization_Index_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Industrial_Capacity_Utilization_Index'] = df[STATES_CODES[state]][ind]
#10- Industrial_Production_Index
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Industrial_Production_Index_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Industrial_Production_Index'] = df[STATES_CODES[state]][ind]
#11- Steel_Production
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Steel_Production_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Steel_Production'] = df[STATES_REGION[state]][ind]
#12- Petroleum_Product_Sales
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Petroleum_Product_Sales_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Petroleum_Product_Sales'] = df[STATES_CODES[state]][ind]
#13- Energy_Generation
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Energy_Generation_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Energy_Generation'] = df[state][ind]
#14- Nominal_Revenue_Tourism_Index
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Nominal_Revenue_Tourism_Index_RealValues_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Nominal_Revenue_Tourism_Index'] = df[state][ind]      
#15- Retail_Trade_Index
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Retail_Trade_Index_RealValues_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Retail_Trade_Index'] = df[state][ind]
##16- Investment_goods_manufact
#df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Investment_goods_manufact_DA.csv')
#for ind in df.index:
#    values[df[df.columns[0]][ind]]['Investment_goods_manufact'] = df[state][ind]
#17- Real_GDP_SA
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Real_GDP_SA_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Real_GDP_SA'] = df[STATES_CODES[state]][ind]
#18- Tendancy_manufact_exports
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Tendancy_manufact_exports_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Tendancy_manufact_exports'] = df[STATES_CODES[state]][ind]
#19- Tendancy_manufact_production
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Tendancy_manufact_production_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Tendancy_manufact_production'] = df[STATES_CODES[state]][ind]
#20- Tendancy_employment
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Tendancy_employment_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Tendancy_employment'] = df[state][ind]
#21- Uncertainty_Index
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Uncertainty_Index_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Uncertainty_Index'] = df[state][ind]
#22- Dollar_Rate
df = pd.read_csv(folder1 + '/Spreadsheets/RealValues/Dollar_Rate_DailyCollapse_RealValues.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Dollar_Rate'] = df[state][ind]
#23- 3_months_bond_yield
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/3_months_bond_yield_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['3_months_bond_yield'] = df[state][ind]
#24- Ibov
df = pd.read_csv(folder1 + '/Spreadsheets/RealValues/Ibov_DailyCollapse_RealValues.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Ibov'] = df[state][ind]
#25_Savings_Deposits
df = pd.read_csv(folder1 + '/Spreadsheets/RealValues/Savings_Deposits_DailyCollapse_RealValues_MA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Savings_Deposits'] = df[state][ind]
#26- Foreign_Trade_Balance
df = pd.read_csv(folder1 + '/Spreadsheets/RealValues/Foreign_Trade_Balance_DA_RealValues_MA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Foreign_Trade_Balance'] = df[state][ind]
#27- Foreign_Trade_Index
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Foreign_Trade_Index_RealValues_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Foreign_Trade_Index'] = df[state][ind]
#28- Average_Real_Income
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Average_Real_Income_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Average_Real_Income'] = df[state][ind]
#29- Household_credit
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Household_credit_RealValues_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Household_credit'] = df[state][ind]
#30- Residential_prices
df = pd.read_csv(folder1 + '/Spreadsheets/DateAdjustment/Residential_prices_DA.csv')
for ind in df.index:
    values[df[df.columns[0]][ind]]['Residential_prices'] = df[state][ind]

res = pd.DataFrame(values).transpose().sort_index()


#ENTER TIME CODE ON THE LEFT
from datetime import timedelta

three_days_before_today = date.today() - timedelta(days = 3)
year = three_days_before_today.year
month = three_days_before_today.month
day = three_days_before_today.day
three_days_before_today = str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2) 


res = res[res.index >= '1996-01-01']
#res = res[res.index < three_days_before_today]   
 
frames = [df2, res]
result = pd.concat(frames)
result = result.fillna("NaN")
result = result.replace({'.': 'NaN'})
for col in result.columns:
    if (result[col] == 'NaN').sum() == (len(result.index) - 3):
        result = result.drop([col], axis=1)

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

year_li.append(0)
quarter_li.append(0)
month_li.append(0)

result.insert(0, 'year', year_li)
result.insert(1, 'quarter', quarter_li)
result.insert(2, 'month', month_li)

result = result.head(-1)

#OUTPUT
result.to_csv("Auxiliar/SeniorThesis_MainOutput.csv", index_label='date')
result.to_excel("Index_Calculation/SeniorThesis_MainOutput.xlsx", index_label='date')