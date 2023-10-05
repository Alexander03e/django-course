from django.shortcuts import render,redirect
from .models import Liked
from film.models import Films

# def films(request):
#     return render(request,"films/object.html")

def home(request):
    return render(request,"home.html")

# def favorites(request):
#     return render(request, "favorites/liked.html")

