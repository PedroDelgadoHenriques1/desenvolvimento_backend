from django.shortcuts import render
from django.http import HttpResponse
from . import form
from django import forms
from .form import MyNewForm


def index(request):
    return HttpResponse("Hello, world!!!")

def calculadora(request):
    return render(request, 'calculadora.html') 

def londrina(request):
    return render(request, 'harrypotter.html') 

def filmes(request):
    return render(request, 'filmes.html')

def _form(request):
    form2 = form.NameForm()
        # Check to see if we get a post back.
    if request.method == "POST":
        # In which case we pass in that request.
        form2 = form.NameForm(request.POST)

        # Check to see form is valid
        if form2.is_valid():
            # Do something.
            print("Form Validation Sucess. Print in console.")
            print("Nome: "+form2.cleaned_data["nome"])
            print("Sobrenome: "+form2.cleaned_data["sobrenome"])
            print("Cpf: "+form2.cleaned_data["cpf"])
            print("Descrição: "+form2.cleaned_data["descricao"])
            print("verificar_nome: "+form2.cleaned_data["verify_nome"])
    return render(request, 'form.html',{"form":form2})

def form_produto(request):
    form = MyNewForm()

    if request.method == "POST":
        form = MyNewForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Vish, deu erro")

    return render(request, "modelform.html", context={"form":form })

def base(request):
    return render(request, 'base.html')

def informacao(request):
    return render(request, 'informacao.html')
