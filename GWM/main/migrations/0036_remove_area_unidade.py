# Generated by Django 5.1.7 on 2025-05-08 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_customuser_supervisor_unidade_head_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='unidade',
        ),
    ]
