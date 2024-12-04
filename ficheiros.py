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


def identificarAta (info, dataset):
    if info == '1':
        return 'nam'
    return 
#perguntar qual e a forma de apagar o ficheiro
def apagarPub (ata, dataset):

    return dataset

print(carregarFicheiro('ata_medica_papers.json'))
