
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Folder, File
from .forms import FolderForm, FileForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required


@login_required
def file_list(request):
    folders = Folder.objects.filter(parent_folder=None)
    files = File.objects.filter(parent_folder=None)
    return render(request, 'file_manager/file_list.html', {'folders': folders, 'files': files})

@login_required
def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            parent_folder_id = form.cleaned_data.get('parent_folder', None)
            parent_folder = None

            if parent_folder_id:
                parent_folder = Folder.objects.get(id=parent_folder_id)

            folder = Folder(name=name, parent_folder=parent_folder)
            folder.save()
            messages.success(request, 'Folder created successfully!')
            return redirect('file_list')

    else:
        form = FolderForm()

    return render(request, 'file_manager/create_folder.html', {'form': form})

@login_required
def create_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.owner = request.user
            file.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('file_list')

    else:
        form = FileForm()

    return render(request, 'file_manager/create_file.html', {'form': form})

def delete_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)

    if request.method == 'POST':
        folder.delete()
        messages.success(request, 'Folder deleted successfully!')
        return redirect('file_list')

    return render(request, 'file_manager/delete_folder.html', {'folder': folder})

def delete_file(request, file_id):
    file = get_object_or_404(File, id=file_id)

    if request.method == 'POST':
        file.delete()
        messages.success(request, 'File deleted successfully!')
        return redirect('file_list')

    return render(request, 'file_manager/delete_file.html', {'file': file})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('file_list') 

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('file_list')  # Redirect to the file_list view after login

    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
