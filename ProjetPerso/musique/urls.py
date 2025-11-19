from django.urls import path
from . import views

urlpatterns = [
    path('', views.musique_list, name='musique_list'),
]