from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.db.models import F, Sum
from django.contrib.auth.models import User
from profiles.models import UserProfile
from products.models import Product, Category
from .models import (
    GameProfile, Creed, Character,
    BagStorage, Storage, Trade,
    CharacterChoice, GameItem
)
from .forms import CharacterForm, GameProfileForm


def make_profile(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        template = 'game/make_profile.html'
        context = {
            'profile': profile,
        }
        if request.method == 'POST':
            GameProfile.objects.create(
                user=request.user, bag_size=0,
                storage_size=0, trade_size=0,
                gold=50, storage_items="",
                trade_items="", bag_increase=0,
                storage_increase=0, trade_increase=0,
                enchantments="", character_name=""
            )

            return redirect('create_character')

        return render(request, template, context)


def game_profile(request):
    if request.user.is_authenticated:
        try:
            # Used only as a check - variable remains unused
            profile_exists = request.user.gameprofile.user
        except:
            return redirect('make_profile')
        profile = UserProfile.objects.get(user=request.user)
        gold = request.user.gameprofile.gold
        character_name = request.user.gameprofile.character_name
        game_profile = request.user.gameprofile
        character_details = request.user.character
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
            'game_profile': game_profile,
            'character': character_details,
        }

        return render(request, template, context)


def create_character(request):
    character_name = request.user.gameprofile.character_name
    if not character_name:
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
            game_profile = request.user.gameprofile
            game_profile.character_name = chosen_character_name
            game_profile.save()
            Character.objects.create(
                name=chosen_character_name, race=chosen_character_race,
                strength=chosen_character_strength, image=chosen_character_image,
                user=request.user)
            BagStorage.objects.create(user=request.user, bag_size=50)
            Storage.objects.create(user=request.user, storage_size=200)
            Trade.objects.create(user=request.user, trade_size=50)
            return redirect('game_profile')

        return render(request, template, context)
    else:
        return redirect('game_profile')


def game_item_storage(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        storage_items = Storage.objects.get(user=request.user)
        game_items = GameItem.objects.filter(user=profile)
        products = Product.objects.all()
        categories = Category.objects.all()
        gold = request.user.gameprofile.gold
        reduce_hold_by = 0
        for game_item in game_items:
            if game_item.location == "Storage" and game_item.size:
                reduce_hold_by += game_item.quantity * game_item.size
        hold_size = storage_items.storage_size - reduce_hold_by
        template = 'game/game_item_storage.html'
        context = {
            'storage': storage_items,
            'game_items': game_items,
            'user': profile,
            'products': products,
            'categories': categories,
            'hold_size': hold_size,
            'gold': gold,
        }
        return render(request, template, context)


def game_item_bag(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        bag_items = BagStorage.objects.get(user=request.user)
        game_items = GameItem.objects.filter(user=profile)
        products = Product.objects.all()
        categories = Category.objects.all()
        gold = request.user.gameprofile.gold
        reduce_bag_by = 0
        for game_item in game_items:
            if game_item.location == "Bag" and game_item.size:
                reduce_bag_by += game_item.quantity * game_item.size
        bag_size = bag_items.bag_size - reduce_bag_by
        template = 'game/game_item_bag.html'
        context = {
            'bag': bag_items,
            'game_items': game_items,
            'user': profile,
            'products': products,
            'categories': categories,
            'bag_size': bag_size,
            'gold': gold,
        }
        return render(request, template, context)


def game_item_trade(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        trade_items = Trade.objects.get(user=request.user)
        game_items = GameItem.objects.filter(user=profile)
        products = Product.objects.all()
        categories = Category.objects.all()
        gold = request.user.gameprofile.gold
        reduce_trade_by = 0
        for game_item in game_items:
            if game_item.location == "Trade" and game_item.size:
                reduce_trade_by += game_item.quantity * game_item.size
        trade_size = trade_items.trade_size - reduce_trade_by
        template = 'game/game_item_trade.html'
        context = {
            'trade': trade_items,
            'game_items': game_items,
            'user': profile,
            'products': products,
            'categories': categories,
            'gold': gold,
            'trade_size': trade_size,
        }
        return render(request, template, context)
