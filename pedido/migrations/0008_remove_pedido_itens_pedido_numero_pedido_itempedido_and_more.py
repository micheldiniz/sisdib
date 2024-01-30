# Generated by Django 5.0.1 on 2024-01-30 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('pedido', '0007_remove_pedido_itens_pedido_itens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='itens',
        ),
        migrations.AddField(
            model_name='pedido',
            name='numero_pedido',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('material_object_id', models.IntegerField()),
                ('estado', models.CharField(choices=[('aceito', 'aceito'), ('indisponivel', 'indisponivel'), ('pendente', 'pendente')], max_length=255)),
                ('observacao', models.CharField(max_length=255)),
                ('material_content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.contenttype')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
