from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('otp/', views.otp, name='otp'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('json_ot/', views.json_ot, name='json_ot'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login')
]
