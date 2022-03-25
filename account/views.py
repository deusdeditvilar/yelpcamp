from django.shortcuts import render


def landing(request):
    return render(request,'dashboard/landing.html')

def home(request):
    return render(request,'dashboard/home.html')

def signup(request):
    return render(request, 'account/auth.html',{"login": False,"btntext": "Create an account"})

def login(request):
    return render(request, 'account/auth.html',{"login": True,"btntext": "Login"})