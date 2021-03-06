# Generated by Django 3.1.7 on 2021-04-08 14:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creed', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='gameprofile',
            name='game_name',
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('strength', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('bag_size', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(200)])),
                ('storage', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(200)])),
                ('gold', models.PositiveIntegerField(null=True)),
                ('race', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.creed')),
            ],
        ),
    ]
