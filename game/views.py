from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.db.models import Sum
from django.contrib.auth.models import User
from profiles.models import UserProfile
from .models import (
    GameProfile, Creed, Character,
    BagStorage, Storage, Trade,
    CharacterChoice
)
from .forms import CharacterForm, GameProfileForm


def game_profile(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        gold = request.user.gameprofile.gold
        character_name = request.user.gameprofile.character_name
        if character_name is not None:
            bag = request.user.gameprofile.bag_size
            storage = request.user.gameprofile.storage_size
            trade = request.user.gameprofile.trade_size
            bag_item = request.user.bagstorage.bag_item
            storage_item = request.user.storage.storage_item
            trade_item = request.user.trade.trade_item
            bag_increase = request.user.gameprofile.bag_increase
            storage_increase = request.user.gameprofile.storage_increase
            trade_increase = request.user.gameprofile.trade_increase
        else:
            return redirect('create_character')

        template = 'game/game_profile.html'
        context = {
            'profile': profile,
            'gold': gold,
            'bag': bag,
            'storage': storage,
            'trade': trade,
            'bag_item': bag_item,
            'storage_item': storage_item,
            'trade_item': trade_item,
            'bag_increase': bag_increase,
            'storage_increase': storage_increase,
            'trade_increase': trade_increase,
            'character_name': character_name,
        }

        return render(request, template, context)


def create_character(request):
    character_name = request.user.gameprofile.character_name
    if character_name is None:
        character_choice = CharacterChoice.objects.all()
        profile = UserProfile.objects.get(user=request.user)
        template = 'game/create_character.html'
        context = {
            'character_choices': character_choice,
            'user': profile,
            }

        if request.method == 'POST':
            chosen_character_name = request.POST.get('name')
            chosen_character_race = request.POST.get('race')
            chosen_character_strength = request.POST.get('strength')
            chosen_character_image = request.POST.get('image')
            user = profile
            game_profile = request.user.gameprofile
            game_profile.character_name = chosen_character_name
            game_profile.save()
            Character.objects.create(
                name=chosen_character_name, race=chosen_character_race,
                strength=chosen_character_strength, image=chosen_character_image,
                user=user)
            BagStorage.objects.create(user=request.user, bag_size=50)
            Storage.objects.create(user=request.user, storage_size=200)
            Trade.objects.create(user=request.user, trade_size=50)
            return redirect('game_profile')

        return render(request, template, context)
    else:
        return redirect('game_profile')
