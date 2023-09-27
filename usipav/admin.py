from django.contrib import admin
from .models import Topico,Pagina,RegistroAcesso,Pessoa

admin.site.register(Topico)
admin.site.register(Pagina)
admin.site.register(RegistroAcesso)
admin.site.register(Pessoa)

# Classe de personalização do modelo
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'verify_nome')
    list_filter = ('cpf',)
    search_fields = ('nome', 'sobrenome', 'cpf')
    ordering = ('nome',)

# Desregistra o modelo existente
admin.site.unregister(Pessoa)

# Registra o modelo com a personalização
admin.site.register(Pessoa, PessoaAdmin)
