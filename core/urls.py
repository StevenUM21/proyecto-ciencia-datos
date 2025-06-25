from django.contrib import admin
from django.urls import path, include

from core.views import seacrh_view, home_view

urlpatterns = [
    path('', home_view, name="home"),
    path('search/', seacrh_view, name="search"),
]