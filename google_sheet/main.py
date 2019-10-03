# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 02:35:00 2019

@author: chitt
"""

from googlesheet import Create_Service
import pandas as pd
import numpy as np


CLIENT_SECRET_FILE='client_secret.json'
API_SERVICE_NAME='sheets'
API_VESRION='v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
gsheetId = '1a8CjU2bVQY0w0P-UbW4rdBMWrBOVkYeAaXnIOeytBaY'

service = Create_Service(CLIENT_SECRET_FILE,API_SERVICE_NAME,API_VESRION,SCOPES)

def Export_Data_To_Sheets():
    URL = r'https://files.digital.nhs.uk/publicationimport/pub20xxx/pub20188/ccg-pres-data-oct-dec-2015-un-dat.csv'
    df = pd.read_csv(URL)
    df.replace(np.nan, '', inplace=True)

#    response_data = service.spreadsheets().values().append(
#        spreadsheetId=gsheetId,
#        valueInputOption='RAW',
#        range='DF!A1',
#        body=dict(
#            majorDimension='ROWS',
#            values=df.T.reset_index().T.values.tolist())
#    ).execute()


    URL2 = r'https://raw.githubusercontent.com/franciscadias/data/master/kc_house_data.csv'
    df2 = pd.read_csv(URL2)
    df2.replace(np.nan, '', inplace=True)

    response_data = service.spreadsheets().values().update(
        spreadsheetId=gsheetId,
        valueInputOption='RAW',
        range='DF2!A1',
        body=dict(
            majorDimension='ROWS',
            values=df2.T.reset_index().T.values.tolist())
    ).execute()

Export_Data_To_Sheets()