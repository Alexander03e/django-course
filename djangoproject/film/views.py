from django.shortcuts import render, get_object_or_404, redirect
from .models import Films, Director
from django.views import View
from .serializers import FilmsSerializer
from .serializers import FilmsDetailSerializer
from django.http import JsonResponse
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics

# Create your views here.
# class FilmsViewSet(generics.ListAPIView):
#     queryset = Films.objects.all()
#     serializer_class = FilmsSerializer

class FilmsListView(viewsets.ModelViewSet):
    
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer

    def retrieve(self, request, pk):
        film = Films.objects.get(id=pk)
        serializer = FilmsDetailSerializer(film)
        return Response(serializer.data)
    
    @action(detail=False, methods = ['GET'])
    def get_favorite_films(self, request):
        favorite_films = Films.objects.filter(is_favorite=True)
        serializer = FilmsSerializer(favorite_films, many=True)
        return Response(serializer.data)









#----------------
        # paginator = LimitOffsetPagination()
        # result_page = paginator.paginate_queryset(queryset, request)
        # serializer = FilmsSerializer(result_page, many = True)
        # return paginator.get_paginated_response(serializer.data)

# class FilmsDetailView(APIView):

#     def get(self, request, pk):
#         film = Films.objects.get(id = pk)
#         serializer = FilmsDetailSerializer(film)
#         return Response(serializer.data)
    
#     @action(detail=False, methods=['GET'] )
#     def get_favorites_films(self, request):
#         films = Films.object.filter(is_favorite=True)
#         serializer = FilmsSerializer(films, many=True   )
#         return Response(serializer.data)
#     # def put(self, request, pk):
#     #     film = get_object_or_404(Films, id = pk)
#     #     serializer = FilmsSerializer(instance = film, data = request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data)
#     #     return Response(serializer.errors)
    
#     # def delete(self, request, pk):
#     #     film = get_object_or_404(Films, id = pk)
#     #     film.delete()
#     #     return Response('Film deleted')







