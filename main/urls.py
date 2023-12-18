# urlshortenerapp/urls.py
from django.urls import path
from .views import shorten_url, redirect_short_url

urlpatterns = [
    path('shorten/', shorten_url, name='shorten_url'),
    path('<str:short_url>/', redirect_short_url, name='redirect_short_url')
    ]