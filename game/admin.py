from django.contrib import admin
from .models import (
    Creed, Character, GameProfile, BagStorage,
    Storage, Trade, UserOwned, GameItem,
    CharacterChoice
)

# Register your models here.
"""
Include the list_displays for the admin.
"""


class CreedAdmin(admin.ModelAdmin):
    list_display = (
        'creed',
    )

    ordering = ('creed',)


class CharacterChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'race',
        'name',
        'strength',
        'image',
    )


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'race',
        'name',
        'strength',
        'image',
        'user',
    )

    ordering = ('user',)




class GameItemAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'quantity',
        'location',
    )


class GameProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'bag_size',
        'storage_size',
        'gold',
        'bag_increase',
        'storage_increase',
        'trade_increase',
        'enchantments',
    )


class BagStorageAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'bag_size',
        'category',
        'bag_item',
        'quantity',
        'item_size',
        'item_weight',
        'location',
    )


class StorageAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'storage_size',
        'category',
        'storage_item',
        'quantity',
        'item_size',
        'item_weight',
        'location',
    )


class TradeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'trade_size',
        'trade_item',
        'category',
        'quantity',
        'item_size',
        'item_weight',
        'location',
    )


class UserOwnedAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'category',
        'item',
        'quantity',
        'item_size',
        'item_weight',
        'location',
    )

admin.site.register(Creed, CreedAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(GameProfile, GameProfileAdmin)
admin.site.register(GameItem, GameItemAdmin)
admin.site.register(BagStorage, BagStorageAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Trade, TradeAdmin)
admin.site.register(UserOwned, UserOwnedAdmin)
admin.site.register(CharacterChoice, CharacterChoiceAdmin)
