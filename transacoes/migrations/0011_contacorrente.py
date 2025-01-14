# Generated by Django 4.0.2 on 2022-04-29 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacoes', '0010_delete_conta_controller'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContaCorrente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=255, null=True, unique=True)),
                ('agencia', models.CharField(max_length=255, null=True, unique=True)),
                ('conta', models.CharField(max_length=255, null=True, unique=True)),
                ('saldo', models.FloatField()),
            ],
        ),
    ]
