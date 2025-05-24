from django.contrib.auth.models import User
from django.shortcuts import render , redirect 
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
import time
# Create your views here.
@login_required(login_url='/login/')
def edit_profile(request) :
    return render(request, 'editprofile.html')


def login_view(request) :
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not (username and password):
            return render(request, 'login.html', {'error': 'All fields are required!'})
        print('username : ' , username)
        print('password : ' , password)
        
        user = authenticate(request, username=username, password=password)
        print("Authenticated user:", user)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password!'})

    return render(request, 'login.html')

def user_logout(request):
    # logout function
    logout(request) # clearing sessions 
    return redirect('login')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        first_password = request.POST.get('password', '').strip()
        second_password = request.POST.get('confirmpassword', '').strip()

        # Field validation
        if not (first_name and last_name and username and email and first_password and second_password):
            return render(request, 'signup.html', {'error': 'All fields are required!'})

        if first_password != second_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match!'})

        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists!'})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists!'})

        if len(first_password) <= 8:
            return render(request, 'signup.html', {'error': 'Password must be at least 8 characters long!'})

        if len(username) <= 4:
            return render(request, 'signup.html', {'error': 'Username must be at least 4 characters long!'})

        if not email.endswith('@gmail.com'):
            return render(request, 'signup.html', {'error': 'Email must end with @gmail.com!'})

        if not username.isalpha():
            return render(request, 'signup.html', {'error': 'Username must contain only letters!'})

        # ✅ Create user using Django's User model
        user = User.objects.create_user(
            username=username,
            email=email,
            password=first_password,
            first_name=first_name,
            last_name=last_name
        )

        user.save()
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('login')  # Change this to your login page route name

    return render(request, 'signup.html')