# Generated by Django 4.0.2 on 2022-04-29 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacoes', '0004_remove_importacoesarquivos_status_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filtro_Buscas_Analises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicial_analise', models.DateField()),
                ('data_final_analise', models.DateField()),
            ],
        ),
    ]
