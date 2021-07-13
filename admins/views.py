from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test


def enter_validate(user):
    return user.is_staff


@user_passes_test(enter_validate)
def index(request):
    context = {
        'title': 'Административная панель',
    }
    return render(request, 'admins/index.html', context)


@user_passes_test(enter_validate)
def admin_users_read(request):
    context = {
        'title': 'Административная панель - Пользователи',
        'admin_users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(enter_validate)
def admin_users_create(request):
    form = UserAdminRegistrationForm()
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:users_read'))
    context = {
        'title': 'Административная панель - Создание пользователя',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(enter_validate)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    form = UserAdminProfileForm(instance=selected_user)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:users_read'))
    context = {
        'title': 'Административная панель - Редактирование пользовтаеля',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(enter_validate)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:users_read'))
