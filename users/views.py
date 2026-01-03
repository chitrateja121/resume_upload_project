import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Resume
from django.shortcuts import get_object_or_404

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return redirect('login')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'resumes': resumes})

@login_required
def upload_resume(request):
    if request.method == 'POST' and request.FILES.get('resume'):
        Resume.objects.create(
            user=request.user,
            resume=request.FILES.get('resume')
        )
        return redirect('dashboard')
    return render(request, 'upload.html')
@login_required
def delete_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)

    # delete file from media folder
    if resume.resume and os.path.isfile(resume.resume.path):
        os.remove(resume.resume.path)

    # delete database record
    resume.delete()

    return redirect('dashboard')