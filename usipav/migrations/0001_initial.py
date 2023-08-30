# Generated by Django 4.2.4 on 2023-08-29 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('url', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroAcesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.CharField(default='SOME STRING', max_length=140)),
                ('date', models.DateField()),
                ('Pagina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usipav.pagina')),
            ],
        ),
        migrations.AddField(
            model_name='pagina',
            name='Topico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usipav.topico'),
        ),
    ]