import FreeSimpleGUI as sg
from interface_auxiliares import *
from functions import *


#Modelo de Dados
dataset = loadFile('ata_medica_papers.json')

#Layout de Interface
#2blocos com divisão -> 3 linhas

sg.theme('darkgrey11')

menu_layout = [
    [sg.Text('Bem vindo ao sistema de consulta e análise de publicações científicas!', font=("Arial",15,'bold'))],
    [sg.Button("Verificar Publicações Disponíveis", key = '-PUBLICACOES-', font=('Arial', 15))],
    [sg.Button("Carregar", key = '-CARREGAR-', font=('Arial', 15))],
    [sg.Button("Sair", key = '-SAIR-', font=('Arial', 15))] 
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
    elif event == '-PUBLICACOES-':
        if dataset:
            openPostsWindow(dataset)
        else:
            sg.popup(f'Ainda não existem publicações registadas.', title='Aviso')
    else:   
        print(f"Opção não suportada:{event} - {values}\n")
window.close()