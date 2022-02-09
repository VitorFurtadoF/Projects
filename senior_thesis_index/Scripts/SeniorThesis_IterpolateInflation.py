import pandas as pd


#CREATE WEEKLY INFLATION BRAZIL
df = pd.read_csv('Spreadsheets/Monthly_Inflation.csv')

df['date'] = pd.to_datetime(df['date'])
rng = pd.date_range(df['date'].min(), df['date'].max(), freq='D')
df = df.set_index('date')

df_reindexed = df.reindex(rng).interpolate(method='linear')


df_reindexed = df_reindexed[df_reindexed.index.weekday == 5]
df_reindexed.to_csv('Spreadsheets/Monthly_Inflation_weekly.csv')


#CREATE WEEKLY INFLATION US

df = pd.read_csv('Spreadsheets/Monthly_Inflation_US.csv')

df['date'] = pd.to_datetime(df['date'])
rng = pd.date_range(df['date'].min(), df['date'].max(), freq='D')
df = df.set_index('date')

df_reindexed = df.reindex(rng).interpolate(method='linear')


df_reindexed = df_reindexed[df_reindexed.index.weekday == 5]
df_reindexed.to_csv('Spreadsheets/Monthly_Inflation_US_weekly.csv')
