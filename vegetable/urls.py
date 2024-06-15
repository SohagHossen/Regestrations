from django.urls import path

from vegetable import views

urlpatterns = [

    path('', views.receipes, name='receipes'),
    path('all_receipes/',views.show_receipes, name='show_receipes'),
    path('all_receipes/<id>/',views.delete_receipes ,name='delete_receipes'),
]
