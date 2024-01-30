# band/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('restricted/', views.restricted_view, name='restricted_view'),
]
