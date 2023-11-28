from django.shortcuts import render, get_object_or_404,redirect
from .models import Serials
from rest_framework import generics
from .serializers import SerialsSerializer
from rest_framework import viewsets,routers,serializers


# Create your views here.
def serials(request):
    serials = Serials.objects.all()
    return render(request, "serials/object.html", {'serials': serials})


class SerialsViewSet(generics.ListAPIView):
    queryset = Serials.objects.all()
    serializer_class = SerialsSerializer