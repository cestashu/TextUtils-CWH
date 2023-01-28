from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request. POST.get('removepunc', 'off')
    fullcaps = request. POST.get('fullcaps', 'off')
    newlineremover = request. POST.get('newlineremover', 'off')
    extraspaceremover = request. POST.get('extraspaceremover', 'off')
    charcount = request. POST.get('charcount', 'off')

    if removepunc == "on":
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed  = ""
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
        params = {'purpose':'Removing Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changing it to UpperText', 'analyzed_text':analyzed}
        djtext = analyzed
    
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Removing New Lines', 'analyzed_text':analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]== " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Removing Extra Spaces', 'analyzed_text':analyzed}
        djtext = analyzed
            
    if(charcount == "on"):
        analyzed = 0
        for i in range(0, len(djtext)):
            if(djtext[i] != ' '):
                analyzed = analyzed + 1;  

        params = {'purpose':'Counting the Number of Characters in the given input is', 'analyzed_text':analyzed}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Please Select any one operation and try again.")
    return render(request, 'analyzer.html',params)    
     

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact-us.html')

