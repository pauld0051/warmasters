from django.shortcuts import (
    render, get_object_or_404
)
from collections import Counter
from django.db.models import Sum
from profiles.models import UserProfile
from checkout.models import OrderLineItem
from .models import GameProfile, Creed, Character

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
        z = OrderLineItem.objects.filter(
            order__user_profile=request.user.userprofile)

        print("Here - look at this here...!!!***", Counter(z))

        template = 'game/game_profile.html'
        context = {
        'profile': profile,
        'orders': orders,
        'gold': gold,
        'bag_size': bag_size,
        'accessories': accessories,
        }

    return render(request, template, context)



