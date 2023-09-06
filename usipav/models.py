from django.db import models

class Topico(models.Model):
    name = models.CharField(max_length=264, unique=True)
    
    
    def __str__(self):
        return self.name
    
class Pagina(models.Model):
    name = models.CharField(max_length=264, unique=True)
    Topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    
    
    def __str__(self):
        return str(self.name)


class RegistroAcesso(models.Model):
    registro = models.CharField(max_length=140, default='SOME STRING')
    data_acesso = models.DateField()
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.data_acesso)

class Form(models.Model):
    nome = models.CharField(max_length=140, default='SOME STRING')
    sobrenome = models.CharField(max_length=140, default='SOME STRING')
    cpf = models.NumberField(max_length=140, default='SOME STRING')
    nome = models.CharField(max_length=140, default='SOME STRING')
    verify_nome =  models.CharField(max_length=140, default='SOME STRING')
    
    
    def __str__(self):
        return str(self.data_acesso)