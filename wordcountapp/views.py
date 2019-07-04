from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html') 

def result(request):
    text=request.GET['textarea']
    words=text.split()
    dic={}
    for word in words:
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1

    return render(request,'result.html',{'fulltext':text,'textlength':len(words),'dictionary':dic.items()})
