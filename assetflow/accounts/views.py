# pyrefly: ignore [missing-import]
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def base(request):
    return render(request,"base.html")

def user_login(request):
    return render(request,"accounts/login.html")

def user_signup(request):
    return render(request,"accounts/signup.html")

def forgot_password(request):
    return render(request,"accounts/forgotpassword.html")

def reset_password(request):
    return render(request,"accounts/reset_password.html")

def password_success(request):
    return render(request,"accounts/password_success.html")
