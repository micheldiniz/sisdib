# Generated by Django 5.0.1 on 2024-02-19 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0008_remove_assinatura_material_content_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assinatura',
            old_name='cliente',
            new_name='solicitante',
        ),
    ]