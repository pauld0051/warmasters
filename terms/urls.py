from django.urls import path
from . import views

urlpatterns = [
    path('terms-and-conditions/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy')
]
