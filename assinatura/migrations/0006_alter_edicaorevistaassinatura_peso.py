# Generated by Django 4.2.13 on 2024-07-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assinatura', '0005_alter_assinante_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edicaorevistaassinatura',
            name='peso',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='peso em gramas'),
        ),
    ]