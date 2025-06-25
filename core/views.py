from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


# Create your views here.
def home_view(request):
    return render(request, "home.html")
def seacrh_view(request):
    return render(request, 'index.html')
