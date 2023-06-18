from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, MusicFileForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import MusicFile
from .models import User


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form' : form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return redirect('login')
    return render(request, 'login.html')
@login_required
def Upload(request):
    if request.method == 'POST':
        form = MusicFileForm(request.POST, request.FILES)
        if form.is_valid():
            music_file = form.save(commit=False)
            music_file.user = request.user
            music_file.save()
            return redirect('homepage')
    else: 
        form = MusicFileForm

    music_file = MusicFile.objects.filter(user=request.user).last()
    context = {
        'form': form,
        'music_file': music_file,
    }
    return render(request, 'upload.html', context)

@login_required
def profile_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)

@login_required
def homepage(request):
    # Retrieve music files for the logged-in user
    user = request.user
    music_files = MusicFile.objects.filter(user=user)

    # Retrieve public music files
    public_files = MusicFile.objects.filter(visibility=MusicFile.PUBLIC)

    # Retrieve protected music files accessible to the user
    protected_files = MusicFile.objects.filter(visibility=MusicFile.PROTECTED, allowed_emails__contains=user.email)

    # Combine all music files
    all_music_files = music_files | public_files | protected_files

    context = {
        'music_files': all_music_files
    }
    return render(request, 'homepage.html', context)

def profile_view(request):
    user_profile = User.objects.get(user=request.user)
    context = {
        'user_profile': user_profile
    }
    return render(request, 'profile.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login_view(request):
    # Logic for user login
    # ...
    pass

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')