from django.urls import path

from vegetable import views

urlpatterns = [

    path('rec/', views.receipes, name='receipes'),
    path('all_receipes/',views.show_receipes, name='show_receipes'),
    path('delete_receipes/<id>/',views.delete_receipes ,name='delete_receipes'),
    path('update_receipes/<id>/',views.update_receipes,name='update_receipes'),
]
