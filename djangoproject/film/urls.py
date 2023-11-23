from django.urls import path, include
from . import views
# from rest_framework import routers

urlpatterns = [
    path('', views.films, name="films"),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('<int:object_id>', views.film_detail, name='films'),
    path('like/<int:film_id>/', views.like_film, name='like_film'),
    path('dislike/<int:film_id>/', views.dislike_film, name='dislike_film')
]

