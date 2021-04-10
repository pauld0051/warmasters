"""
Set up a user profile for in-game that is attached
to the real world profile for purchases
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator


class GameProfile(models.Model):
    """
    A user profile model for displaying default
    in-game information.
    """
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    bag_size = models.PositiveIntegerField(validators=[MaxValueValidator(
        2000), MinValueValidator(50)], null=True, blank=False)
    storage = models.PositiveIntegerField(validators=[MaxValueValidator(
        2000), MinValueValidator(50)], null=True, blank=False)
    gold = models.PositiveIntegerField(null=True, blank=False)
    bag_items = models.CharField(max_length=254, null=True, blank=True)
    storage_items = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class BagStorage(models.Model):
    class Meta:
        verbose_name_plural = 'Bag storage'

    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    bag_size = models.PositiveIntegerField(validators=[MaxValueValidator(
        2000), MinValueValidator(50)], null=True, blank=False)
    bag_item = models.CharField(max_length=254, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    item_size = models.PositiveIntegerField(null=True, blank=True)


class Storage(models.Model):
    class Meta:
        verbose_name_plural = 'Storage'

    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    storage_size = models.PositiveIntegerField(validators=[MaxValueValidator(
        2000), MinValueValidator(50)], null=True, blank=False)
    storage_item = models.CharField(max_length=254, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    item_size = models.PositiveIntegerField(null=True, blank=True)


class Trade(models.Model):
    class Meta:
        verbose_name_plural = 'Trading'

    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    trade_size = models.PositiveIntegerField(validators=[MaxValueValidator(
        2000), MinValueValidator(50)], null=True, blank=False)
    trade_item = models.CharField(max_length=254, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    item_size = models.PositiveIntegerField(null=True, blank=True)


class Creed(models.Model):
    creed = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.creed


class Character(models.Model):
    race = models.ForeignKey(
        'Creed', null=True, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=False, blank=False)
    strength = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True)
