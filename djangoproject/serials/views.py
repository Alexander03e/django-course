from django.shortcuts import render, get_object_or_404,redirect
from .models import Serials
from rest_framework import generics
from .serializers import SerialsSerializer
from rest_framework import viewsets,routers,serializers


# Create your views here.
def serials(request):
    serials = Serials.objects.all()
    return render(request, "serials/object.html", {'serials': serials})
    

def serial_detail(request, object_id):
    object = get_object_or_404(Serials, pk=object_id)
    return render(request, 'serials/about.html', {'object': object})

def like_serial(request, serial_id):
    serial = Serials.objects.get(id=serial_id)
    serial.is_favorite = True
    serial.save()
    return redirect('serials')
def dislike_serial(request, serial_id):
    serial = Serials.objects.get(id=serial_id)
    serial.is_favorite = False
    serial.save()
    return redirect('serials')

class SerialsViewSet(generics.ListAPIView):
    queryset = Serials.objects.all()
    serializer_class = SerialsSerializer