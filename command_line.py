from functions import * 

def menu():
    data = loadFile('ata_medica_papers.json')
    newData = loadFile('ata_medica_papers.json')
    stop = False
    selectiveMenu = ('''Que operação deseja executar?
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
    helpMenu = ('''Bem vindo ao menu de ajuda do sistema. Para executar alguma das opções abaixo, digite o número correspondente à mesma.
                    (2) Criar Publicação: criação de uma nova publicação com informações fornecidas pelo utilizador
                    (3) Consulta de Publicação: consultar as informações detalhadas de uma publicação especificada pelo utilizador
                    (4) Consultar Publicações: lista as
                    (5) Eliminar Publicação: eliminar uma publicação especificada pelo utilizador
                    (6) Relatório de Estatísticas: gerar 
                    (7) Listar Autores: lista todos os autores existentes na base de dados fornecida.
                    (8) Importar Publicações: importa uma base de dados de um ficheiro JSON.
                    (9) Guardar Publicações: atualizar a base de dados com novas informações fornecidas
                    (0) Sair''')
    keyMenu = ('''Qual campo vai ser o identificador da ata desejada? Selecione o número correspondente:
               (1) Abstract
               (2) Nome de um Autor
               (3) DOI
               (4) PDF
               (5) Data de Publicação
               (6) Título
               (7) URL
               (0) Voltar ao Menu''')
    selectedOption = input(f'Bem vindo ao sistema de consulta e análise de publicações científicas. {selectiveMenu}')
    while not stop:
        if selectedOption in ['3', '4', '5', '6', '7'] and data == []:
            selectedOption = input('''Esta opção não está disponível pois não existem atas em sistema. O que deseja fazer?
                                   (1) Ajuda
                                   (8) Importar Publicações
                                   (0) Sair''')
        if selectedOption == '1':
            print(helpMenu)
            selectedOption = input('Deseja realizar alguma destas operações?')
        elif selectedOption == '2':
            insertNew(newData)
            selectedOption = input(selectiveMenu)
        elif selectedOption == '3':
            postIdentificator = input(keyMenu)
            if postIdentificator not in ['0','1', '2', '3', '4', '5', '6', '7']: 
                print('Operação não suportada. Por favor tente outra vez.')
                postIdentificator = input(keyMenu)    
            elif postIdentificator == '0':
                selectedOption = input(selectiveMenu)
            else:
                targetInfo = input(f"Qual {print(keyIdentificator(postIdentificator))} deseja pesquisar?")
                print(findPost(postIdentificator, targetInfo, data))
                selectedOption = input(selectiveMenu)
        #elif selectedOption == '4':
        elif selectedOption == '5':
            postIdentificator = input(keyMenu)
            if postIdentificator not in ['0','1', '2', '3', '4', '5', '6', '7']: 
                print('Operação não suportada. Por favor tente outra vez.')
                postIdentificator = input(keyMenu)    
            elif postIdentificator == '0':
                selectedOption = input(selectiveMenu)
            else:
                targetInfo = input(f'Qual {keyIdentificator(postIdentificator)} deseja pesquisar?')
                confirmDelete = input(f"Deseja apagar a ata com {keyIdentificator(postIdentificator)} correspondente a {targetInfo}? S/N")
                if confirmDelete in ['S', 's']: 
                    newData = deletePost(postIdentificator, targetInfo, newData)
                    print ("Ata apagada com sucesso!")
                    selectedOption = input(selectiveMenu)
                else: 
                    selectedOption == '5'
        elif selectedOption == '0':
            if data != newData:
                save = input('''As alterações feitas à database não foram devidamente guardadas. Deseja guardar as alterações antes de sair?
                             (1) Guardar alterações e Sair
                             (2) Sair sem guardar alterações
                             (3) Voltar ao menu''')
                if save == '1':
                    stop = True 
                    saveFile(newData, 'ata_medica_papers.json')
                    print('Alterações guardadas!')
                elif save == '2':
                    stop = True
                else:
                    selectedOption 
            else:
                stop = True
    print('Obrigado, volte sempre!')
menu()