# Generated by Django 3.1.7 on 2021-04-16 07:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0012_auto_20210411_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameprofile',
            name='trade_size',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(50)]),
        ),
        migrations.CreateModel(
            name='CreateCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('strength', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('race', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.creed')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
