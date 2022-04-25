from re import A
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    s=''' <h2> Navigation Bar </h2> <br>
    <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> News </a> <br>
    <a href="https://www.google.com/"> Google </a> <br>'''

    params = {'name':"Shahmeer" , 'place':"USE"}
    return render(request,'index.html', params)
# <a href="kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format/code?resource=download"> Kaggle </a>

def index2(request):
    return render (request, "index2.html")


def about(request):
    return HttpResponse("This is About")


def analyze(request):
    djtext= (request.GET.get('text', 'default'))
    print(djtext)
    removepunc = request.GET.get("removepunc", "off")
    fullCap = request.GET.get("fullcap", "off")
    newLineRemover = request.GET.get("newlineremover", "off")
    spaceRemover = request.GET.get("spaceremover", "off")
    analyzed = ""
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
    if fullCap == "on":
        if analyzed == "":
            analyzed = djtext.upper()
        else:
            analyzed = analyzed.upper()
  
    if newLineRemover == "on":
        if analyzed == "":
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
                else:
                    analyzed = analyzed + " "
        else:
            newLineVar = ""
            for char in analyzed:
                if char != "\n" and char != "\r":
                    newLineVar = newLineVar + char
                else: 
                    analyzed = analyzed + " "
            analyzed = newLineVar
    if spaceRemover == "on":
        if analyzed == "":
            for char in djtext:

                if not char  == " ":
                    analyzed = analyzed +char
        else: 
            for char in analyzed:
                if not char  == " ":
                    analyzed = analyzed +char

    if removepunc == "off" and newLineRemover == "off" and fullCap == "off" and spaceRemover == "off":
        return HttpResponse("ERROR")
    
    params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
    print(analyzed)
    return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("ERROR ")


    




# def removepunc(request):
#     djtext= (request.GET.get('text', 'default'))
#     print(djtext)
#     backButton= '''
#     <h1>Remove Punctuations</h1>
#     <a href="http://127.0.0.1:8000/charcount"><button>Go Backk</button></a>
#     '''
#     return HttpResponse(backButton)


# def capfirst(request):
#     return HttpResponse("Capitalize First")


# def newlineremove(request):
#     return HttpResponse("Newline")


# def spaceremove(request):
#     return HttpResponse("Space")


# def charcount(request):
#     return HttpResponse("Char count")