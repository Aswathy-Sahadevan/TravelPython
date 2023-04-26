from collections import UserDict
from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def register(request):
   
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email_id=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email_id)
        user.save();
        print("user createrd")

    return render(request,"register.html")

