# Generated by Django 4.2.13 on 2024-06-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0003_alter_materialadaptado_is_disponivel_para_pedido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialadaptado',
            name='is_disponivel_para_pedido',
            field=models.BooleanField(default=False, verbose_name='Disponível para pedido?'),
        ),
    ]
