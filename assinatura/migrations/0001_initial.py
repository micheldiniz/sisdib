# Generated by Django 4.2.13 on 2024-06-06 19:25

import assinatura.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '0001_initial'),
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('vigente', 'vigente'), ('cancelado', 'cancelado')], default='vigente', max_length=255)),
                ('data_registro', models.DateTimeField(auto_now_add=True, verbose_name='Data de registro')),
                ('data_ultima_alteracao', models.DateTimeField(null=True)),
                ('observacao', models.CharField(blank=True, max_length=255, verbose_name='Observação')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.materialadaptado')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroEnvioAssinaturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('enviado', models.BooleanField(default=False, verbose_name='Enviado?')),
                ('remetente', models.CharField(blank=True, default='Instituto Benjamin Constant', max_length=255, verbose_name='Remetente')),
                ('identificacao', models.CharField(blank=True, default='Cecograma', max_length=255, verbose_name='Identificação')),
                ('data_registro', models.DateTimeField(auto_now_add=True, verbose_name='Data de registro')),
                ('observacao', models.CharField(blank=True, max_length=255, verbose_name='Observação')),
            ],
            options={
                'verbose_name_plural': 'Configurar envio de Assinaturas',
            },
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('data_registro', models.DateTimeField(auto_now_add=True, verbose_name='Data de registro')),
                ('is_disponivel_para_assinatura', models.BooleanField(default=False, verbose_name='Disponível para assinatura?')),
            ],
        ),
        migrations.CreateModel(
            name='TipoRemessa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pessoa.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Remessa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_registro', models.DateTimeField(auto_now_add=True, verbose_name='Data de registro')),
                ('data_envio', models.DateField(blank=True, null=True)),
                ('quantidade', models.PositiveIntegerField(blank=True, null=True)),
                ('observacao', models.CharField(blank=True, max_length=255, verbose_name='Observação')),
                ('ordem', models.CharField(blank=True, max_length=255, verbose_name='ordem')),
                ('registro_envio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assinatura.registroenvioassinaturas')),
                ('tipo_remessa', models.ManyToManyField(max_length=255, to='assinatura.tiporemessa')),
            ],
            options={
                'verbose_name': 'Remessa',
                'verbose_name_plural': 'Remessas para Envio (de edições de assinaturas)',
            },
        ),
        migrations.CreateModel(
            name='EdicaoMaterialAssinatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edicao', models.CharField(blank=True, max_length=255, null=True)),
                ('quantidade_paginas', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('peso', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('arquivo_original', models.FileField(blank=True, null=True, upload_to=assinatura.models.get_revista_upload_path)),
                ('quantidade_assinaturas_RJ', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Qtd. ass. Rio de Janeiro (ativas)')),
                ('quantidade_assinaturas_Es', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Qtd. ass. Estrangeiros (ativas)')),
                ('quantidade_assinaturas_OE', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Qtd. ass. Outros Estados (ativas)')),
                ('assinaturas', models.ManyToManyField(limit_choices_to={'estado': 'vigente'}, to='assinatura.assinatura')),
                ('material', models.ForeignKey(blank=True, limit_choices_to={'is_disponivel_para_assinatura': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='material.materialadaptado')),
                ('registro_envio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assinatura.registroenvioassinaturas')),
            ],
            options={
                'verbose_name': 'Edição da Assinatura',
                'verbose_name_plural': 'Edições da Assinatura',
            },
        ),
        migrations.AddField(
            model_name='assinatura',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assinatura.solicitante', verbose_name='Solicitante / Assinante'),
        ),
        migrations.CreateModel(
            name='Assinante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='nome da pessoa que receberá o material')),
                ('assinatura', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assinatura.assinatura')),
            ],
        ),
    ]
