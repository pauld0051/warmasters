from django.contrib import admin
from .models import (
    Creed, Character, GameProfile, BagStorage, Storage, Trade, UserOwned
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


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'race',
        'name',
        'strength',
        'image',
    )

    ordering = ('name',)


class GameProfileAdmin(admin.ModelAdmin):
    list_display = (
        'bag_size',
        'storage',
        'gold',
        'bag_items',
        'storage_items',
        'enchantments',
        'location',
    )


class BagStorageAdmin(admin.ModelAdmin):
    list_display = (
        'bag_size',
        'bag_item',
        'quantity',
        'item_size',
        'user',
        'category',
        'item_weight',
        'location',
    )


class StorageAdmin(admin.ModelAdmin):
    list_display = (
        'storage_size',
        'storage_item',
        'quantity',
        'item_size',
        'user',
        'category',
        'location',
    )


class TradeAdmin(admin.ModelAdmin):
    list_display = (
        'trade_size',
        'category',
        'trade_item',
        'quantity',
        'item_size',
        'item_weight',
        'user',
        'location',
    )


class UserOwnedAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'quantity',
        'item_size',
        'item_weight',
        'user',
        'location',
        'item',
    )

admin.site.register(Creed, CreedAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(GameProfile, GameProfileAdmin)
admin.site.register(BagStorage, BagStorageAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Trade, TradeAdmin)
admin.site.register(UserOwned, UserOwnedAdmin)
