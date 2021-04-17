from django.urls import path
from . import views

urlpatterns = [
    path('make_profile/', views.make_profile, name='make_profile'),
    path('game_profile/', views.game_profile, name='game_profile'),
    path('create_character/', views.create_character, name='create_character'),
]
