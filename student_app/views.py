from django.http import request
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import *


# Create your views here.



def homepage(request):
    return render(request, 'homepage.html')


def number_pattern(request):
    return render(request, 'numberpatterns.html')

def register_user(request):

    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'registerpage.html', {'form' : form})


def base(request):
    return render(request, 'base.html')
