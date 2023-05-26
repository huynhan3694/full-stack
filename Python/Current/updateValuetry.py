import os
from Google import Create_Service
import pandas as pd
import numpy as np
# from splitFile import getValueTuple
CLIENT_SECRET_FILE = 'apivalue.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
# GET_VALUE = getValueTuple
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '13byGylyOUDpQZARlfq2mzm537_v65WzjMdUkeersQxI'

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION,SCOPES)

URL= "/home/datbike/Documents/FullStack/Python/dataFaker.csv"
df = pd.read_csv(URL)
df.replace(np.nan,'',inplace=True)
response_date = service.spreadsheets().values().append(
    spreadsheetId= SAMPLE_SPREADSHEET_ID,
    valueInputOption="RAW",
    range= 'Sheet1!A1',
    body=dict(
        majorDiemnsion='ROWS',
        values=df.T.reset_index().T.values.tolist()
    )
    ).execute()