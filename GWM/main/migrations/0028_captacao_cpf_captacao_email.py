# Generated by Django 5.1.7 on 2025-04-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_captacao_pl_alter_captacao_planejado_migracao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='captacao',
            name='cpf',
            field=models.CharField(blank=True, default='', max_length=14, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='captacao',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=255, verbose_name='Email'),
        ),
    ]
