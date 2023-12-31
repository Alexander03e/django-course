"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hello import views
from film import views
# from favorites import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from film.views import FilmViewSet

router = routers.DefaultRouter()
# router.register(r'films', views.FilmViewSet)

urlpatterns = [
    path('', include('hello.urls')),
    path('api/', include(router.urls)),
    path('api/films/', FilmViewSet.as_view()),
    path('films/', include('film.urls')),
    path('serials/', include('serials.urls')),
    path('favorites/', include('favorites.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls