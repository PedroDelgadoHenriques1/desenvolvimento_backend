from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!!!")

def calculadora(request):
    return render(request, 'calculadora.html') 

def londrina(request):
    return render(request, 'harrypotter.html') 

def filmes(request):
    return render(request, 'filmes.html')

def form(request):
    return render(request, 'form.html')

