from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register_user(request):

    if request.method == 'POST':
        username   = request.POST['username']
        email      = request.POST['email']
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        pw1        = request.POST['password1']
        pw2        = request.POST['password2']

        if pw1 != pw2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        else:
            user = User(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.set_password(pw1)
            user.save()
            messages.info(request,'User created successfully')
            return redirect('/auth/login/')
    
    template = loader.get_template('register.html')
    context = {}
    return HttpResponse(template.render(context,request))
  
def login_user(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,'User with this username does not exist')
            return redirect('/auth/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request,'invalid password')
            return redirect('/auth/login')
        

        login(request,user)
        messages.info(request,'login successful')

        return redirect('/dashboard/')
    
    template = loader.get_template('login.html')
    context ={}
    return HttpResponse(template.render(context,request))

def logout_user(request):
    logout(request)
    messages.info(request,'logout successful')
    return redirect('/auth/login/')