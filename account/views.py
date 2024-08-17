from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def login(request):
    return render(request,'account/login.html')

def signup(request):


    if request.method == "POST":
        user_name = request.POST.get("username")
        user_pass = request.POST.get("password")

        new_register = User(username = user_name)
        new_register.set_password(user_pass)
        new_register.save()
        return redirect("login")
        

    return render(request,'account/signup.html')





# Create your views here.
