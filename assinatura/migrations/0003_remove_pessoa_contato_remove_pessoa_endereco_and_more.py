# Generated by Django 5.0.1 on 2024-01-12 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assinatura', '0002_remove_assinatura_contato_remove_assinatura_endereco_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='contato',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='pessoafisica',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='pessoajuridica',
            name='pessoa',
        ),
        migrations.DeleteModel(
            name='Contato',
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
        migrations.DeleteModel(
            name='PessoaFisica',
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
        migrations.DeleteModel(
            name='PessoaJuridica',
        ),
    ]