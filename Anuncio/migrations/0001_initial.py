# Generated by Django 2.2.2 on 2019-09-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=50)),
                ('textoTitulo', models.CharField(max_length=200)),
                ('preco', models.PositiveIntegerField()),
                ('textoAnuncio', models.CharField(max_length=150)),
                ('nomeContato', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('secao', models.CharField(max_length=50)),
                ('tipoAnuncio', models.CharField(max_length=150)),
            ],
        ),
    ]
