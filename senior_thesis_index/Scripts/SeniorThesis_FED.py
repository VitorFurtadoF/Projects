#NATIONAL DATASET
#FED

"""
Index	Source	Series_Code	Link/Code

10	FRED	Industrial_Production_Index	https://fred.stlouisfed.org/series/BRAPROINDMISMEI#0

16	FRED	Investment_goods_manufact	https://fred.stlouisfed.org/series/PRMNVG01BRQ661S

18	FRED	Tendancy_manufact_exports	https://fred.stlouisfed.org/series/BSXRLV02BRM086S
19	FRED	Tendancy_manufact_production	https://fred.stlouisfed.org/series/BSPRFT02BRM460S
20	FRED	Tendancy_employment	https://fred.stlouisfed.org/series/BSEMFT02BRM460S
21	FRED	Uncertainty_Index	https://fred.stlouisfed.org/series/WUIBRA

29	FRED	Household_credit	https://fred.stlouisfed.org/series/QBRHAMUSDA#0
30	FRED	Residential_prices	https://fred.stlouisfed.org/series/QBRR368BIS
-   FRED    Monthly_Inflation_US  https://fred.stlouisfed.org/series/CPIAUCSL 

"""

import requests
import json
import pandas as pd
import time
from collections import defaultdict
import os
import numpy as np

URL = 'https://api.stlouisfed.org/fred/series/observations?'
PARAMETERS = {}
PARAMETERS['api_key'] = '92ba84e46c48ec39a53e15e4a1d40a09'
PARAMETERS['file_type'] = 'json'
RETRIES = 6
WAIT_RETRIES2 = [10,20,30,30,30]
WAIT_RETRIES = [20,20,20,60,60]

def get_data(seriesId):
    p = PARAMETERS.copy()
    p['series_id'] = seriesId

    attempt = 0
    while attempt < RETRIES:
        r = requests.get(URL, params=p)
        if r.status_code == 429 and attempt + 1 < RETRIES:
            print('RETRYING, attempt:', attempt, 'series_id:', seriesId, '(rate limit exceeded)')
            time.sleep(WAIT_RETRIES[attempt])
            attempt += 1
            continue

        if r.status_code == 504:
            print('Gateaway Timeout error. Try again')
            time.sleep(WAIT_RETRIES2[attempt])
            attempt += 1
            continue

        if not r.ok:
            print('ERROR:', r.json())
            print('ON SERIES ID:', seriesId)
            return pd.DataFrame()

        j = r.json()
        return pd.DataFrame(j['observations'])

def get_all_data(seriesIdFormat):
    values = defaultdict(dict)
    df = get_data(seriesIdFormat)
    for row in df.itertuples():
        values[getattr(row, 'date')]['Brazil'] = getattr(row, 'value')
    return pd.DataFrame(values).transpose().sort_index()

folder1 = os.getcwd()


#10- Industrial_Production_Index
get_all_data('BRAPROINDMISMEI').to_csv(folder1 + '/Spreadsheets/Industrial_Production_Index.csv', index_label='date')
#16- Investment_goods_manufact
get_all_data('PRMNVG01BRQ661S').to_csv(folder1 + '/Spreadsheets/Investment_goods_manufact.csv', index_label='date')
#18- Tendancy_manufact_exports
get_all_data('BSXRLV02BRM086S').to_csv(folder1 + '/Spreadsheets/Tendancy_manufact_exports.csv', index_label='date')
#19- Tendancy_manufact_production
get_all_data('BSPRFT02BRM460S').to_csv(folder1 + '/Spreadsheets/Tendancy_manufact_production.csv', index_label='date')
#20- Tendancy_employment
get_all_data('BSEMFT02BRM460S').to_csv(folder1 + '/Spreadsheets/Tendancy_employment.csv', index_label='date')
#21- Uncertainty_Index
get_all_data('WUIBRA').to_csv(folder1 + '/Spreadsheets/Uncertainty_Index.csv', index_label='date')
#29- Household_credit
get_all_data('QBRHAMUSDA').to_csv(folder1 + '/Spreadsheets/Household_credit.csv', index_label='date')
#30- Residential_prices
get_all_data('QBRR368BIS').to_csv(folder1 + '/Spreadsheets/Residential_prices.csv', index_label='date')
#- Monthly_Inflation_US
get_all_data('CPIAUCSL').to_csv(folder1 + '/Spreadsheets/Monthly_Inflation_US.csv', index_label='date')
