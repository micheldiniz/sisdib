# Generated by Django 4.2.13 on 2024-07-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0006_classificacao_alter_material_classificacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='ano_publicacao',
            field=models.CharField(blank=True, null=True),
        ),
    ]
