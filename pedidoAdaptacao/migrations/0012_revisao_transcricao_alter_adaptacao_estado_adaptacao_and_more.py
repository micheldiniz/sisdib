# Generated by Django 4.2.11 on 2024-05-29 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidoAdaptacao', '0011_rename_estado_envio_revisao_estado_revisao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='revisao',
            name='transcricao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pedidoAdaptacao.transcricao'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adaptacao',
            name='estado_adaptacao',
            field=models.CharField(choices=[('novo', 'novo'), ('processado', 'processado'), ('pendente', 'pendente'), ('finalizado', 'finalizado')], default='novo', max_length=255, verbose_name='estado da adaptação'),
        ),
        migrations.AlterField(
            model_name='diagramacao',
            name='estado_diagramacao',
            field=models.CharField(choices=[('novo', 'novo'), ('processado', 'processado'), ('pendente', 'pendente'), ('finalizado', 'finalizado')], default='novo', max_length=255, verbose_name='estado da diagramação'),
        ),
        migrations.AlterField(
            model_name='encadernacao',
            name='estado_encadernacao',
            field=models.CharField(choices=[('novo', 'novo'), ('processado', 'processado'), ('pendente', 'pendente'), ('finalizado', 'finalizado')], default='novo', max_length=255, verbose_name='estado da encadernação'),
        ),
        migrations.AlterField(
            model_name='esteriotipia',
            name='estado_esteriotipia',
            field=models.CharField(choices=[('novo', 'novo'), ('processado', 'processado'), ('pendente', 'pendente'), ('finalizado', 'finalizado')], default='novo', max_length=255, verbose_name='estado da esteriotipia'),
        ),
        migrations.AlterField(
            model_name='impressao',
            name='estado_impressao',
            field=models.CharField(choices=[('novo', 'novo'), ('processado', 'processado'), ('pendente', 'pendente'), ('finalizado', 'finalizado')], default='novo', max_length=255, verbose_name='estado da impressão'),
        ),
        migrations.AlterField(
            model_name='revisao',
            name='estado_revisao',
            field=models.CharField(choices=[('novo', 'novo'), ('processado', 'processado'), ('pendente', 'pendente'), ('finalizado', 'finalizado')], default='novo', max_length=255),
        ),
        migrations.AlterField(
            model_name='transcricao',
            name='estado_transcricao',
            field=models.CharField(choices=[('novo', 'novo'), ('processado', 'processado'), ('pendente', 'pendente'), ('finalizado', 'finalizado')], default='novo', max_length=255, verbose_name='estado da transcrição'),
        ),
    ]
