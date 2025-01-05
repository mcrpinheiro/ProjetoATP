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

def askForValidDate (questionText, failedQuestionText):
    date = input(questionText)
    while not isDate(date):
        date = input(failedQuestionText)
    return date