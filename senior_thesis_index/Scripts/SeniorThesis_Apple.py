#APPLE

from download_path import download_path

"""
Index	Source	Series_Code	Link/Code
1	Apple	Apple_Mobility_Index	https://www.apple.com/covid19/mobility
"""

import datetime
import requests
import pandas as pd
import io
import time
from selenium import webdriver
import os
import shutil

#Requesting Data
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : download_path}
chrome_options.add_experimental_option('prefs', prefs)


folder1 = os.getcwd()
path = folder1 + r'/Auxiliar/chromedriver'
driver = webdriver.Chrome(executable_path=path, options=chrome_options) 

driver.get('https://www.apple.com/covid19/mobility')
elem = driver.find_element_by_xpath('//*[@id="download-card"]/div[2]/ui-button')
time.sleep(3)
elem.click()
time.sleep(3)
driver.quit()

path = download_path
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)) and 'applemobilitytrends' in i:
        file1 = i

#Read csv in Pandas

df = pd.read_csv(path + file1)
os.remove(path + file1)

#Querying data
my_query = "region == 'Brazil'"

df.query(my_query, inplace = True)
df.query("transportation_type == 'driving'", inplace = True)

del df['transportation_type']
del df['alternative_name']
del df['sub-region']
del df['country']
del df['geo_type']

df.set_index('region',inplace=True)
df = df.transpose()
df = df.reset_index()
df = df.rename(columns={"index": "date"})
df.set_index('date',inplace=True)

#Saving

df.to_csv(folder1 + '/Spreadsheets/Apple_Mobility_Index.csv')
quit(0)