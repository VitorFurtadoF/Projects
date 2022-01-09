"""
Summary of Coding Sample1

"""

from download_path import download_path

LAST_DATE_IF_LEAP = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
LAST_DATE = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} 


SERIES_ID_SR = {
#Financial Data/Gov
'Ibov': '40774401_SR4685374', #3
'Monthly_CPI': '210989202_SR3670683', #46
#'Market_Expectations:GDP': '240781002_SR4538465', #4
'Unemployment_Claims': '458692687_SR143241917', #16
#Mobility
'Air_Traffic_(Domestic)': '292262901_SR4338520', #19
#Agriculture
'Agriculture_Price:Soybean': '455427917_SR143496007', #20
'Soy_(Volume)': '228948202_SR4333080', #21
#Industry
'Automobile_Sales': '205388802_SR4266819', #25
#Mining
'Aluminium_Production(Volume)': '297369901_SR4494582', #31
#Energy 
'Energy_Generation': '365246102_SR6741274', #37
#Services
'Retail_Trade_Index': '385726277_SR105535237', #45
}

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from collections import defaultdict
import pandas as pd
import time
import datetime
import calendar


# Log in the CEIC database website. 
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : download_path}
chrome_options.add_experimental_option('prefs', prefs)


folder1 = os.getcwd()
values = defaultdict(dict)
path = folder1 + r'/Auxiliar/chromedriver'
driver = webdriver.Chrome(executable_path=path, options=chrome_options)

driver.get('https://insights-ceicdata-com.proxy.library.nd.edu/Untitled-insight/myseries')

input("Log in Okta and then press Enter to continue...")

#Sign as Guest
elem0 = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div[1]/a').click()
time.sleep(3)

#Use the file download_path to 
path = download_path


#Series in this project have different frequencies. This function 
def change_dates_order(df):

    last_row = len(df.index)
    last_column = len(df.columns)
    values.clear()
    
    for i in range(0,last_row):

        if len(df.iloc[i]['date']) == 10:
            year = int(df.iloc[i]['date'][6:10])
            month = int(df.iloc[i]['date'][3:5])
            day = int(df.iloc[i]['date'][0:2])
        elif len(df.iloc[i]['date']) == 7:
            year = int(df.iloc[i]['date'][3:7])
            month = int(df.iloc[i]['date'][0:2])
            if (calendar.isleap(year)):
                day = LAST_DATE_IF_LEAP[month]
            else:    
                day = LAST_DATE[month]

        date = datetime.datetime(year,month,day)

        year = date.year
        month = date.month
        day = date.day

        for j in range (1,last_column):    
            values[str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)][df.columns[j]] = df.iloc[i][j]            
        
    return pd.DataFrame(values).transpose().reset_index().rename(columns={"index": "date"})

#USING SELENIUM - "Controlling Chrome"
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Requesting the series
for series in SERIES_ID_SR:

    #Download file. 
    driver.get('https://insights-ceicdata-com.proxy.library.nd.edu/series/' + SERIES_ID_SR[series])
    time.sleep(4)

    for i in range(1,6):
        try:
            element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[4]/div/button')))
            element.click()
            break
        except: 
            if(i==5):
                print('Download buttom is giving us trouble')

    time.sleep(3)
    elem2 = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]').click()
    elem3 = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/label/span').click()
    elem4 = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div/div[3]/div[2]/button[4]/span').click()
    time.sleep(5)
    
    #Reading the downloaded file.
    try: 
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path,i)):
                file1 = i

    
        df = pd.read_csv(path + file1, error_bad_lines=False)
    except: 
        time.sleep(5)
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path,i)):
                file1 = i
        df = pd.read_csv(path + file1, error_bad_lines=False)
    #except:
    #    try:
    #        df = pd.read_csv(path + file1, encoding='iso-8859-1', error_bad_lines=False)
    #    except:
    #        try:
    #            df = pd.read_csv(path + file1, encoding='latin1', error_bad_lines=False)
    #        except:
    #            try:
    #                df = pd.read_csv(path + file1, encoding='iso-8859-1', error_bad_lines=False)
    #            except:
    #                df = pd.read_csv(path + file1, encoding='cp1252', error_bad_lines=False)

    #The Monthly_CPI series is outputted in a different format. Create exception. 
    if series == 'Monthly_CPI':
        df = df.tail(-25)
    else: 
        df = df.tail(-24)

    #Add values to a dictionary
    last_row = len(df.index)
    for i in range(1,last_row):
        values[df.iloc[i][0]][series] = df.iloc[i][1]
    
    os.remove(path + file1)

#From the dictionary, create CSV table. 
df = pd.DataFrame(values).transpose().reset_index()
df = df.rename(columns={"index": "date"})

df = change_dates_order(df)

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

#OUTPUT
df.to_csv(folder1 + '/Sample_data.csv', index=False)

#Log Out
try:
    driver.get('https://insights-ceicdata-com.proxy.library.nd.edu/Untitled-insight/myseries')
    elem_last = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[5]/div[1]/button').click()
except:
    print('Driver was not able to log out')

driver.quit()
quit()
