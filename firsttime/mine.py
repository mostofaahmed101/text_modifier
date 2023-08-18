#M it's a manual file -ME

from django.http import HttpResponse
from django.shortcuts import render
import re

def func1(request):
    para = {"name":"bigboss", "age":"10"}
    return render(request, "index.html", para)    # setup html with django


def func2(request):
    text = request.POST.get("Text", "None")
    Punc = request.POST.get("chkpunc", "off")
    RmNL = request.POST.get("rmnewline", "off")
    RmS = request.POST.get("rmspace", "off")
    RmES = request.POST.get("rmexspace", "off")
    Upper = request.POST.get("uppercase", "off")
    ChCount = request.POST.get("chcount", "off")
    print(text)
    print(Punc)
    
    analyze = []
    if Punc == "on":
        newtext = ''
        analyse = 'Remove Punctuation'
        knownPunc = '''!@#~`$%^&*(){}[]:;"'|\<>?/'''
        for char in text:
            if char not in knownPunc:
                newtext += char
        text = newtext
        analyze.append(analyse)
    
    if RmS == "on":
        analyse = 'Remove All Space'
        newtext = text.split(" ")
        newtext = "".join(newtext)
        text = newtext
        analyze.append(analyse)
    
    if RmES == "on":
        analyse = 'Remove Extra Space'
        newtext = ""
        for i in range(len(text)):
            if text[i] == ' ' and text[i-1] == ' ':
                pass
            else:
                newtext += text[i]
        text = newtext
        analyze.append(analyse)

    if Upper == "on":
        newtext = text.upper()
        analyse = 'FULL UPPERCASE'
        text = newtext
        analyze.append(analyse)
    
    if RmNL == "on":
        analyse = 'Remove New Line'
        newtext = ''
        for i in text:
            if i != '\n' and i != '\r':
                newtext += i
        text = newtext
        analyze.append(analyse)
        
    if ChCount == "on":
        newtext = text.split(" ")
        newtext = "".join(newtext)
        text = text + "\n\n Number of Character in your Text : "+ str(len(newtext))
        analyse = 'Character Count'
        analyze.append(analyse)

    if len(analyze) == 1:
        analyze = analyze[0]
    elif len(analyze) > 1:
        analyze = ", ".join(analyze)
    else:
        analyze = "None"
        
    para = {"analyse":analyze, "newtext":text}
    return render(request, "analysis.html", para)