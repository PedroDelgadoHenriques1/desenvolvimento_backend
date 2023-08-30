import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first.settings')
import django
django.setup()

import random


from usipav.models import Topico,Pagina,RegistroAcesso
from faker import Faker


fakegen = Faker()
todos = ['futebol','cachaça', 'carro']

for i in range(15):
    topico = Topico.objects.get_or_create(name=todos[0])[0]
    pagina = Pagina.objects.get_or_create(name = fakegen.name(), Topico =topico, url = fakegen.url())[0]
    data_acesso = RegistroAcesso.objects.get_or_create(registro = fakegen.name(), data_acesso=fakegen.date(),pagina=pagina)[0]





