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
                            (6) Relatório de Estatísticas de Publicações por Ano
                            (7) Listar Autores
                            (8) Importar Publicações
                            (9) Guardar Publicações
                            (0) Sair''')
    helpMenu = ('''Bem vindo ao menu de ajuda do sistema. Para executar alguma das opções abaixo, digite o número correspondente à mesma.
                    (2) Criar Publicação: criação de uma nova publicação com informações fornecidas pelo utilizador
                    (3) Consulta de Publicação: consultar as informações detalhadas de uma publicação especificada pelo utilizador
                    (4) Consultar Publicações: lista as informações mais importantes de todas as publicações presentes no sistema 
                    (5) Eliminar Publicação: eliminar uma publicação especificada pelo utilizador
                    (6) Relatório de Estatísticas: gerar estatísticas do número de publicações por ano
                    (7) Listar Autores: lista todos os autores existentes na base de dados fornecida.
                    (8) Importar Publicações: importa uma base de dados de um ficheiro JSON.
                    (9) Guardar Publicações: atualizar a base de dados com novas informações fornecidas
                    (0) Sair: sair do programa''')
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
        if selectedOption not in ['0', '1','2', '3', '4', '5', '6', '7', '8', '9']:
            print('Opção não disponível. Por favor tente outra vez.')
            selectedOption = input(selectiveMenu)
        elif selectedOption in ['3', '4', '5', '6', '7'] and data == []:
            selectedOption = input('''Esta opção não está disponível pois não existem atas em sistema. O que deseja fazer?
                                   (1) Ajuda
                                   (8) Importar Publicações
                                   (0) Sair''')
        elif selectedOption == '1':
            print(helpMenu)
            selectedOption = input('Deseja realizar alguma destas operações?')
        elif selectedOption == '2':
            newData = insertNew(newData)
            print('Publicação adicionada com sucesso!')
            selectedOption = input(selectiveMenu)
        elif selectedOption == '3':
            postIdentificator = input(keyMenu)
            if postIdentificator not in ['0','1', '2', '3', '4', '5', '6', '7']: 
                print('Operação não suportada. Por favor tente outra vez.')
                postIdentificator = input(keyMenu)    
            elif postIdentificator == '0':
                selectedOption = input(selectiveMenu)
            else:
                if keyIdentificator(postIdentificator) == 'publish_date':
                    targetInfo = askForValidDate('Qual data deseja pesquisar?', 'Por favor insira uma data válida no formato AAAA-MM-DD.')
                else:
                    targetInfo = askForNonEmptyAnswer(f'Qual {(keyIdentificator(postIdentificator))} deseja pesquisar?', f'Por favor insira um {(keyIdentificator(postIdentificator))} válido.')
                post = findPost(postIdentificator, targetInfo, newData)
                if post!= "": print(post)
                else: print('Não foi encontrada uma publicação com estes dados.')
                selectedOption = input(selectiveMenu)
        elif selectedOption == '4':
            print(listPosts(newData))
            selectedOption = input(selectiveMenu)
        elif selectedOption == '5':
            postIdentificator = input(keyMenu)
            if postIdentificator not in ['0','1', '2', '3', '4', '5', '6', '7']: 
                print('Operação não suportada. Por favor tente outra vez.')
                postIdentificator = input(keyMenu)    
            elif postIdentificator == '0':
                selectedOption = input(selectiveMenu)
            else:
                if keyIdentificator(postIdentificator) == 'publish_date':
                    targetInfo = askForValidDate('Qual data deseja pesquisar?', 'Por favor insira uma data válida no formato AAAA-MM-DD.')
                else:
                    targetInfo = askForNonEmptyAnswer(f'Qual {(keyIdentificator(postIdentificator))} deseja pesquisar?', f'Por favor insira um {(keyIdentificator(postIdentificator))} válido.')
                confirmDelete = input(f"Deseja apagar a ata com {keyIdentificator(postIdentificator)} correspondente a {targetInfo}? S/N")
                if confirmDelete in ['S', 's']: 
                    if deletePost(postIdentificator, targetInfo, newData) == newData: 
                        print('Não conseguimos encontrar uma pubalicação com esta informação.')
                    else: 
                        newData = deletePost(postIdentificator, targetInfo, newData)
                        print ("Ata apagada com sucesso!")
                    selectedOption = input(selectiveMenu)
                else: 
                    selectedOption = '5'
        elif selectedOption == '6':
            postsPerYear(newData)
            selectedOption = input(selectiveMenu)
        elif selectedOption == '7':
            print(listAuthors(newData))
            selectedOption = input(selectiveMenu)
        elif selectedOption == '8':
            importingMenu = ('''Que operação deseja efetuar?
                            (1) Substituir os dados atuais pelos dados do novo ficheiro
                            (2) Adicionar os dados do ficheiro aos dados em sistema
                            (0) Voltar ao menu''')
            importingOption = input(importingMenu)
            if importingOption not in ['0', '1', '2']:
                print('Operação não suportada. Por favor tente outra vez.')
                importingOption = input(importingMenu)
            elif importingOption == '1':
                fileName = askForNonEmptyAnswer('Qual o nome do ficheiro que deseja importar?', 'Por favor insira um nome de um ficheiro JSON válido.')
                incomingFile = loadFile(fileName)
                if incomingFile != []:
                    newData = incomingFile
                    print('Ficheiro importado com sucesso!')
                selectedOption = input(selectiveMenu)
            elif importingOption == '2':
                fileName = askForNonEmptyAnswer('Qual o nome do ficheiro que deseja importar?', 'Por favor insira um nome de um ficheiro JSON válido.')
                incomingFile = loadFile(fileName)
                if incomingFile != []:
                    newData += incomingFile
                    print('Ficheiro importado com sucesso!')
                selectedOption = input(selectiveMenu)
            else:
                selectedOption = input(selectiveMenu)   
        elif selectedOption == '9':
            save = input('Deseja guardar as alterações feitas? S/N')
            if save in ['s', 'S']:
                saveFile(newData, 'ata_medica_papers.json')
                data = newData
                print('Alterações guardadas com sucesso!')
            selectedOption = input(selectiveMenu)
        elif selectedOption == '0':
            if data != newData:
                saveMenu = ('''As alterações feitas à database não foram devidamente guardadas. Deseja guardar as alterações antes de sair?
                             (1) Guardar alterações e Sair
                             (2) Sair sem guardar alterações
                             (0) Voltar ao menu''')
                save = input(saveMenu)
                if save not in ['0', '1', '2']:
                    print('Opção não suportada. Tente outra vez.')
                    save = input(saveMenu)
                elif save == '1':
                    stop = True 
                    saveFile(newData, 'ata_medica_papers.json')
                    print('Alterações guardadas!')
                elif save == '2':
                    stop = True
                elif save == '0':
                    selectedOption = input(selectiveMenu)
            else:
                stop = True
    print('Obrigado, volte sempre!')
menu()