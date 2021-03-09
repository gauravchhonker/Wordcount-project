from django.shortcuts import render
import operator

def homepage(request):
    return render( request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    mytext = request.GET['fulltext']
    wordlist = mytext.split(); 
    
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortwords = sorted(worddictionary.items() , key= operator.itemgetter(1) , reverse=True)

    return render( request, 'count.html' , { 'mytext': mytext, 'count': len(wordlist), 'sortwords': sortwords})