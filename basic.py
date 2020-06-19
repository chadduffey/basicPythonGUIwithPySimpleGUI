# pip3 install PySimpleGUI

import PySimpleGUI as sg 

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create Window
window = sg.Window("Demo", layout)

# Create an event loop (similar to windows api apps)
while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
