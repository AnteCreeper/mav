# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:42:03 2022

@author: erofe
"""

import PySimpleGUI as sg

layout = [
    [sg.Text('File 1'), sg.InputText(), sg.FileBrowse()],
    [sg.Text('File 2'), sg.InputText(), sg.FileBrowse()],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('File Compare', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break