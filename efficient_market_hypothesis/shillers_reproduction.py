#pip install pandas, numpy, matplotlib, scipy

#!/usr/bin/env python3

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats.mstats import gmean
from scipy.signal import detrend

df = pd.read_csv('historical-data.csv')

# parse date from 2019.01, 2019.02, ... 2019.1, 2019.11, 2019.12 format
def read_date(x):
    x = str(x)
    if len(x) == 6:
        x += "0"
    return pd.to_datetime(x, format="%Y.%m")

df['Date'] = pd.to_datetime(df['Date'].apply(read_date), errors='coerce')
df.set_index("Date")

# interpolate interest rates (some values are missing for the first few years)
df['Long Interest Rate GS10'] = df['Long Interest Rate GS10'].interpolate()

# interpolate monthly dividends based on quarterly dividends
df['Dividends'] = df['Dividends'].interpolate()

# interpolate monthly earnings based on quarterly earnings
df['Earnings'] = df['Earnings'].interpolate()

# restrict to up to previous year, 2021 doesn't have all the necessary data
df = df.loc[df["Date"] < "2021-01-01"]

# use Consumer Price Index to compute how many dollars at the time would correspond to today's dollars due to inflation
# most_recent_cpi = 264.09
most_recent_cpi = df.iloc[-1]["Consumer Price Index"]
df["Inflation Adjustment"] = most_recent_cpi/df["Consumer Price Index"]

# compute prices adjusted by inflation
df["Real Price"] = df["S&P Composite Price"] * df["Inflation Adjustment"]

# compute dividends adjusted by inflation
df["Real Dividends"] = df["Dividends"] * df["Inflation Adjustment"]

# compute earnings adjusted by inflation
df["Real Earnings"] = df["Earnings"] * df["Inflation Adjustment"]

# compute real total return price
df.loc[0, "Real Total Return Price"] = df.loc[0, "Real Price"]
for i in range(1, len(df)):
    df.loc[i, "Real Total Return Price"] = df.loc[i - 1, "Real Total Return Price"] * (df.loc[i, "Real Price"] + df.loc[i, "Real Dividends"]/12) / df.loc[i - 1, "Real Price"]

# compute 10-year annualized stock real return
for i in range(0, len(df) - 12):
    df.loc[i, "Real Return"] = (df.loc[i + 12, "Real Total Return Price"]/df.loc[i, "Real Total Return Price"]) - 1

# restrict to data up until 2002:
df = df.loc[df["Date"] < "2002-01-01"]

# determine the implicit discount rate r_e
r_e = gmean(1 + df["Real Return"]) - 1

print(f"r_e = {r_e}")

# determine the ex post rational price series
df.loc[len(df) - 1, "Rational Price"] = df.loc[len(df) - 1, "Real Price"]
for i in range(len(df) - 2, -1, -1):
    df.loc[i, "Rational Price"] = (df.loc[i+1, "Rational Price"] + df.loc[i+1, "Real Dividends"]/12) * (1 + r_e)**(-1/12)

desired_dates = (df["Date"] >= "1870-01-01") & (df["Date"] <= "1980-01-01")
df.plot(x="Date", y=["Real Price", "Rational Price"], figsize=(15, 10), title="S&P 500 Inflation-Corrected Real Prices vs. Ex Post Rational Prices")

df.plot(x="Date", y=["Real Price", "Rational Price"], figsize=(15, 10), title="S&P 500 Inflation-Corrected Real Prices vs. Ex Post Rational Prices (in logarithmic scale)", logy=True)

# detrend price series
df["Detrended Price"] = np.exp(detrend(np.log(df["Real Price"])))
df["Detrended Rational Price"] = np.exp(detrend(np.log(df["Rational Price"])))

df.loc[desired_dates].plot(x="Date", y=["Detrended Price", "Detrended Rational Price"], figsize=(15, 10), title="S&P 500 Detrended Prices vs. Detrended  Ex Post Rational Prices")

# compute standard deviation of the two series
stddev_p = np.std(df["Detrended Price"])
stddev_p_star = np.std(df["Detrended Rational Price"])

print(f"sigma(p) = {stddev_p}, sigma(p*) = {stddev_p_star}")

# generate graph for standard deviation comparison explanation
n = 30
x = np.linspace(0, 1, n)
y_real = np.random.choice([1, 2], n)
y_pred = np.full(n, 1.5)

plt.subplots(figsize=(15, 10))
plt.title("Real Series vs Expected Series")
plt.plot(x, y_real, label="Real Series")
plt.plot(x, y_pred, label="Expected Series")
plt.legend()
plt.show()

