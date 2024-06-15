from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def receipes(request):

    if request.method == 'POST':
        data =request.POST
        rec_name = data.get('rec_name')
        rec_price= data.get('rec_price')
        rec_dis= data.get('rec_dis')
        rec_image=request.FILES.get('rec_image')

        Vegetable.objects.create(
            rec_name=rec_name,
            rec_price=rec_price,
            rec_dis=rec_dis,
            rec_image=rec_image,
        )
        return redirect('receipes')


    return render(request,'templates/receipes.html')
def show_receipes(request):

    data_rece = Vegetable.objects.all()
    context = {'data_rece': data_rece}
    return render(request,"templates/show_receipes.html",context)

def delete_receipes(request, id):
    de=Vegetable.objects.get(id=id)
    de.delete()
    return redirect('show_receipes')