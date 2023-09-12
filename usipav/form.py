from django import forms
from django.core import validators
from .models import Pessoa

class NameForm(forms.Form):
    nome = forms.CharField(label="Your name", max_length=100)
    sobrenome = forms.CharField(label="Your sobrenome", max_length=100)
    cpf = forms.CharField(label="Your cpf", max_length=100)
    descricao = forms.CharField(label="Your descrição", max_length=100)
    botcacher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
      
    verify_nome = forms.CharField(label="enter you nome again: ")

    def clean(self):
        all_clean_data = super().clean()
        nome = all_clean_data["nome"]
        verify_nome = all_clean_data["verify_nome"]

        if nome != verify_nome:
            raise forms.ValidationError("MAKE SURE NOME SOBRENOME MATCH!")


    def clean_botcatcher(self):
        botcatcher = self.cleaned_data["botcatcher"]
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT")
        
        return botcatcher
#def check_forz(value):
#   if value[0].lower() != "z":
#        raise forms.ValidationError("NAME NEEDS TO START WITH Z")


class MyNewForm(forms.ModelForm):
    #FORM FIELD GO HERE
    class Meta:
        model = Pessoa
        fields = "__all__"


