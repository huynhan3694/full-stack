import os
from Google import Create_Service
from splitFile import convertValue
CLIENT_SECRET_FILE = 'apivalue.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION,SCOPES)

SAMPLE_SPREADSHEET_ID = '1RH7NFwFrRAn-mgGadVkScjdV-SIGUw8at5KOfF9ov_k'
SAMPLE_RANGE_NAME = 'Class Sheet!A1:C6'

mySpreadsheets = service.spreadsheets().get(spreadsheetId=SAMPLE_SPREADSHEET_ID).execute()
worksheet_name = "Sheet1!"
cell_range_insert = 'A2'
# print((GET_VALUE))
# print(istOneLocation)
value_range_body = {
   'majorDimension':'ROWS',
   'values':convertValue.reset_index().values.tolist()}
service.spreadsheets().values().update(
   spreadsheetId=SAMPLE_SPREADSHEET_ID,
   valueInputOption='USER_ENTERED',
   range=worksheet_name + cell_range_insert,
   body=value_range_body
   ).execute()