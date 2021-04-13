"""
Form details for moving items
to the game_item bag.
"""

from django import forms
from .models import GameItem


class GameItemForm(forms.ModelForm):
    class Meta:
        model = GameItem
        fields = ('user', 'product',
                  'quantity', 'location')


