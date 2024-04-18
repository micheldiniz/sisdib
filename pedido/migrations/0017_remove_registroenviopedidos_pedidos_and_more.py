# Generated by Django 5.0.1 on 2024-04-18 21:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0016_registroenviopedidos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registroenviopedidos',
            name='pedidos',
        ),
        migrations.AddField(
            model_name='pedido',
            name='registro_envio',
            field=models.ForeignKey(blank=True, limit_choices_to={'estado_do_pedido': 'novo'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedido.registroenviopedidos'),
        ),
    ]
