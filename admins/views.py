from django.shortcuts import render


def index(request):
    return render(request, 'admins/index.html')


def admin_users_read(request):
    return render(request, 'admins/admin-users-read.html')


def admin_users_create(request):
    return render(request, 'admins/admin-users-create.html')


def admin_users_update(request):
    return render(request, 'admins/admin-users-update-delete.html')


def admin_users_delete(request):
    pass
