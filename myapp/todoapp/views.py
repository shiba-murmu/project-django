from django.shortcuts import render

# Create your views here.

def home(request):
    # homepage function views here
    return render(request, 'home.html')

def login(request):
    # login function
    return render(request, 'login.html')

def profile(request):
    # profile function
    return render(request, 'profile.html')