from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('mcq_json',views.mcq_json,name="mcq_json"),
    path('questions/<int:pk>/', views.question_detail, name='question_detail'),
]
