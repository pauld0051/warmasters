from collections import defaultdict
from django.shortcuts import (
    render, get_object_or_404
)
from django.db.models import Sum
from profiles.models import UserProfile
from checkout.models import OrderLineItem
from .models import (
    GameProfile, Creed, Character, BagStorage
    )

def game_profile(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        orders = profile.orders.all()
        accessories = GameProfile.objects.all()
        gold = request.user.gameprofile.gold
        sum_size = OrderLineItem.objects.filter(
            order__user_profile=request.user.userprofile)
        total_size = 0
        if sum_size:
            total_size = sum_size.aggregate(size=Sum('product__size'))['size']
        bag_size = request.user.gameprofile.bag_size - total_size
        storage_size = request.user.gameprofile.storage - total_size
        trade_size = request.user.gameprofile.storage - total_size
        items = []
        x = defaultdict(dict)
        for order in orders:
            for item in order.lineitems.all():
                items.append({"name": item.product.name, "qty": item.quantity})
                x[order.send_to][item.product.name] = item.quantity
        print(x)
        template = 'game/game_profile.html'
        context = {
        'profile': profile,
        'orders': orders,
        'gold': gold,
        'bag_size': bag_size,
        'storage_size': storage_size,
        'accessories': accessories,
        'data': dict(x),
        }

    return render(request, template, context)


def bag_storage(request):
    if request.user.is_authenticated:
        bag_size = request.user.gameprofile.bag_size

    template = 'game/game_profile.html'
    context = {
        'bag_size': bag_size,
    }

    return render(request, template, context)


def storage(request):
    if request.user.is_authenticated:
        storage = request.user.gameprofile.storage_size

    template = 'game/game_profile.html'
    context = {
        'storage': storage,
    }

    return render(request, template, context)


def trade(request):
    if request.user.is_authenticated:
        trade = request.user.gameprofile.trade_size

    template = 'game/game_profile.html'
    context = {
        'trade': trade,
    }

    return render(request, template, context)
