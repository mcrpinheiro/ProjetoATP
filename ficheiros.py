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

