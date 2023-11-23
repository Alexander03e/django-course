from django.shortcuts import render,redirect

from film.models import Films
from .models import Recs

# def films(request):
#     return render(request,"films/object.html")

def home(request):
    recs = Recs.objects.all()
    return render(request, "home.html", {'recs':recs})

# def favorites(request):
#     return render(request, "favorites/liked.html")

def films(request):
    films = Films.objects.all()
    return render(request, "home.html", {'films': films})
    