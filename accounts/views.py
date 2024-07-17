from django.shortcuts import render, get_object_or_404,redirect
from.forms import AuthorForm,BookForm
from django.core.paginator import Paginator, EmptyPage
from book_app.models import Book
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate

from accounts.models import UserProfile


# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def register_user(request) :
    if request.method=='POST':

        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('password1')

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'this username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'this mail id already taken') 
                return redirect('register')
  
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)  
                user.save()
                user_profile = UserProfile.objects.create(user=user)
                user_profile.save()
            return redirect('login')
        else:
            messages.info(request,'This password not matching')
            return redirect('register')

    return render(request,'admin/register.html') 


def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('listview')
        else:
            messages.info(request,'please provide correct details')
            return redirect('login')


    return render(request,'admin/login.html')

def logOut(request):
    auth.logout(request)
    return redirect('login')

