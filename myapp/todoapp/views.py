from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from .models import Note 
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate , login , logout
# Create your views here.

def login(request):
    # login function
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')

@login_required(login_url='/login/')
def profile(request):
    user = request.user # loggined user data
    firstname = user.first_name
    lastname = user.last_name
    username = user.username
    userEmail = user.email
    user_joined_date = user.date_joined
    # returning by this function profile..
    return render(request, 'profile.html' , {
        'firstname' : firstname,
        'lastname' : lastname,
        'username' : username,
        'userEmail' : userEmail,
        'user_joined_date' : user_joined_date
    })


@login_required(login_url='/login/')
def noteitems(request , id):
    # noteitems function to show single notes
    item = get_object_or_404(Note , pk=id) # this function is used to get single note item from the database
    return render(request, 'noteitems.html', {'item': item})



@login_required(login_url='/login/')
def delete_note(request , id) :
    deleted_note = Note.objects.get(pk=id)
    deleted_note.delete()
    messages.success(request, 'Note deleted successfully!')
    return redirect('home')



@login_required(login_url='/login/')
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