from django.shortcuts import render, get_object_or_404, redirect
from .models import Films, Director
from django.views import View
from .serializers import FilmsSerializer
from django.http import JsonResponse
from rest_framework import viewsets,routers,serializers

from rest_framework import generics

# Create your views here.
def films(request):
    films = Films.objects.all()
    return render(request, "films/object.html", {'films': films})
    

def film_detail(request, object_id):
    object = get_object_or_404(Films, pk=object_id)
    return render(request, 'films/about.html', {'object': object})

def rec_detail (request, object_id):
    object = get_object_or_404(Films, pk=object_id)
    return render(request, 'home.html', {'object': object})

def like_film(request, film_id):
    film = Films.objects.get(id=film_id)
    film.is_favorite = True
    film.save()
    return redirect('films')
def dislike_film(request, film_id):
    film = Films.objects.get(id=film_id)
    film.is_favorite = False
    film.save()
    return redirect('films')

class FilmViewSet(generics.ListAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer

