# Generated by Django 4.2.5 on 2023-09-12 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usipav', '0002_rename_pagina_registroacesso_pagina_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sobrenome', models.CharField(default='SOME STRING', max_length=140)),
                ('cpf', models.PositiveIntegerField(default=0)),
                ('nome', models.CharField(default='SOME STRING', max_length=140)),
                ('verify_nome', models.CharField(default='SOME STRING', max_length=140)),
            ],
        ),
    ]