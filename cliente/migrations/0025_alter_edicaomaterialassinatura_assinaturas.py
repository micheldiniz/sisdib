# Generated by Django 4.2.11 on 2024-04-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0024_edicaomaterialassinatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edicaomaterialassinatura',
            name='assinaturas',
            field=models.ManyToManyField(limit_choices_to={'estado': 'vigente'}, to='cliente.assinatura'),
        ),
    ]
