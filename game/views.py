from django.shortcuts import (
    render, get_object_or_404
)
from profiles.models import UserProfile
from .models import GameProfile, Creed, Character

def game_profile(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        orders = profile.orders.all()
        accessories = GameProfile.objects.all

        template = 'game/game_profile.html'
        context = {
        'profile': profile,
        'orders': orders,
        'accessories': accessories,
    }

    return render(request, template, context)



