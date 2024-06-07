from django.contrib.auth.models import User
from django.shortcuts import render

def user_login(request):

    return render(request,'templates/login.html')
def home_page(request):
    pass
    return render(request,'templates/home.html')

def registrations(request):

    if request.method == "POST":
        fname =request.POST.get('fristname')
        lname =request.POST.get('lastname')
        uname =request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob=request.POST.get('dob')
        gender = request.POST.get('gender')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('repassword')
        my_user =User.object.create_user(fname,lname,uname,email,phone,dob,gender,pass1)
        my_user.save()
        print(my_user)
    return render(request,'templates/resistrations.html')

