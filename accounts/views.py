from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def my_info(request):
    return render(request, 'my_info.html')

def edit_info(request):
    return render(request, 'edit_info.html')