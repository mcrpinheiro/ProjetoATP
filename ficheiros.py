import json

#loading do ficheiro para o sistema
def carregarFicheiro (fnome):
    file = open(fnome, 'r', encoding ='utf-8')
    data = json.load(file)
    file.close()
    return data
    
#   ensure_ascii para evitaar que caraacteres especiais fiquem em ascii
# indent = 4 para espaçamento entre elementos da lista/dicionario
def guardarFicheiro (data, ficheiro):
    file = open (ficheiro, 'w', encoding='utf-8')
    json.dump(data, file, ensure_ascii=False, indent = 4)
    file.close()

#inserirNovo(ata, dataset)
#ideia é colocar os inputos para o utilizador meter os campos da ata.´
#pergunta individualmente?? ou so uma vez e o user poe tudo numa linha?
def inserirNovo (ata, dataset):
    dataset.append(ata)
    return dataset


def identificadorAta (opcaosel):
    if opcaosel == '1':
        return 'abstract'
    elif opcaosel == '2':
        return 'authors' #assumir que é pelo nome
    elif opcaosel == '3':
        return 'doi'
    elif opcaosel == '4':
        return 'pdf'
    elif opcaosel == '5':
        return 'publish_date'
    elif opcaosel == '6':
        return 'title'
    elif opcaosel == '7':
        return 'url'
    else:
        print('Opção não suportada.')
    
#perguntar qual e a forma de apagar o ficheiro
def apagarPub (campo, infoata, dataset):
    opcao_selecionada = identificadorAta(campo)
    novo_dataset = [] #novo data set para mover as atas
    if opcao_selecionada in ['abstract', 'doi', 'pdf', 'title', 'url']:
        for ata in dataset:
            if infoata != ata[opcao_selecionada]:
                novo_dataset.append(ata)
    #elif opcao_selecionada == 'publish_date':
        #verificar o formato da data
    elif opcao_selecionada == 'authors':# stop
        for ata in dataset:
            lista_autores = ata['authors']
            autorExiste =  False
            i = 0 
            while i<len(lista_autores) and autorExiste == False:
                if infoata == lista_autores[i]['name']:
                    autorExiste =  True # tem que exist stop para o ciclo parar assim que encontrar o autor
                else:
                    i +=1
            if not autorExiste:
                novo_dataset.append(ata)     
    if novo_dataset == dataset: print('Não conseguimos encontrar uma ata com esta informação.')
    return novo_dataset


