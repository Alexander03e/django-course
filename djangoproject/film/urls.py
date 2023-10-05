from django.urls import path
from . import views


urlpatterns = [
    path('', views.films, name="films"),
    path('<int:object_id>', views.film_detail, name='films'),
    path('like/<int:film_id>/', views.like_film, name='like_film'),
    path('dislike/<int:film_id>/', views.dislike_film, name='dislike_film'),
]
