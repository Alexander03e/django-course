from django.shortcuts import render

# Create your views here.
from film.models import Films
from serials.models import Serials



def favorites(request):
    serials = Serials.objects.filter(is_favorite=True)
    films = Films.objects.filter(is_favorite=True)
    data = {'films':films, 'serials':serials}
    return render(request, "favorites/liked.html", context = data)

