import pyfiglet

import PySimpleGUI as sg

sg.theme("DarkTeal9")
sg.set_options(font=("Courier New", 13))

fonts = ['graffiti', 'basic', 'banner3-D', 'big', 'block', 'isometric4', 'crawford', 'cursive', 'devilish', 'diamond']

layout = [
            [sg.Text('Enter a text')],
            [sg.InputText(size=(70, 1))],
            [sg.Text('Select a font')],
            [sg.InputCombo(fonts, default_value='graffiti', size=(69, 1))],
            [sg.Button('Generate'), sg.Button('Close')],
            [sg.Text('_'  * 100, size=(70, 1))],
            [sg.Text('Your ASCII ART ....', key="OUT")]
        ]

window = sg.Window('ASCII ART GENERATOR', layout, margins=(70, 40))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    if event == 'Generate':
      custom_fig = pyfiglet.Figlet(font=values[1])
      ascii_text = custom_fig.renderText(values[0])
      window['OUT'].update(ascii_text)

window.close()
