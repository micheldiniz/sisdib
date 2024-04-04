# Generated by Django 4.2.11 on 2024-04-04 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0014_alter_material_arquivo_original_and_more'),
        ('cliente', '0015_alter_assinatura_observacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assinatura',
            name='estado',
            field=models.CharField(choices=[('vigente', 'vigente'), ('cancelado', 'cancelado')], default='vigente', max_length=255),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.materialadaptado'),
        ),
    ]
