"""
Set up a user profile for in-game that is attached
to the real world profile for purchases
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator
from products.models import Product, Category
from profiles.models import UserProfile


class GameItem(models.Model):
    user = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    size = models.PositiveIntegerField(null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    locate = [
        ("Storage", "Storage"),
        ("Bag", "Bag"),
        ("Trade", "Trade"),
    ]
    location = models.CharField(choices=locate, max_length=7, blank=False, default="Storage")

    def save(self, *args, **kwargs):
        """
        Save the order to the game profile separting all items.
        """
        super().save(*args, **kwargs)


class GameProfile(models.Model):
    """
    A user profile model for displaying default
    in-game information.
    """
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    bag_size = models.PositiveIntegerField(validators=[MaxValueValidator(
        20000), MinValueValidator(50)], null=True, blank=True)
    storage_size = models.PositiveIntegerField(validators=[MaxValueValidator(
        500000), MinValueValidator(50)], null=True, blank=True)
    trade_size = models.PositiveIntegerField(validators=[MaxValueValidator(
        100000), MinValueValidator(50)], null=True, blank=True)
    gold = models.PositiveIntegerField(null=True, blank=True)
    storage_items = models.CharField(max_length=254, null=True, blank=True)
    trade_items = models.CharField(max_length=254, null=True, blank=True)
    bag_increase = models.CharField(max_length=254, null=True, blank=True)
    storage_increase = models.CharField(max_length=254, null=True, blank=True)
    trade_increase = models.CharField(max_length=254, null=True, blank=True)
    enchantments = models.CharField(max_length=254, null=True, blank=True)
    character_name = models.CharField(max_length=254, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class CharacterChoice(models.Model):
    race = models.ForeignKey(
        'Creed', null=True, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=False, blank=False)
    strength = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True)


class Character(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    race = models.CharField(max_length=50, null=True, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    strength = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class BagStorage(models.Model):
    class Meta:
        verbose_name_plural = 'Bag storage'

    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    bag_size = models.PositiveIntegerField(validators=[MaxValueValidator(
        20000), MinValueValidator(50)], null=True, blank=True)
    bag_item = models.ForeignKey(GameItem, null=True,
                              blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    item_size = models.PositiveIntegerField(null=True, blank=True)
    category = models.CharField(max_length=254, null=True, blank=True)
    item_weight = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=254, null=True, blank=True)



class Storage(models.Model):
    class Meta:
        verbose_name_plural = 'Storage'

    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    storage_size = models.PositiveIntegerField(validators=[MaxValueValidator(
        500000), MinValueValidator(50)], null=True, blank=False)
    storage_item = models.CharField(max_length=254, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    item_size = models.PositiveIntegerField(null=True, blank=True)
    category = models.CharField(max_length=254, null=True, blank=True)
    item_weight = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=254, null=True, blank=True)


class Trade(models.Model):
    class Meta:
        verbose_name_plural = 'Trading'

    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    trade_size = models.PositiveIntegerField(validators=[MaxValueValidator(
        100000), MinValueValidator(50)], null=True, blank=False)
    trade_item = models.CharField(max_length=254, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    item_size = models.PositiveIntegerField(null=True, blank=True)
    category = models.CharField(max_length=254, null=True, blank=True)
    item_weight = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=254, null=True, blank=True)


class UserOwned(models.Model):
    class Meta:
        verbose_name_plural = 'User owned'

    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    item = models.CharField(max_length=254, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    item_size = models.PositiveIntegerField(null=True, blank=True)
    category = models.CharField(max_length=254, null=True, blank=True)
    item_weight = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=254, null=True, blank=True)

class Creed(models.Model):
    creed = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.creed
