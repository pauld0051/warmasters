from django.shortcuts import (
    render, get_object_or_404
)
from django.db.models import Sum
from profiles.models import UserProfile
from checkout.models import OrderLineItem
from .models import (
    GameProfile, Creed, Character
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
        items = []
        for order in orders:
            location = order.send_to
            for item in order.lineitems.all():
                items.append({"name": item.product.name, "qty": item.quantity})
        x = {}
        for i in items:
            _key = i['name']
            _qty = i['qty']
            x[_key] = x.get(_key, 0) + _qty

        template = 'game/game_profile.html'
        context = {
        'profile': profile,
        'orders': orders,
        'gold': gold,
        'bag_size': bag_size,
        'storage_size': storage_size,
        'accessories': accessories,
        'item': x,
        }

    return render(request, template, context)
