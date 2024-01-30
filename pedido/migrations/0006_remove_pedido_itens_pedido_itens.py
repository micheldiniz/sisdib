# Generated by Django 5.0.1 on 2024-01-30 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0005_rename_items_pedido_itens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='itens',
        ),
        migrations.AddField(
            model_name='pedido',
            name='itens',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pedido.item'),
            preserve_default=False,
        ),
    ]
