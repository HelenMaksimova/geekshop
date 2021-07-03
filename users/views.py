from django.shortcuts import render, HttpResponseRedirect
from users.forms import LoginUserForm, RegistrationUserForm
from django.urls import reverse
from django.contrib import auth


def login(request):

    form = LoginUserForm()

    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.data['username'], password=form.data['password'])
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)

    context = {
        'title': 'GeekShop - Авторизация',
        'form': form,
    }

    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def registration(request):

    form = RegistrationUserForm()

    if request.method == 'POST':
        form = RegistrationUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)

    context = {
        'title': 'GeekShop - Регистрация',
        'form': form,
    }

    return render(request, 'users/registration.html', context)
