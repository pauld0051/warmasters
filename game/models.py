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
    gold = models.PositiveIntegerField(null=True, blank=False)
    
    storage_items = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return str(self.user)


class Bag(models.Model):
    bag_size = models.PositiveIntegerField(validators=[MaxValueValidator(
        2000), MinValueValidator(50)], null=True, blank=True)
    bag_items = models.CharField(max_length=254, null=True, blank=True)


class Storage(models.Model):
    storage = models.PositiveIntegerField(validators=[MaxValueValidator(
        2000), MinValueValidator(50)], null=True, blank=True)
    bag_items = models.CharField(max_length=254, null=True, blank=True)



class Creed(models.Model):
    creed = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.creed


class Character(models.Model):
    race = models.ForeignKey('Creed', null=True, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=False, blank=False)
    strength = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True)

