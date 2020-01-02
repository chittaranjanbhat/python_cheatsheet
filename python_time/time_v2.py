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
month_day = datetime.today().strftime('X%d').replace('X0', '')
week_day = datetime.today().strftime('%a').lower()
print('Day of the week: ',week_day)
print('Day of month: ',month_day)
data = [['daily.dat','{"type":"daily","interval":"allday"}','daily','06:00:00'],
        ['intraday.dat','{type":"intraday","interval":"allday"}','intraday','06:00:00'],
        ['weekly.dat','{"type":"weekly","interval":"mon,fri,sun"}','weekly','06:00:00'],
        ['monthly.dat','{"typ":"montly","include":"1|3|12|29"}','monthly','06:00:00'],
        ['monthly.dat','{"typ":"montly","exclude":"1|12|29"}','monthly','06:00:00']]
df = pd.DataFrame(data,columns=['file_name','json','day_type','time'])

for ind in df.index: 
     if df['day_type'][ind] == 'daily':
         print()
#         print(df['json'][ind])
#         
     if df['day_type'][ind] == 'intraday':
         print()
#         print('intraday job:')
#         print(df['json'][ind])
#         
     if df['day_type'][ind] == 'weekly':
#         print('weekly job:')
#         print(df['json'][ind])
         loaded_json = eval(df['json'][ind])
         list1 = loaded_json['interval'].split(',')
         if week_day in list1:
             print(week_day)
         
         
     if df['day_type'][ind] == 'monthly':
        loaded_json = eval(df['json'][ind])
        if 'include' in loaded_json.keys():
            list1 = loaded_json['include'].split('|')
            if month_day in list1:
                print('today job listed in include list',month_day)
        elif 'exclude' in loaded_json.keys():
            list1 = loaded_json['exclude'].split('|')
            if month_day not in list1:
                print('today job listed not in exclude list',month_day)