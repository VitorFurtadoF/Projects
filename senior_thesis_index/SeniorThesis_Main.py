import os
import time

"""
Index	Source	Series_Code	Link/Code
1	Apple	Apple_Mobility_Index	https://www.apple.com/covid19/mobility
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
27	CEIC	Foreign_Trade_Index	ID: 471295677 SR Code: SR153983837
28	CEIC	Average_Real_Income	ID: 376266557 SR Code: SR98321397
29	FRED	Household_credit	https://fred.stlouisfed.org/series/QBRHAMUSDA#0
30	FRED	Residential_prices	https://fred.stlouisfed.org/series/QBRR368BIS
-   CEIC    Monthly_Inflation	ID: 273491403 SR Code: SR5814771
-   CEIC    Monthly_Inflation_US FRED https://fred.stlouisfed.org/series/CPIAUCSL  
"""

folder1 = os.getcwd()

def run(scriptname, filepath):
    for i in range (1,5):
        if i == 4:
            print('Script was not able to run ' + scriptname)
            quit()
        try:
            os.system("python3 " + folder1 + filepath)
            break
        except:
            if i != 3:
                print('Retrying ' + scriptname + '. Attempt ' + str(i+1))
            continue

start = time.time()
"""
print("Running IPEADATA")
run('IPEADATA','/Scripts/SeniorThesis_IPEADATA.py')
#input("INPUT: IpeaData")

print("Running FED")
run('FED','/Scripts/SeniorThesis_FED.py')

print("Running CEIC")
run('CEIC', '/Scripts/SeniorThesis_CEIC.py')

print("Running Apple")
run('Apple','/Scripts/SeniorThesis_Apple.py')
"""
print("Running Daily Collapse")
run('Daily Collapse','/Scripts/SeniorThesis_DailyCollapse.py')

print("Running Iterpolate Inflation")
run('Iterpolate Inflation','/Scripts/SeniorThesis_IterpolateInflation.py')

print("Running Date Adjustment WEEKLY")
run('Date Adjustment Weekly','/Scripts/SeniorThesis_DateAdjustment_weekly.py')

print("Running Real Values")
run('Iterpolate Inflation','/Scripts/SeniorThesis_RealValues.py')

print("Running Moving Average")
run('Moving Average','/Scripts/SeniorThesis_MovingAverage.py')

print("Running Seasonal Adjustment")
run('Seasonal Adjustment','/Scripts/SeniorThesis_SeasonalAdjustment.py')

print("Running Date Adjustment")
run('Date Adjustment','/Scripts/SeniorThesis_DateAdjustment.py')

print("Running MainOutput")
run('MainOutput','/Scripts/SeniorThesis_MainOutput.py')



end = time.time()
print(str(end - start) + 's')

quit()
