from django.urls import path

from vegetable import views

urlpatterns = [

    path('', views.receipes, name='receipes'),
]
