# Generated by Django 3.1.7 on 2021-03-28 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_remove_order_street_address2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_address1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='town_or_city',
        ),
    ]
