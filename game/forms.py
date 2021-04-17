"""
Form details for moving items
to the game_item bag.
"""

from django import forms
from .models import (
    GameItem, Character,
    GameProfile, BagStorage,
    Storage, Trade
)


class GameItemForm(forms.ModelForm):
    class Meta:
        model = GameItem
        fields = ('user', 'product',
                  'quantity', 'location')


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('race', 'name',
                 'strength', 'image',
                 'user')


class GameProfileForm(forms.ModelForm):
    class Meta:
        model = GameProfile
        fields = ('character_name',)


class BagStorageForm(forms.ModelForm):
    class Meta:
        model = BagStorage
        fields = ('bag_size',)


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ('storage_size',)


class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ('trade_size',)
