#IPEADATA

"""
23	IPEA DATA	3_months_bond_yield	Taxa de juros pré fixada - estrutura a termo - LTN - 3 meses: ANBIMA12_TJTLN312
"""

import pyIpeaData as ipea
import pandas as pd

df = pd.DataFrame(ipea.get_serie('ANBIMA12_TJTLN312'))

df['date'] = df['VALDATA'].str[:10]
df1 = df[['date','VALVALOR']].rename(columns={"VALVALOR": "Brazil"})
df1.to_csv('Spreadsheets/3_months_bond_yield.csv', index=False)
