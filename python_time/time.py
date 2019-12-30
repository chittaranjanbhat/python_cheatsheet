# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:06:09 2019

@author: chitt
"""
#https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

from datetime import datetime
import pytz
import pandas as pd
import json
tz_NY = pytz.timezone('America/New_York') 
now = datetime.now(tz_NY).time() # time object
month_day = datetime.today().strftime('%d')
week_day = datetime.today().strftime('%a')
print("now =", now)
print("NY time:", now.strftime("%H:%M:%S"))
print('Day of the week: ',week_day)
print('Day of month: ',month_day)
data = [['daily.dat','{"type":"daily","interval":"allday"}','daily','06:00:00'],
        ['intraday.dat','{type":"intraday","interval":"allday"}','intraday','06:00:00'],
        ['weekly.dat','{"type":"weekly","interval":"Mon,Sun"}','weekly','06:00:00'],
        ['monthly.dat','{"typ":"montly","interval":"1,12,29"}','monthly','06:00:00']]
df = pd.DataFrame(data,columns=['file_name','json','day_type','time'])

for ind in df.index: 
     if df['day_type'][ind] == 'daily':
         print('daily job:')
         print(df['json'][ind])
         
     if df['day_type'][ind] == 'intraday':
         print('intraday job:')
         print(df['json'][ind])
         
     if df['day_type'][ind] == 'weekly':
         print('weekly job:')
         print(df['json'][ind])
         loaded_json = eval(df['json'][ind])
         print(loaded_json['interval'])
         
         
     if df['day_type'][ind] == 'monthly':
         print('monthly job:')
         print(df['json'][ind])