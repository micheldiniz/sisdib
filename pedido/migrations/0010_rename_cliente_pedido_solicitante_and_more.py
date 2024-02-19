# Generated by Django 5.0.1 on 2024-02-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0009_remove_itempedido_material_content_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='cliente',
            new_name='solicitante',
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado_do_pedido',
            field=models.CharField(choices=[('novo', 'novo'), ('processado', 'processado'), ('enviado', 'enviado'), ('finalizado', 'finalizado'), ('pendente', 'pendente')], default='novo', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='observacao',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
