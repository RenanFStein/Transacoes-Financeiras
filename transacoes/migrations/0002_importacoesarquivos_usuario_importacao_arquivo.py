# Generated by Django 4.0.2 on 2022-04-26 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transacoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='importacoesarquivos',
            name='usuario_importacao_arquivo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
