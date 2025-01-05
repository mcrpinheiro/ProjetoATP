import json
import matplotlib.pyplot
from check_date import *


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
    

def saveFile (data, fname):
    file = open (fname, 'w', encoding='utf-8')
    json.dump(data, file, ensure_ascii=False, indent = 4)
    file.close()


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


def askForNonEmptyAnswer (questionText, failedQuestionText):
    answer = input(questionText)
    while answer == "":
        answer = input(failedQuestionText)
    return answer
    
def insertNew (dataset):
    post = {}
    post['abstract'] = askForNonEmptyAnswer('Qual o abstract da nova publicação?', 'Por favor insira um abstract para adicionar à publicação.')
    if input('Deseja adicionar keywords?s/n') == 's':
        post['keywords'] = askForNonEmptyAnswer('Que keywords deseja adicionar à publicação?', 'Por favor insira keywords para adicionar à publicação.')
    nrAuthors = input('Quantos autores contribuiram para esta publicação? É possível adicionar até 10 autores.')
    while not nrAuthors.isnumeric() or int(nrAuthors)<=0 or int(nrAuthors)>10:
        nrAuthors= input('É necessário adicionar pelo menos um autor. Por favor, tente outra vez. Quantos autores contribuiram para esta publicação? É possível adicionar até 10 autores.')
    nrAuthors = int(nrAuthors)
    i = 1
    post['authors'] = []
    while i<=nrAuthors:
        author = {}
        author['name'] = askForNonEmptyAnswer(f'Qual o nome do autor número {i}?', f'Por favor insira o nome do autor {i}')
        if input('Deseja adicionar uma afiliação para este autor?s/n') == 's': 
            author['affiliation'] = askForNonEmptyAnswer('Qual a afiliação deste autor?', 'Por favor insira uma afiliação para este autor.')
        post['authors'].append(author)
        i +=1
    post['doi'] = askForNonEmptyAnswer('Qual o doi da nova publicação?', 'Por favor insira um doi para adicionar à publicação.')
    if input('Deseja adicionar pdf?s/n') == 's': 
        post['pdf'] = askForNonEmptyAnswer('Qual o pdf da nova publicação?', 'Por favor insira um pdf para adicionar à publicação.')
    if input('Deseja adicionar uma data de publicação?s/n') == 's':
        date =  input('Qual a data de publicação desta publicação')
        while not isDate(date):
            date = input('O formato da data está incorreto, por favor submita a mesma no formato AAAA-MM-DD.')
        post['publish_date'] = date
    post['title'] = askForNonEmptyAnswer('Qual o título da nova publicação?', 'Por favor insira um título para adicionar à publicação.')
    post['url'] = askForNonEmptyAnswer('Qual o url da nova publicação?', 'Por favor insira um url para adicionar à publicação.')

    dataset.append(post)
    return dataset


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
    if newDataset == dataset: print('Não conseguimos encontrar uma pubalicação com esta informação.')
    return newDataset

  
def formatPost (post, full = True):
    formattedPost = ""
    formattedKeywords = ""
    formattedDate = ""
    formattedPDF = ""
    formattedAbstract = f"Abstract: {post['abstract']}\n"
    if 'keywords' in post: formattedKeywords = f"Keywords: {post['keywords']}\n"
    formattedAuthors = "Authors:\n"
    for author in post['authors']:
        formattedAuthors += f"Name: {author['name']}\n"
        if 'affiliation' in author: formattedAuthors += f"Affiliation: {author['affiliation']}\n"
    if 'publish_date' in post: formattedDate = f"Publish Date: {post['publish_date']}\n"      
    formattedDoi = f"Doi: {post['doi']}\n"
    if 'pdf' in post: formattedPDF = f"Pdf: {post['pdf']}\n"
    formattedTitle = f"Title: {post['title']}\n"
    formattedURL = f"URL: {post['url']}"
    
    if not full: 
        formattedPost = formattedTitle + formattedKeywords + formattedDate
    else:
        formattedPost += formattedAbstract + formattedKeywords + formattedAuthors 
        formattedPost += formattedDate + formattedDoi + formattedPDF + formattedTitle + formattedURL
    return formattedPost


def findPost (key, info, dataset):
    selectedOption = keyIdentificator(key)
    postFound = ""
    formattedPost = ""
    i = 0
    found=False
    while i<len(dataset) and found == False:
        if selectedOption == 'authors' :
            for author in dataset[i]['authors']:
                if author['name'] == info:
                    found = True
                    postFound = dataset[i]
        elif selectedOption in dataset[i]:
            if dataset[i][selectedOption] == info:
                postFound = dataset[i]
                found = True
        i+=1
    if postFound != "":
        formattedPost = formatPost(postFound)
    return formattedPost


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
    formatAuthors = ""
    for name, titles in postsAuthor.items():
        newAuthor = f'''{name}: '''
        i = 0
        while i<len(titles):
            if titles[i] == titles[len(titles) - 1]:
                newAuthor += f'''{titles[i]}'''
            else:
                newAuthor += f'''{titles[i]}; '''
            i+=1
        formatAuthors += newAuthor + '\n'
    return formatAuthors


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

    listPostsYear = ""
    for currentYear, posts in sortedPostsYear.items():
        listPostsYear += f'{currentYear}: {posts} publicações\n'
    print(listPostsYear)


    matplotlib.pyplot.bar(sortedPostsYear.keys(),sortedPostsYear.values())
    matplotlib.pyplot.xticks(rotation=45)
    matplotlib.pyplot.show()

    return sortedPostsYear

