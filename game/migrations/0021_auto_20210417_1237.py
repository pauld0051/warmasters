# Generated by Django 3.1.7 on 2021-04-17 10:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0020_auto_20210417_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameprofile',
            name='bag_size',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='gameprofile',
            name='gold',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gameprofile',
            name='storage_size',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='gameprofile',
            name='trade_size',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(50)]),
        ),
    ]
