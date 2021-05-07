# Generated by Django 3.1.7 on 2021-05-03 14:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0025_auto_20210503_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bagstorage',
            name='bag_size',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(20000), django.core.validators.MinValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='storage',
            name='storage_size',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(500000), django.core.validators.MinValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='trade',
            name='trade_size',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(50)]),
        ),
    ]
