from . import views
from django.urls import path



urlpatterns = [
    path('', views.user_login, name='login'),
    path('home/',views.home_page, name='home'),
    path('register/', views.registrations, name='register'),
]