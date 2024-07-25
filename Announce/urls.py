# Announce/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('announce/', views.announce_list, name='announce_list'),
    path('json/',views.json,name='json')
   
]

