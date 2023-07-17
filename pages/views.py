from django.shortcuts import render

def about(request):
    return render (request, 'pages/about.html')

def dashboard(request):
    return render (request, 'pages/dashboard.html')

def index(request):
    return render (request, 'pages/index.html')

def login(request):
    return render (request, 'pages/login.html')

def register(request):
    return render (request, 'pages/register.html')