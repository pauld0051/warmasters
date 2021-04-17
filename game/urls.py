from django.urls import path
from . import views

urlpatterns = [
    path('game_profile/', views.game_profile, name='game_profile'),
    path('create_character/', views.create_character, name='create_character'),
]
