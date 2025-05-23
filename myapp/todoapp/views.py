from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Note
# Create your views here.

def login(request):
    # login function
    return render(request, 'login.html')

def profile(request):
    # profile function
    return render(request, 'profile.html')

def home(request):
    if request.method == 'POST':
        note = request.POST.get('note', '').strip()
        date = request.POST.get('date', '').strip()
        noteheading = request.POST.get('noteheading', '').strip()

        if not (note and date and noteheading):
            todos = Note.objects.all()
            return render(request, 'home.html', {
                'todos': todos,
                'error': 'All fields are required!'
            })
            
        # ✅ This prevents resubmission on refresh
        Note(note=note, date=date, noteheading=noteheading).save()
        messages.success(request, 'Note added successfully!')
        return redirect('home')

    todos = Note.objects.all()
    return render(request, 'home.html', {'todos': todos})