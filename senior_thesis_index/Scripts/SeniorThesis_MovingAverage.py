import pandas as pd


df = pd.read_csv('Spreadsheets/RealValues/Savings_Deposits_DailyCollapse_RealValues.csv', index_col='date')
df['Brazil'] = df['Brazil'].rolling(4).mean()
df.to_csv('Spreadsheets/RealValues/Savings_Deposits_DailyCollapse_RealValues_MA.csv')


df = pd.read_csv('Spreadsheets/RealValues/Foreign_Trade_Balance_DA_RealValues.csv', index_col='date')
df['Brazil'] = df['Brazil'].rolling(4).mean()
df.to_csv('Spreadsheets/RealValues/Foreign_Trade_Balance_DA_RealValues_MA.csv')
