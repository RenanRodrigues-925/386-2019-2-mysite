# Generated by Django 2.2.2 on 2019-09-10 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricaoProduto', models.CharField(max_length=200)),
                ('unidadeCompra', models.CharField(max_length=50)),
                ('qtdPrevistoMes', models.IntegerField()),
                ('preco', models.IntegerField()),
                ('precoMaximo', models.IntegerField()),
            ],
        ),
    ]
