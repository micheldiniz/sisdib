# Generated by Django 5.0.1 on 2024-04-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0015_alter_itempedido_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroEnvioPedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=255, verbose_name='Descrição')),
                ('data_registro', models.DateTimeField(auto_now_add=True, verbose_name='Data de registro')),
                ('data_envio', models.DateField(blank=True, null=True)),
                ('observacao', models.CharField(blank=True, max_length=255, verbose_name='Observação')),
                ('pedidos', models.ManyToManyField(limit_choices_to={'estado_do_pedido': 'novo'}, to='pedido.pedido')),
            ],
            options={
                'verbose_name_plural': 'Registo de envio de Pedidos',
            },
        ),
    ]