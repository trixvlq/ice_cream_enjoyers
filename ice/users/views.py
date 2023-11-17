from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from .forms import *


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['user'], password=data['password'])
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, 'login.html', context)


def registration_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        else:
            print('something went wrong')
            return render(request, 'registration.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('home')