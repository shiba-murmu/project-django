from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from .models import Note 
# Create your views here.

def login(request):
    # login function
    return render(request, 'login.html')

def profile(request):
    # profile function
    return render(request, 'profile.html')




def noteitems(request , id):
    # noteitems function to show single notes
    item = get_object_or_404(Note , pk=id) # this function is used to get single note item from the database
    return render(request, 'noteitems.html', {'item': item})


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