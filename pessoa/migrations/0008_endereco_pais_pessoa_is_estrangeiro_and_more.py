# Generated by Django 5.0.1 on 2024-02-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0007_pessoa_data_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='pais',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='is_estrangeiro',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='nacionalidade',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='cpf',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
