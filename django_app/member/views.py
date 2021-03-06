from django.contrib.auth import \
    authenticate, \
    login as django_login, \
    logout as django_logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, SignupForm

User = get_user_model()


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            django_login(request, user)
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('post:post_list')

        else:
            return HttpResponse('Login credentials invalid')

    else:
        if request.user.is_authenticated:
            return redirect('post:post_list')
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'member/login.html', context)


def logout(request):
    django_logout(request)
    return redirect('post:post_list')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.create_user()
            django_login(request, user)
            return redirect('post:post_list')

    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)
