# Generated by Django 5.0.1 on 2024-02-19 20:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_rename_cliente_assinatura_solicitante'),
    ]

    operations = [
        migrations.AddField(
            model_name='assinatura',
            name='data_registro',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assinatura',
            name='data_ultima_alteracao',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
