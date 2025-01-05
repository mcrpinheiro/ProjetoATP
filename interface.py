import FreeSimpleGUI as sg
from interface_auxiliares import *
from functions import *

dataset = []



sg.theme('darkgrey11')

menu_layout = [
    [sg.Text('Bem vindo ao sistema de consulta e análise de publicações científicas!', font=("Arial",15,'bold'))],
    [sg.Button("Verificar Publicações Disponíveis", key = '-PUBLICACOES-', font=('Arial', 15))],
    [sg.Button("Carregar", key = '-CARREGAR-', font=('Arial', 15))],
    [sg.Button("Sair", key = '-SAIR-', font=('Arial', 15))] 
]


layout = [
    [sg.Column(menu_layout, element_justification='centre')]
]

window = sg.Window("Sistema de Consulta e Análise de Publicações Científicas", layout, font= ('Helvetica', 24), element_justification='c')

stop = False
while not stop:
    event, values = window.read()
    if event in [sg.WINDOW_CLOSED, '-SAIR-']:
        stop = True
    elif event == '-CARREGAR-':
        ficheiro = sg.popup_get_file("Selecione o ficheiro JSON",
                                     file_types=(("Ficheiros JSON", "*.json"),))
        dataset = loadFile(ficheiro)
        if dataset:
            print(f"Dataset carregado!\n Foram lidos {len(dataset)} registos.")
    elif event == '-PUBLICACOES-':
        if dataset:
            openPostsWindow(dataset)
        else:
            sg.popup(f'Ainda não existem publicações registadas.', title='Aviso')
    else:   
        print(f"Opção não suportada:{event} - {values}\n")
window.close()