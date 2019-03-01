from django.shortcuts import render
from django.http import HttpResponse
from . import FileHandler as fh
from . import MyLucene as ML
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.

def index(request):
    '''filepath = "C:/Users/M.S.Shruthi/Desktop/Desktop files/sem_5/InformationRetrieval/project/ir-project/movie"
    totalFiles = 100
    listOfFiles = []
    for i in range(totalFiles):
        listOfFiles.append(filepath+str(i+1)+'.txt')
    WordsList = fh.ListOfWords(listOfFiles)
    WordsList = fh.removeExtraCharacters(WordsList)
    UniqueList = fh.getUniqueTerms(WordsList)
    StopWordFreeUniqueList, WordsListNew = ML.removeStopWords(WordsList, UniqueList,100)
    WordsListNewCopy = WordsListNew
    AfterLemmWordsList, AfterLemmUniqueList = ML.MyLemmatizer(WordsListNew,StopWordFreeUniqueList)
    FinalWords, FinalUnique = ML.Stemmer(AfterLemmWordsList, AfterLemmUniqueList)
    ML.BuildIndex(FinalUnique, FinalWords)'''
    x = ['shruthi', 'mahi', 'harshi']
    template = loader.get_template("App/index.html")
    context = {
	    'list' : x
    }
    return HttpResponse(template.render(context,request))