from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import CreateUserForm
from .forms import ProfileForm
from .forms import Profile

from django.views.generic import TemplateView
from django.http import HttpResponseServerError


def signup(request):
    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.profile.user_name = request.POST['user_name']
            user.profile.user_code = request.POST['user_code']
            user.profile.phone_number = request.POST['phone_number']
            user.profile.brith = request.POST['birth']
            user.profile.department = request.POST['dept_name']
            user.save()
            print('회원가입 성공!')
            return redirect('signup_done')
        return HttpResponseServerError('회원가입에 실패했습니다.')
    else:
        user_form = CreateUserForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'user_form' : user_form})

class signup_done(TemplateView):
    template_name = 'signup_done.html'

def signin(request):
    return render(request, 'signin.html')

def my_info(request):
    return render(request, 'my_info.html')

def edit_info(request):
    return render(request, 'edit_info.html')