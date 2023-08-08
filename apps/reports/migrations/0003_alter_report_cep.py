# Generated by Django 4.2.3 on 2023-08-07 18:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_alter_report_options_alter_report_cep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='cep',
            field=models.CharField(default='Sem CEP', max_length=11, validators=[django.core.validators.RegexValidator(message='Digite um CEP válido', regex='\\d{5}-?\\d{3}')]),
        ),
    ]