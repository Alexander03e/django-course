from django.shortcuts import render, get_object_or_404, redirect
from .models import Films, Director
from django.views import View
from .serializers import FilmsSerializer
from django.http import JsonResponse
from rest_framework import viewsets,routers,serializers

from rest_framework import generics

# Create your views here.
class FilmViewSet(generics.ListAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer

