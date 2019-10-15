"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
import operator

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'سیستم مدیریت خیریه',
            'company':'شرکت داده پردازی کلیک',
            'year':datetime.now().year,
            
        }
    )

def word(request):
    return render(request, 'app/home.html')

def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext) 
      
       
    worddictionary={}
    for word in fulltext.split():
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    sortedwords = sorted(worddictionary.items(),key=operator.itemgetter(1))

    return render(request, 'app/count.html',{'fulltext':fulltext,
                                             'count':len(worddictionary),
                                             'sortedwords':sortedwords,})


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
