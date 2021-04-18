from django.urls import path
from . import views

urlpatterns = [
    path('make_profile/', views.make_profile, name='make_profile'),
    path('game_profile/', views.game_profile, name='game_profile'),
    path('create_character/', views.create_character, name='create_character'),
    path('game_item_storage/', views.game_item_storage, name='game_item_storage'),
    path('game_item_bag/', views.game_item_bag, name='game_item_bag'),
    path('game_item_trade/', views.game_item_trade, name='game_item_trade'),
]
