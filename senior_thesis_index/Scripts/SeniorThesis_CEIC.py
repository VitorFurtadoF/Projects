#NATIONAL DATASET
#CEIC

from download_path import download_path

"""
Index	Source	Series_Code	Link/Code
2	CEIC	Fuel_Price_Ethanol	ID: 255784002 SR Code: SR4964096
3	CEIC	Air_Traffic_(Domestic)	ID: 292262901 SR Code: SR4338520
4	CEIC	Unemployment_Rate	ID: 475685597 SR Code: SR157483527
5	CEIC	Unemployment_Claims	ID: 458692687 SR Code: SR143241917
6	CEIC	Agriculture_Price:Soybean	ID: 455427917 SR Code: SR143496007
7	CEIC	Automobile_Sales	ID: 205388802 SR Code: SR4266819
8	CEIC	Manufacturing_Working_hours_index	ID: 356295407 SR Code: SR7300823
9	CEIC	Industrial_Capacity_Utilization_Index	ID: 283504504 SR Code: SR6658430

11	CEIC	Steel_Production	ID: 297371601 SR Code: SR4489914
12	CEIC	Petroleum_Product_Sales	ID: 229230402 SR Code: SR4326341
13	CEIC	Energy_Generation	ID: 365246102 SR Code: SR6741274
14	CEIC	Nominal_Revenue_Tourism_Index	ID: 385720717 SR Code: SR105578867
15	CEIC	Retail_Trade_Index	ID: 385726277 SR Code: SR105535237

17	CEIC	Real_GDP_SA	ID: 366988057 SR Code: SR88309317

22	CEIC	Dollar_Rate	ID: 1326501 SR Code: SR4690985

24	CEIC	Ibov	ID: 40774401 SR Code: SR4685374
25	CEIC	Savings Deposits	ID: 455322477 SR Code: SR141339927
26	CEIC	Foreign_Trade_Balance	ID: 245232002 SR Code: SR4641526
27	CEIC	Foreign_Trade_Index	ID: 471295677 SR Code: SR153983837
28	CEIC	Average_Real_Income	ID: 376266557 SR Code: SR98321397

-   CEIC    Monthly_Inflation	ID: 273491403 SR Code: SR5814771

"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from collections import defaultdict
import pandas as pd
import time
import datetime


chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : download_path}
chrome_options.add_experimental_option('prefs', prefs)

folder1 = os.getcwd()
path = folder1 + r'/Auxiliar/chromedriver'

driver = webdriver.Chrome(executable_path=path, options=chrome_options)

driver.get('https://insights-ceicdata-com.proxy.library.nd.edu/Untitled-insight/myseries')  

#input("Log in Okta and then press Enter to continue...")

#Sign as Guest
elem0 = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div[1]/a').click()
time.sleep(3)

path = download_path

def change_dates_order(df):

    last_row = len(df.index)
    last_column = len(df.columns)
    values.clear()
    
    for i in range(0,last_row):

        #print(df.iloc[i]['date'])
        year = int(df.iloc[i]['date'][6:10])
        month = int(df.iloc[i]['date'][3:5])
        day = int(df.iloc[i]['date'][0:2])
        date = datetime.datetime(year,month,day)

        year = date.year
        month = date.month
        day = date.day

        for j in range (1,last_column):    
            values[str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)][df.columns[j]] = df.iloc[i][j]            
        
    return pd.DataFrame(values).transpose().reset_index().rename(columns={"index": "date"})

SERIES_NAMES = [
'Fuel_Price_Ethanol','Air_Traffic_(Domestic)','Unemployment_Rate','Unemployment_Claims',
'Agriculture_Price:Soybean','Automobile_Sales','Manufacturing_Working_hours_index','Industrial_Capacity_Utilization_Index',
'Steel_Production','Petroleum_Product_Sales','Energy_Generation','Nominal_Revenue_Tourism_Index','Retail_Trade_Index',
'Real_GDP_SA','Dollar_Rate','Ibov','Savings_Deposits','Foreign_Trade_Balance','Foreign_Trade_Index','Average_Real_Income', 'Monthly_Inflation']

SERIES_ID = {
'Fuel_Price_Ethanol': '255784002','Air_Traffic_(Domestic)': '292262901','Unemployment_Rate': '475685597','Unemployment_Claims': '458692687',
'Agriculture_Price:Soybean': '455427917','Automobile_Sales': '205388802','Manufacturing_Working_hours_index': '356295407',
'Industrial_Capacity_Utilization_Index': '283504504','Steel_Production': '297371601','Petroleum_Product_Sales': '229230402',
'Energy_Generation': '365246102','Nominal_Revenue_Tourism_Index': '385720717','Retail_Trade_Index': '385726277','Real_GDP_SA': '366988057',
'Dollar_Rate': '1326501','Ibov': '40774401','Savings_Deposits': '455322477','Foreign_Trade_Balance': '245232002','Foreign_Trade_Index': '471295677',
'Average_Real_Income': '376266557', 'Monthly_Inflation': '273491403'}

SERIES_SR = {
'Fuel_Price_Ethanol': 'SR4964096', 'Air_Traffic_(Domestic)': 'SR4338520', 'Unemployment_Rate': 'SR157483527', 'Unemployment_Claims': 'SR143241917',
'Agriculture_Price:Soybean': 'SR143496007', 'Automobile_Sales': 'SR4266819', 'Manufacturing_Working_hours_index': 'SR7300823',
'Industrial_Capacity_Utilization_Index': 'SR6658430', 'Steel_Production': 'SR4489914', 'Petroleum_Product_Sales': 'SR4326341',
'Energy_Generation': 'SR6741274', 'Nominal_Revenue_Tourism_Index': 'SR105578867', 'Retail_Trade_Index': 'SR105535237',
'Real_GDP_SA': 'SR88309317', 'Dollar_Rate': 'SR4690985', 'Ibov': 'SR4685374', 'Savings_Deposits': 'SR141339927',
'Foreign_Trade_Balance': 'SR4641526', 'Foreign_Trade_Index': 'SR153983837','Average_Real_Income': 'SR98321397', 'Monthly_Inflation': 'SR5814771'}


for series in SERIES_NAMES:
    
    values = defaultdict(dict)
    print('Working on', series)

    ID = SERIES_ID[series]
    SR = SERIES_SR[series]
    
    #go to webpage
    driver.get('https://insights-ceicdata-com.proxy.library.nd.edu/series/' + ID + '_' + SR)
    time.sleep(4)

    #download series
    for i in range (1,51):
        if i != 50:
            try:
                elem1 = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[4]/div/button').click()
                break
            except:
                time.sleep(1)
                continue
        else: 
            print('Brazil ' + series + ' has malfunctioned')
    time.sleep(3)

    elem2 = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/label/span').click()
    elem3 = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/label/span').click()

    #CHANGE DATE FORMAT
    elem3_1 = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[4]/div[2]/div/div[1]').click()
    elem3_2   = driver.find_element_by_xpath('/html/body/ul/div[3]/li[2]/div/label').click()
    date_format = 'YYYY-MM-DD'
    elem3_3 = driver.find_element_by_xpath('/html/body/ul/div[3]/li[2]/div/div/div[1]/input').clear()
    elem3_3 = driver.find_element_by_xpath('/html/body/ul/div[3]/li[2]/div/div/div[1]/input').send_keys(date_format)
    #input("Log in Okta and then press Enter to continue...")

    elem4 = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div/div[3]/div[2]/button[4]').click()
    
    #get data from Downloads folder
    time.sleep(5)
    file1 =''
    for j in range (0,11):
        if j == 10:
            print('Unable to get',series, 'data for Brazil')
            break
        for i in os.listdir(path):
            file1 = i
        if file1 == '':
            time.sleep(3)
            continue
        else:
            break
    try: 
        df = pd.read_csv(path + file1, error_bad_lines=False)
    except:
        try:
            df = pd.read_csv(path + file1, encoding='iso-8859-1', error_bad_lines=False)
        except:
            try:
                df = pd.read_csv(path + file1, encoding='latin1', error_bad_lines=False)
            except:
                try:
                    df = pd.read_csv(path + file1, encoding='iso-8859-1', error_bad_lines=False)
                except:
                    df = pd.read_csv(path + file1, encoding='cp1252', error_bad_lines=False)
    df = df.tail(-24)
    last_row = len(df.index)
    for i in range(1,last_row):
        values[df.iloc[i][0]]['Brazil'] = df.iloc[i][1]
    
    os.remove(path + file1)
    
    df = pd.DataFrame(values).transpose().reset_index()
    df = df.rename(columns={"index": "date"})

    #print(df)
    #df = change_dates_order(df)

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(by="date")

    df.to_csv(folder1 + '/Spreadsheets/' + series + '.csv', index=False)

#Log Out
try:
    driver.get('https://insights-ceicdata-com.proxy.library.nd.edu/Untitled-insight/myseries')
    elem_last = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div/div[5]/div[1]/button').click()
except:
    print('Driver was not able to log out')

driver.quit()
quit()