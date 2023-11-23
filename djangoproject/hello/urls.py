
from django.urls import path
from . import views



urlpatterns = [
    # path('films', views.films, name='films'),
    # path('serials', views.serials, name='serials'),
    # path('favorites', views.favorites, name='favorites'),
    path('', views.home, name='home'),
    
]
