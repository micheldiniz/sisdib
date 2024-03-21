# Generated by Django 4.2.11 on 2024-03-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0004_remove_materialbraille_material_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name_plural': 'Materiais'},
        ),
        migrations.AlterModelOptions(
            name='materialadaptado',
            options={'verbose_name_plural': 'Materiais Adaptados'},
        ),
        migrations.AddField(
            model_name='material',
            name='autor',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='edicao',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='editora',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='classificacao',
            field=models.CharField(choices=[('didático', 'didático'), ('paradidático', 'paradidático'), ('revista', 'revista'), ('DAL (S/Revisão)', 'DAL (S/Revisão)'), ('Outro', 'Outro')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='titulo',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
