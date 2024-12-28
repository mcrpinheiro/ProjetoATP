import FreeSimpleGUI as sg
from ficheiros import *


#Modelo de Dados
dataset = []


#Layout de Interface
#2blocos com divisão -> 3 linhas

sg.theme('darkgrey9')

menu_layout = [
    [sg.Text('Bem vindo ao sistema de consulta e análise de publicações científicas!', font=("Arial",15,'bold'))],
    [sg.Button("Carregar", key = '-CARREGAR-')],
    [sg.Button("Sair", key = '-SAIR-')] 
]
'''[sg.Button("Gravar", key = '-GRAVAR-')],
        [sg.Text('Cursos Disponíveis:')],
        [sg.Listbox(values = [], size=(12,6), key = '-lista_cursos-', enable_events=True)],
        '''

layout = [
    [sg.Column(menu_layout, element_justification='centre'),
     ]
]

#Escolha do tema


#Criar a janela
window = sg.Window("Sistema de Consulta e Análise de Publicações Científicas", layout, font= ('Helvetica', 24), element_justification='c')

#Event Listener
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
    else:   
        print(f"Opção não suportada:{event} - {values}\n")
window.close()