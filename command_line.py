from ficheiros import * 

def menu():
    data = []
    selectedOption = input('''Bem vindo ao sistema de consulta e análise de publicações científicas.
                        Que operação deseja executar?
                           (1) Ajuda
                           (2) Criar Publicação
                           (3) Consulta de Publicação
                           (4) Consultar Publicações
                           (5) Eliminar Publicação
                           (6) Relatório de Estatísticas
                           (7) Listar Autores
                           (8) Importar Publicações
                           (9) Guardar Publicações
                           (0) Sair''')
    helpMenu = ('''Bem vindo ao menu de ajuda do sistema. Para exercutar alguma das opções abaixo, digite o número correspondente à mesma.
                    (2) Criar Publicação: criação de uma nova publicação com informações fornecidas pelo utilizador
                    (3) Consulta de Publicação: consultar as informações detalhadas de uma publicação especificada pelo utilizador
                    (4) Consultar Publicações: lista as
                    (5) Eliminar Publicação: eliminar uma publicação especificada pelo utilizador
                    (6) Relatório de Estatísticas: gerar 
                    (7) Listar Autores: lista todos os autores existentes na base de dados fornecida.
                    (8) Importar Publicações: importa uma base de dados de um ficheiro JSON.
                    (9) Guardar Publicações: atualizar a base de dados com novas informações fornecidas
                    (0) Sair''')
    while selectedOption!='0':
        if selectedOption == '1':
            print(helpMenu)
            selectedOption = input('Deseja realizar alguma destas operações?')
        elif selectedOption == '2':
            insertNew(data)
            selectedOption = input('Deseja realizar alguma destas operações?')
menu()