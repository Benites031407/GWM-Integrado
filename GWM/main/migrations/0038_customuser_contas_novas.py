# Generated by Django 5.1.7 on 2025-05-08 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_alter_area_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contas_novas',
            field=models.PositiveIntegerField(default=0, verbose_name='Contas Novas'),
        ),
    ]
