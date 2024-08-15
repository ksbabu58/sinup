from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_login
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.
from django.shortcuts import render


def login_view(request):
    return render(request, 'login.html')
    # Your login logic here

def register_view(request):
    # Your registration logic here
    return render(request, 'register.html')


def home_view(request):
    return render(request, 'home.html')

'''
def home(request):
    if request.user.is_authenticated:
        return render(request,"home.html")
    else:
         return redirect('/signin')

def signin(request):
    if request.user.is_authenticated:
         return redirect('')
    else:
        if request.method=="POST":
            uname= request.POST['username']
            pword= request.POST['password']
            user=authenticate(username=uname,password=pword)
            if user is not None:
                login(request,user)
            else:
                return redirect('/signin')
        else:
            return render(request,"home.html")

'''