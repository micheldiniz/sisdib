# Generated by Django 4.2.11 on 2024-03-21 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0007_alter_material_quantidade_paginas'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='publico_alvo',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Público alvo'),
        ),
    ]