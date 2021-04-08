from django.shortcuts import (
    render, get_object_or_404
)
from profiles.models import UserProfile
from .models import GameProfile
from .forms import GameProfileForm

def game_profile(request):
    """ Display in-game profile """
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            #game_profile = GameProfile(initial={
            #            'game_name': profile.user.game_name,
            #        })
        except UserProfile.DoesNotExist:
            game_profile = GameProfile()
    else:
        game_profile = game_profile()

    form = GameProfileForm(instance=profile)
    template = 'game/game_profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

