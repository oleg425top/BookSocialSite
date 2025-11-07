from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from account.forms import LoginForm, UserRegistrationForm, UserEditionForm, ProfileEditionForm
from account.models import Profile


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section':'dashboard', 'title':'Главная страница'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    context = {
        'form': form,
        'title': 'Вход в аккаунт',
    }
    return render(request, 'account/login.html', context=context)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])  # Исправлено: password
            new_user.save()
            Profile.objects.create(user=new_user)
            context = {
                'new_user': new_user,
                'title': f'Добро пожаловать {new_user.first_name}'  # Исправлено: убрана лишняя буква
            }
            return render(request, 'account/registration/register_done.html', context)
    else:
        user_form = UserRegistrationForm()

    context = {
        'user_form': user_form,
        'title': 'Регистрация'  # Исправлено: убрана лишняя буква
    }
    return render(request, 'account/registration/register.html', context)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditionForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditionForm(instance=request.user.profile,
                                          data=request.POST,
                                          files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditionForm(instance=request.user)
        profile_form = ProfileEditionForm(instance=request.user.profile)
    context = {
        'title':'Редактировать: ',
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request, 'account/edit.html', context=context)