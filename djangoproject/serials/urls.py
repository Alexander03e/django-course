from django.urls import path
from . import views

urlpatterns = [
    path('', views.serials, name="serials"),
    path('<int:object_id>', views.serial_detail, name='serials'),
    path('like/<int:serial_id>/', views.like_serial, name='like_serial'),
    path('dislike/<int:serial_id>/', views.dislike_serial, name='dislike_serial'),
]