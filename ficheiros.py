import json
import matplotlib.pyplot

#loading do ficheiro para o sistema
def loadFile (fname):
    data = []
    try:
        with open(fname, 'r', encoding ='utf-8') as file:
            data = json.load(file)
            file.close()
    except Exception as e:
        print('Houve um erro a carregar o ficheiro.')
    return data
    
#   ensure_ascii para evitaar que caraacteres especiais fiquem em ascii
# indent = 4 para espaçamento entre elementos da lista/dicionario
def saveFile (data, fname):
    file = open (fname, 'w', encoding='utf-8')
    json.dump(data, file, ensure_ascii=False, indent = 4)
    file.close()

#inserirNovo(dataset)
#ideia é colocar os inputos para o utilizador meter os campos da ata.´
#pergunta individualmente?? ou so uma vez e o user poe tudo numa linha?
def insertNew (dataset):
    ata = {}
    ata['abstract'] = input('Qual o abstract da nova ata?')
    if input('Deseja adicionar keywords?s/n') == 's': ata['keywords'] = input('Que keywords deseja adicionar à ata?')
    nrAuthors = input('Quantos autores contribuiram para esta ata?')
    while not nrAuthors.isnumeric() or int(nrAuthors)<=0:
        nrAuthors= input('É necessário adicionar pelo menos um autor. Por favor, tente outra vez. Quantos autores contribuiram para esta data?')
    nrAuthors = int(nrAuthors)
    i = 1
    ata['authors'] = []
    while i<=nrAuthors:
        author = {}
        author['name'] = input(f'Qual o nome do autor número {i}?')
        if input('Deseja adicionar uma afiliação para este autor?s/n') == 's': author['affiliation'] = input('Qual a afilição deste autor?')
        ata['authors'].append(author)
        i +=1
    ata['doi'] = input('Qual o doi desta ata?')
    ata['pdf'] = input('Qual o link do pdf desta ata?')
    if input('Deseja adicionar uma data de publicação?s/n') == 's':
        date =  input('Qual a data de publicação desta ata?')
        while not isDate(date):
            date = input('O formato da data está incorreto, por favor submita a mesma no formato AAAA-MM-DD.')
        ata['publish_date'] = date
    ata['title'] = input('Qual o título desta ata?')
    ata['url'] = input('Qual o url desta ata?')

    dataset.append(ata)
    return dataset


def keyIdentificator (selected_option):
    if selected_option == '1':
        return 'abstract'
    elif selected_option == '2':
        return 'authors' #assumir que é pelo nome
    elif selected_option == '3':
        return 'doi'
    elif selected_option == '4':
        return 'pdf'
    elif selected_option == '5':
        return 'publish_date'
    elif selected_option == '6':
        return 'title'
    elif selected_option == '7':
        return 'url'
    else:
        print('Opção não suportada.')
    

#verifica se o year é bissexto
def isLeapYear (year, day):
    if year%4 == 0 and year%100 !=0:
        if day<30:
            return True
    elif day <29:
        return True
    return False

#confirma se o day bate certo para cada month 
def checkMonth (year, month, day):
    if month in [1,3,5,7,8,10,12]:
        if day< 32:
            return True
    elif month in [4,6,9,11]:
        if day< 31:
            return True
    elif month == 2:
            return isLeapYear(year, day)
    return False

def splitDate(date):
    newDate = date.split('-')
    splitDate = (0,0,0)
    if len(newDate)==3:
        concatenatedDate = newDate[0] + newDate[1] + newDate[2]
        if concatenatedDate.isnumeric(): 
           splitDate = (int(newDate[0]), int(newDate[1]), int(newDate[2]))
    return splitDate
            
    
#verifica o formato da data
def isDate (date):
    (year, month, day) = splitDate(date)
    isFormatValid = False
    if (year, month, day) != (0,0,0):
            if (day>0 and day<32) and (year <2025 and year>1900):
                isFormatValid = checkMonth(year, month, day)
    return isFormatValid 

#verifica se autor existe numa ata
def doesAuthorExist (author, post):
    authorExists = False
    authorsList = post['authors']
    i = 0 
    while i<len(authorsList) and not authorExists:
        if author == authorsList[i]['name']:
            authorExists =  True # tem que existir stop para o ciclo parar assim que encontrar o autor
        else:
            i +=1
    return authorExists 


#perguntar qual e a forma de apagar o ficheiro
def deletePost (key, targetInfo, dataset):
    selectedOption = keyIdentificator(key)
    newDataset = [] #novo data set para mover as atas
    if selectedOption in ['abstract', 'doi', 'pdf', 'title', 'url']:
        for post in dataset:
            if targetInfo != post[selectedOption]:
                newDataset.append(post)
    elif selectedOption == 'publish_date':
       if isDate(targetInfo):
           for post in dataset:
               if targetInfo != post[selectedOption]:
                newDataset.append(post)
    elif selectedOption == 'authors':# stop
        for post in dataset:
            if not doesAuthorExist(targetInfo,post):
                newDataset.append(post)    
    if newDataset == dataset: print('Não conseguimos encontrar uma ata com esta informação.')
    return newDataset


def existingKeys (post):
    postKeys = []
    if 'abstract' in post:
        postKeys.append('abstract')
    if 'keywords' in post:
        postKeys.append('keywords')
    if 'authors' in post:
        postKeys.append('authors')
    if 'doi' in post:
        postKeys.append('doi')
    if 'title' in post:
        postKeys.append('title')
    if 'url' in post:
        postKeys.append('url')

    return postKeys

#formata as atas    
def formatPost (post, full = True):
    formattedPost = ""
    formattedKeywords = ""
    formattedDate = ""
    formattedAbstract = f"Abstract: {post['abstract']}\n"
    if 'keywords' in post: formattedKeywords = f"Keywords: {post['keywords']}\n"
    formattedAuthors = "Authors:\n"
    for author in post['authors']:
        formattedAuthors += f"Name: {author['name']}\n"
        if 'affiliation' in author: formattedAuthors += f"Affiliation: {author['affiliation']}\n"
    if 'publish_date' in post: formattedDate = f"Publish Date: {post['publish_date']}\n"      
    formattedDoi = f"Doi: {post['doi']}\n"
    formattedTitle = f"Title: {post['title']}\n"
    formattedURL = f"URL: {post['url']}"
    
    if not full: 
        formattedPost = formattedTitle + formattedKeywords + formattedDate + formattedAuthors
    else:
        formattedPost += formattedAbstract + formattedKeywords + formattedAuthors 
        formattedPost += formattedDate + formattedDoi + formattedTitle + formattedURL
    return formattedPost


def findPost (key, info, dataset):
    selectedOption = keyIdentificator(key)
    postFound = ""
    i = 0
    found=False
    while i<len(dataset) and found == False:
        if dataset[i][selectedOption] == info:
            postFound = dataset[i]
            found = True
            i +=1
    return formatPost(postFound)


#listar os campos mais importantes
def listPosts (dataset):
    listedPosts = ""
    i = 1
    for post in dataset:
        listedPosts += f'Post {i}\n' + formatPost(post, False)
        i +=1
    return listedPosts

def listAuthors (dataset):
    postsAuthor = {}
    for post in dataset:
        for author in post['authors']:
            if author['name'] in postsAuthor:
                postsAuthor[author['name']].append(post['title'])
            else:
                postsAuthor[author['name']] = [post['title']]
    postsAuthor = dict(sorted(postsAuthor.items(), key= lambda x: x[0])) #acentos vao p fim
    return postsAuthor


#distrib
#Distribuição de publicações por ano
def postsPerYear (dataset):
    postsYear = {}
    for post in dataset:
        if 'publish_date' in post:
            if isDate(post['publish_date']):
                year = str(splitDate(post['publish_date'])[0])
                if year in postsYear:
                    postsYear[year]+=1
                else:
                    postsYear[year] = 1
    sortedPostsYear = dict(sorted(postsYear.items(), key = lambda item: item[0]))
    matplotlib.pyplot.bar(sortedPostsYear.keys(),sortedPostsYear.values())
    matplotlib.pyplot.xticks(rotation=45)
    matplotlib.pyplot.show()
    return sortedPostsYear

