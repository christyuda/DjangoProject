from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context = {
        'Judul' : 'blog1',
        'h1': 'Django'
    }
    return render(request,'wiw.html',context)

def recent(request):
    context = {
        'Judul' : 'blog2',
        'h1' : 'Python'
    } 
    return render (request,'blog/wiw.html', context)



def article(request, year):
    return HttpResponse(f"{year}")
