# Generated by Django 4.2.11 on 2024-03-26 19:31

from django.db import migrations, models
import material.models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0013_alter_materialadaptado_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='arquivo_original',
            field=models.FileField(blank=True, null=True, upload_to=material.models.get_material_upload_path),
        ),
        migrations.AlterField(
            model_name='materialadaptado',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to=material.models.get_material_upload_path),
        ),
    ]
