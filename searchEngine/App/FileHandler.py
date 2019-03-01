def ListOfWords(ListOfFiles):
    MyList = []
    iterator = 0
    for i in ListOfFiles:
        f = open(i,encoding="utf8")
        fFull = f.read()
        fLines = list(fFull.split('\n'))
        fWords = []
        for j in fLines:
            fWords = fWords+(list(j.split(' ')))
        #print(fWords)
        MyList.append(fWords)
        f.close()
    return MyList

def removeExtraCharacters(WordsList):
    for i in range(len(WordsList)):
        #WordsList[i] = set(WordsList[i])
        for j in range(len(WordsList[i])):
            temp = list(WordsList[i][j].lower())
            #print(temp)
            if '.' in temp:
                temp.remove('.')
            if ',' in temp:
                temp.remove(',')
            if "'" in temp:
                temp.remove("'")
            if '(' in temp:
                temp.remove('(')
            if ')' in temp:
                temp.remove(')')
            if '[' in temp:
                temp.remove('[')
            if ']' in temp:
                temp.remove(']')
            if ';' in temp:
                temp.remove(';')
            if '"' in temp:
                temp.remove('"')
            if '"' in temp:
                temp.remove('"')
            if ':' in temp:
                if(len(temp)>1):
                    temp.remove(':')
            WordsList[i][j] = ''.join(temp)
        WordsList[i] = set(WordsList[i])
        WordsList[i] = list(WordsList[i])
        WordsList[i].sort()
        if ':' in WordsList[i]:
            WordsList[i].remove(':')
    return WordsList

def getUniqueTerms(WordsList):
    MyList = []
    for i in range(len(WordsList)):
        MyList = MyList + WordsList[i]
    MyList = set(MyList)
    MyList = list(MyList)
    MyList.sort()
    return MyList