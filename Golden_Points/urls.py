from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_point, name='add_point'),
    path('points/', views.points_list, name='point_list'),
]
