import PySimpleGUI as sg
import pandas as pd
# add some color to the window 
sg.theme('DarkTeal9')

EXCEL_FILE= 'data.xlsx'
df=pd.read_excel(EXCEL_FILE)

layout = [ 
          [sg.Text("Please fill out the following fields: ")],
          [sg.Text('Name', size=(15,1)),sg.InputText(key='Name')],
          [sg.Text('Favorite Colour',size=(15,1)),sg.Combo(['Green','Blue','Red'],key='Favorite Colour')],
          [sg.Text('I speak',size=(15,1),),
             sg.Checkbox('German',key='German'),
             sg.Checkbox('Arbic',key='Arbic'),
             sg.Checkbox('English',key='English')
           ],
          [sg.Text('No. of childern',size=(15,1),),sg.Spin([i for i in range(0,16)], initial_value=0,key='Childern')],
          [sg.Submit(), sg.Exit()]
          ]

window= sg.Window('Simple data entry form',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        df=df.append(values,ignore_index=True)
        df.to_excel(EXCEL_FILE,index=False)
        sg.popup('Data saved!')
       
       
window.close()
   