# Generated by Django 5.0.1 on 2024-05-28 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidoAdaptacao', '0008_pedidoadaptacao_quantidade_solicitada'),
        ('pessoa', '0017_alter_funcionario_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adaptacao',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.funcionario'),
        ),
        migrations.AlterField(
            model_name='diagramacao',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.funcionario'),
        ),
        migrations.AlterField(
            model_name='encadernacao',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.funcionario'),
        ),
        migrations.AlterField(
            model_name='esteriotipia',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.funcionario'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.funcionario'),
        ),
        migrations.AlterField(
            model_name='impressao',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.funcionario'),
        ),
        migrations.AlterField(
            model_name='revisao',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.funcionario'),
        ),
        migrations.AlterField(
            model_name='transcricao',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.funcionario'),
        ),
    ]