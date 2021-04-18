"""
Form details for moving items
to the game_item bag.
"""

from django import forms
from .models import (
    GameItem, Character,
    GameProfile, BagStorage,
    Storage, Trade, 
)


class GameItemForm(forms.ModelForm):
    class Meta:
        model = GameItem
        fields = ('user', 'product',
                  'category', 'image',
                  'size', 'weight',
                  'quantity', 'location',
                  )


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('user', 'race',
                 'name', 'strength',
                 'image',
                 )


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


class MakeProfileForm(forms.ModelForm):
    class Meta:
        model = GameProfile
        fields = ('user', 'bag_size',
                  'storage_size', 'trade_size',
                  'gold', 'storage_items',
                  'trade_items', 'bag_increase',
                  'storage_increase', 'trade_increase',
                  'enchantments', 'character_name',)
