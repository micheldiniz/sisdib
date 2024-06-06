# Generated by Django 5.0.1 on 2024-01-23 15:08

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assinatura', '0003_remove_pessoa_contato_remove_pessoa_endereco_and_more'),
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assinatura',
            name='pessoa',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='pessoa.pessoa'),
            preserve_default=False,
        ),
    ]