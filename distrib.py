def countKeysAuthors (authors):
    listAuthors = list(authors)
    nameCount = 0
    affiliationCount = 0
    for author in listAuthors:
        if 'name' in author:
            nameCount+=1
        if 'affiliation' in author:
            affiliationCount+=1
    return (nameCount, affiliationCount)
    
def countKeys (dataset):
    counter = {}
    postsCounter = 0
    counter['name'] = 0
    counter['affiliation'] = 0
    for post in dataset:
        listPost = list(post.items())
        for key,value in listPost:
            if key == 'authors':
                counter['name'] += countKeysAuthors(value)[0]
                counter['affiliation'] += countKeysAuthors(value)[1]
            if key in counter:
                counter[key]+=1
            else:
                counter[key] = 1
        postsCounter+=1
    counter['postsCounter'] = postsCounter
    return counter
             
#{'name': 16408, 'affiliation': 9357, 
# 'abstract': 3595, 'keywords': 1017, 
# 'authors': 3595, 'doi': 3595, 'pdf': 3533, 
# 'publish_date': 1430, 'title': 3595, 
# 'url': 3595, 
# 'postsCounter': 3595}

#obrigatorios : abstract, authors, doi, pdf, title, url, name
#nobrigatorios: keywords, publish_date, affiliation
        
