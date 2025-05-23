from django.shortcuts import render , redirect 
from django.contrib import messages
from .models import Register
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name' , '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        fist_password = request.POST.get('password', '').strip()
        second_password = request.POST.get('confirmpassword', '').strip()
        
        if not (first_name and last_name and email and fist_password and second_password):
            return render(request, 'signup.html', {'error': 'All fields are required!'})
        
        if fist_password != second_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match!'})
        
        Register(firstname=first_name, lastname=last_name, email=email, password=fist_password).save()
        messages.success(request, 'Account created successfully!')
        return redirect('register')
    
    return render(request, 'signup.html')
