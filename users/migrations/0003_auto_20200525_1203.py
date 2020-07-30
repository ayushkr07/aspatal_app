# Generated by Django 3.0.6 on 2020-05-25 06:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200525_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
