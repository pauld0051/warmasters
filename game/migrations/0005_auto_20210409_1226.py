# Generated by Django 3.1.7 on 2021-04-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20210408_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameprofile',
            name='bag_items',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='gameprofile',
            name='storage_items',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
