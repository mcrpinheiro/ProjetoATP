import FreeSimpleGUI as sg
from functions import *
from threading import Thread
from time import sleep


def formatPostWindow (post, dataset):
    title = [sg.Text(f"{dataset[post]['title']}", font= ('Arial', 17))]
    titleAuthors = [sg.Text(f"Autores:", font= ('Arial', 15, "bold"))]

    table = [['PDF', dataset[post]['pdf']], 
            ['DOI', dataset[post]['doi']], 
            ['URL', dataset[post]['url']]]
    tableLink = [sg.Table(values= table, font = ('Arial', 12), headings=['Referências', 'Link'], 
                      auto_size_columns=True, justification='left',
                      expand_x=True,
                      expand_y=True,
                      key = '-tabela_links-',
                      enable_events=True,
                      enable_click_events = True,
                      num_rows=3,
                      )]
    postWindowLayout = [title, titleAuthors]
    for author in dataset[post]['authors']:
        postWindowLayout.append([sg.Text(f"{author['name']}", font= ('Arial', 13))])
        if 'affiliation' in author:
            postWindowLayout.append([sg.Text(f"{author['affiliation']}", font= ('Arial', 10))])
    if 'keywords' in dataset[post]: 
        keywords = [sg.Text(f"Keywords: {dataset[post]['keywords']}", font= ('Arial', 12))]
        postWindowLayout.append(keywords)
    titleAbstract = [sg.Text(f"Abstract:", font= ('Arial', 13, "bold"))]
    abstract = [sg.Multiline(f"{dataset[post]['abstract']}", font = ('Arial', 12), size=(None,5), expand_x=True, expand_y=True, disabled=True)]
    postWindowLayout.append(titleAbstract)
    postWindowLayout.append(abstract)
    postWindowLayout.append(tableLink)
    postWindowLayout.append([sg.Button('Fechar', key = '-FECHAR-')])
    return postWindowLayout

def createTable (dataset):
    table = []
    for post in dataset:
        tableLine = ["-", "-", "-"]
        tableLine[0] = post['title']
        if 'keywords' in post:
            tableLine[1] = post['keywords']
        if 'publish_date' in post:
            tableLine[2] = post['publish_date']
        table.append(tableLine)
    return table


def openPostsWindow(dataset):
    
    if not dataset:
        sg.popup(f'Ainda não existem publicações registadas.', title='Aviso')
    else:
        dados_tabela = createTable(dataset)
        cabecalho = ["Title", "Keywords", "Date"]
        layout = [
            [sg.Text(f"Publicações Disponíveis", font= ('Arial', 20))],
            [sg.Table(values= dados_tabela, font = ('Arial', 12), headings= cabecalho, 
                      auto_size_columns=True, justification='left',
                      expand_x=True,
                      expand_y=True,
                      key = '-tabela_posts-', num_rows = 15, 
                      enable_events=True,
                      enable_click_events = True)],
            [sg.Button('Fechar',key='-FECHAR-')]
        ]

        posts_window = sg.Window(f"Publicações disponíveis", layout, 
                                  modal= False, font= ('Helvetica', 20), 
                                  location= (200, 200), resizable = True)
    
        stop = False
        while not stop:
            event,_ = posts_window.read()
            if event in [sg.WINDOW_CLOSED, '-FECHAR-']:
                stop = True
            elif isinstance(event, tuple):
                _, _, (row, _) = event
                if row!= -1:
                    selectedPost_window = sg.Window(f"Publicação Selecionada", formatPostWindow(row,dataset), 
                                  modal= False, font= ('Arial', 12), 
                                  location= (200, 200), resizable = True, finalize = True)
                    stop2 = False
                    while not stop2:
                        postEvent,_ = selectedPost_window.read()
                        if postEvent in [sg.WINDOW_CLOSED, '-FECHAR-']:
                            selectedPost_window.close()
                            stop2 = True
        posts_window.close()