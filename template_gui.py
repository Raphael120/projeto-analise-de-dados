import PySimpleGUI as sg

layout = [
    [sg.Text('Linha 1', key='-Line1-'), sg.Button('Botão Linha 1')],
    [sg.In('Input 2', key='-Input2-'), sg.Button('Botão Linha 2')],
]

window = sg.Window('Teste', layout)

while True:
    event, values = window.read()
    print(event, values)
    
    if event == sg.WIN_CLOSED:
        break
        
window.close()
