# Generated by Django 5.0.1 on 2024-01-12 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('nome_contato', models.CharField(max_length=255)),
                ('celular', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=255)),
                ('logradouro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=255)),
                ('complemento', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, null=True)),
                ('contato', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.contato')),
                ('endereco', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=255)),
                ('pessoa', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=255)),
                ('pessoa', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.pessoa')),
            ],
        ),
    ]
