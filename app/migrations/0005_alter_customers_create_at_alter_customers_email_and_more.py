# Generated by Django 4.0.5 on 2022-06-09 20:58

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_customers_create_at_alter_customers_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customers',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^-?\\d+\\Z'), code='invalid', message='Enter a valid integer.')]),
        ),
        migrations.AlterField(
            model_name='customers',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
