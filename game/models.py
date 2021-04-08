"""
Set up a user profile for in-game that is attached
to the real world profile for purchases
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class GameProfile(models.Model):
    """
    A user profile model for displaying default
    in-game information.
    """
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    game_name = models.CharField(
        max_length=20, null=False, blank=False)

    def __str__(self):
        return str(self.game_name)
