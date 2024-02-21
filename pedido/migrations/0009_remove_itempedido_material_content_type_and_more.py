# Generated by Django 5.0.1 on 2024-02-19 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0004_remove_materialbraille_material_and_more'),
        ('pedido', '0008_remove_pedido_itens_pedido_numero_pedido_itempedido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itempedido',
            name='material_content_type',
        ),
        migrations.RemoveField(
            model_name='itempedido',
            name='material_object_id',
        ),
        migrations.AddField(
            model_name='itempedido',
            name='material',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='material.materialadaptado'),
            preserve_default=False,
        ),
    ]