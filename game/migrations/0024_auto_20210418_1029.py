# Generated by Django 3.1.7 on 2021-04-18 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210407_1224'),
        ('game', '0023_auto_20210418_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameitem',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]