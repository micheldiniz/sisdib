# Generated by Django 4.2.13 on 2024-07-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0004_alter_materialadaptado_is_disponivel_para_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='ano_publicacao',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
