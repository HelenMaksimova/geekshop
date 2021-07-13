from django.shortcuts import render
from users.models import User


def index(request):
    return render(request, 'admins/index.html')


def admin_users_read(request):
    context = {
        'title': 'Административная панель - Пользователи',
        'admin_users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    return render(request, 'admins/admin-users-create.html')


def admin_users_update(request, id):
    return render(request, 'admins/admin-users-update-delete.html')


def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
