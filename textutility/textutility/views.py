from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    return render(request, 'index.html')


def analyze(request):
    gettext = request.POST.get('text','default')
    remvpunc = request.POST.get('remvpunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    countchar = request.POST.get('countchar', 'off')
    countwords = request.POST.get('countwords', 'off')
    newlineremover = request.POST.get('newlineremover','off') 
    
    if remvpunc == 'on':
        punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed_text = ''
        for char in gettext:
            if char not in punc:
                analyzed_text = analyzed_text+char
        params={'purpose':'removing punctuation', 'result':analyzed_text}
        return render(request, 'analyzed.html', params)
    
    if uppercase == 'on':
        analyzed_text = ''
        for char in gettext:
            analyzed_text = analyzed_text+ char.upper()
        params={'purpose':'uppercase conversion', 'result':analyzed_text}
        return render(request, 'analyzed.html', params)
    
    if lowercase == 'on':
        analyzed_text = ''
        for char in gettext:
            analyzed_text = analyzed_text+char.lower()
        params={'purpose':'lowercase conversion', 'result':analyzed_text}
        return render(request, 'analyzed.html', params)

    if countchar == 'on':
        analyzed_text = len(gettext)
        params={'purpose':'counting number of char', 'result':analyzed_text}
        return render(request, 'analyzed.html', params)

    if countwords == 'on':
        # punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        words = re.sub(' +|\n',' ',gettext)
        numbwords = str(len(words.rstrip().split(' ')))
        params={'purpose':'counting number of words', 'result':numbwords}
        return render(request, 'analyzed.html', params)

    if newlineremover == 'on':
        # punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed_text = ''
        for char in gettext:
            if char != '\n' and char != '\r':
                analyzed_text = analyzed_text + char
        params={'purpose':'counting number of words', 'result':analyzed_text}
        return render(request, 'analyzed.html', params)

    return HttpResponse('Error')

def navigation(request):
    sites = ['''For Entertainment...<a href = "https://www.youtube.com" >youtube video</a>''',
             '''For Interaction...<a href = "https://www.facebook.com" >Facebook</a>''',
             '''For Insight...<a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''For Internship...<a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))

def about(request):
    return HttpResponse("<h2>About Us</h2>")