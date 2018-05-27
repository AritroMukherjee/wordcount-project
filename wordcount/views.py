from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    #return HttpResponse('Hello World!')
    #return render (request,'homepage.html',{'hithere':'this is me'})
    #passing a dictionary easily
    return render (request,'homepage.html')

def count(request):

    fulltext = request.GET['fulltext'].lower()

    wordlist = fulltext.split()
    #splits the message into respective words
    count = len(wordlist)
    #count the number of words in the message

    #create a new dictionary
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1 #increase the counter
        else:
            #add the word to the dictionary,
            #by passing the word as a key into the dictionary
            worddictionary[word] = 1
    #                                        search on the operator, look at the values (starting from 1)and sort it in the reverse order, word with the highest count will be displayed first
    sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':count,'sortedwords':sortedwords})
    #.items ta use kora hoeche to turn the values into lists



def about(request):
    return render(request,'about.html')
