from django.urls import path
from Video import views

urlpatterns=[
    path('',views.video,name='video')
]