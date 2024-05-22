# Generated by Django 4.2.11 on 2024-05-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0038_edicaomaterialassinatura_quantidade_assinaturas_es_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edicaomaterialassinatura',
            name='quantidade_assinaturas_Es',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Qtd. ass. Estrangeiros (ativas)'),
        ),
        migrations.AlterField(
            model_name='edicaomaterialassinatura',
            name='quantidade_assinaturas_OE',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Qtd. ass. Outros Estados (ativas)'),
        ),
        migrations.AlterField(
            model_name='edicaomaterialassinatura',
            name='quantidade_assinaturas_RJ',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Qtd. ass. Rio de Janeiro (ativas)'),
        ),
    ]
