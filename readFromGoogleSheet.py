import PySimpleGUI as sg
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials 
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\User\\Desktop\\CYF\\python\\secrit_key.json",scopes=scopes)
file=  gspread.authorize(creds)
workbook = file.open("data")
sheet = workbook.sheet1
for call in sheet.range('A2:A10'):
    print(call.value)
print(sheet.range('A2:A3'))
