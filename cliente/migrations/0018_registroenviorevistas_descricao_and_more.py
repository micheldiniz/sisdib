# Generated by Django 5.0.1 on 2024-04-16 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0017_registroenviorevistas'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroenviorevistas',
            name='descricao',
            field=models.CharField(blank=True, max_length=255, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='registroenviorevistas',
            name='observacao',
            field=models.CharField(blank=True, max_length=255, verbose_name='Observação'),
        ),
    ]