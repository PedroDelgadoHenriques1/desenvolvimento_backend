from django import forms


class NameForm(forms.Form):
    nome = forms.CharField(label="Your name", max_length=100)
    sobrenome = forms.CharField(label="Your name", max_length=100)
    cpf = forms.CharField(label="Your name", max_length=100)
    endereço = forms.CharField(label="Your name", max_length=100)