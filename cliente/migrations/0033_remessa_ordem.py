# Generated by Django 4.2.11 on 2024-05-06 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0032_tiporemessa_remove_remessa_tipo_remessa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='remessa',
            name='ordem',
            field=models.CharField(blank=True, max_length=255, verbose_name='ordem'),
        ),
    ]
