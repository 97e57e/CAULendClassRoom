from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CreateUserForm
from .forms import ProfileForm
from .forms import Profile
from .forms import LoginForm

from django.views.generic import TemplateView, DetailView
from django.http import HttpResponseServerError


def signup(request):
    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.profile.user_name = request.POST['user_name']
            user.profile.user_code = request.POST['user_code']
            phone_number = request.POST.get('phone_head')
            phone_number += request.POST.get('phone_body')
            print(phone_number)
            user.profile.phone_number = phone_number
            user.profile.brith = request.POST['birth']
            user.profile.department = request.POST['dept_name']
            user.profile.userType = 'student'
            user.save()
            return redirect('signup_done')
        user_form.add_error(None, '회원가입에 실패하였습니다.')
    else:
        user_form = CreateUserForm()
        profile_form = ProfileForm()
    context = {
        'user_form': user_form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    if request.method == 'POST':

        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate( username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')
    else:
        login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'signin.html', context)

def my_info(request):
    user_info = request.user
    return render(request, 'my_info.html', {'user_info' : user_info})

def edit_info(request):
    if request.method == "POST":
        return redirect("/")
    else:
        user_info = request.user
        return render(request, 'edit_info.html',{'user_info' : user_info})

def request_edit_info(request):
    user = request.user
    if user.is_authenticated:
        user.profile.birth = request.POST['edit_birth']
        user.profile.phone_number = request.POST['edit_phone_number']
        user.profile.save()
        return redirect('edit_done')
    else:
        return HttpResponseServerError('잘못된 접근입니다.')

def edit_done(request):
    return render(request, 'edit_done.html')

class signup_done(TemplateView):
    template_name = 'signup_done.html'