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

    #Search function working
    if request.GET.get('rec_name_search'):
        data_rece = Vegetable.objects.filter(rec_name__icontains=request.GET.get('rec_name_search'))
    
    context = {'data_rece': data_rece}
    return render(request,"templates/show_receipes.html",context)

def delete_receipes(request, id):
    de=Vegetable.objects.get(id=id)
    de.delete()
    return redirect('show_receipes')

def update_receipes(request, id):
    up=Vegetable.objects.get(id=id)
    if request.method =='POST':
        data = request.POST
        rec_name = data.get('rec_name')
        rec_price = data.get('rec_price')
        rec_dis = data.get('rec_dis')
        rec_image = request.FILES.get('rec_image')
        # update value
        up.rec_name=rec_name
        up.rec_price=rec_price
        up.rec_dis=rec_dis
        if rec_image:
            up.rec_image=rec_image
            up.save()
            return redirect('show_receipes')

    context = {'update_rece': up}

    return render(request, 'templates/update_receipes.html',context)

    