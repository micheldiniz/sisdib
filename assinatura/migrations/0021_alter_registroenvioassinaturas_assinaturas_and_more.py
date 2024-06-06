# Generated by Django 5.0.1 on 2024-04-18 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assinatura', '0020_rename_registroenviorevistas_registroenvioassinaturas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroenvioassinaturas',
            name='assinaturas',
            field=models.ManyToManyField(limit_choices_to={'estado': 'vigente'}, to='assinatura.assinatura'),
        ),
        migrations.AlterField(
            model_name='registroenvioassinaturas',
            name='data_registro',
            field=models.DateField(auto_now_add=True, verbose_name='Data de registro'),
        ),
    ]