# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 01:57:51 2019

@author: chitt
"""

import pandas as pd

df = pd.read_excel('Test.xlsx', sheet_name='Sheet1')
df1 = pd.read_excel('Test.xlsx', sheet_name='Sheet2')
#df['Description'] = df.loc[df['Desc 2'].isnull(),'Desc 4'] = df["Desc 1"]

df.loc[df.Result == 'Pass', 'Description'] = df['Desc 1']  
df.loc[df.Result != 'Pass', 'Description'] = df['Desc 2']

df_final = df[['Column A','Column B','Table Name','Description']]
df1_final = df1[['Column C','Column D','Table Name']]

df3 = df_final.join(df1_final.set_index('Table Name'), on='Table Name')

print(df3)