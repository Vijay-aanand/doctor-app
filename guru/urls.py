from django.urls import path
from . import views


urlpatterns=[
    path('',views.guru_list,name='guru_list'),


]