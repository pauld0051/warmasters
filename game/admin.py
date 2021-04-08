from django.contrib import admin
from .models import Creed, Character, GameProfile

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
        'image'
    )

    ordering = ('name',)


class GameProfileAdmin(admin.ModelAdmin):
    list_display = (
        'bag_size',
        'storage',
        'gold',
    )


admin.site.register(Creed, CreedAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(GameProfile, GameProfileAdmin)
