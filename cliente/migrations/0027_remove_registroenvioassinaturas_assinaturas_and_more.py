# Generated by Django 4.2.11 on 2024-05-02 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0026_registroenvioassinaturas_nome_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registroenvioassinaturas',
            name='assinaturas',
        ),
        migrations.RemoveField(
            model_name='registroenvioassinaturas',
            name='descricao',
        ),
    ]
