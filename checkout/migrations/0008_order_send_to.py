# Generated by Django 3.1.7 on 2021-04-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='send_to',
            field=models.CharField(choices=[('1', 'Storage'), ('2', 'Bag'), ('3', 'Trade')], default=1, max_length=7),
        ),
    ]
