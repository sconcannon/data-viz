#! python3
# testing gspread access and functionality
# using a copy of the Microbe_scope sheet from Ch 5 of
# Data Visualisation with Python and Javascript

import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('data/g_api_keyfile.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('Microbe_scope')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)