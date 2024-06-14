from django.shortcuts import render
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

    return render(request,'templates/receipes.html')