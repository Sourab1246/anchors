from django.shortcuts import render,redirect
from .forms import VideoForm,RegistrationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'anchorsapp/home.html')

def user_register(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
          user=form.save()
          login(request,user)
          return redirect('home')

    else:
        form=RegistrationForm()
    return render(request,'anchorsapp/register.html',{'form':form})        

def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request,'anchorsapp/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('home')
@login_required
def top_earning_videos(request):
    return render(request, 'top_earning_videos.html')

@login_required
def user_profile(request):
    return render(request, 'user_profile.html')

@login_required
def upload_video(request):
    return render(request, 'upload_video.html')

@login_required
def notifications(request):
    return render(request, 'notifications.html')

@login_required
def settings(request):
    return render(request, 'settings.html')

@login_required
def logout_view(request):
    # Implement your logout logic here
    return redirect('home')    

def upload_video(request):
    if request.method=='POST':
        form=VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anchorsapp/home.html')
    else:
        form=VideoForm()
    return render(request,'anchorsapp/upload.html',{'form':form})            