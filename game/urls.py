from django.urls import path
from . import views

urlpatterns = [
    path('game_profile/', views.game_profile, name='game_profile'),
]
