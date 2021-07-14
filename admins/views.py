from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from products.models import ProductCategory, Product
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, CategoryAdminForm, GoodAdminForm
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


@user_passes_test(enter_validate)
def admin_categories_read(request):
    context = {
        'title': 'Административная панель - Категории',
        'admin_categories': ProductCategory.objects.all(),
    }
    return render(request, 'admins/admin-categories-read.html', context)


@user_passes_test(enter_validate)
def admin_categories_create(request):
    form = CategoryAdminForm()
    if request.method == 'POST':
        form = CategoryAdminForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:categories_read'))
    context = {
        'title': 'Административная панель - Создание категории',
        'form': form,
    }
    return render(request, 'admins/admin-categories-create.html', context)


@user_passes_test(enter_validate)
def admin_categories_update(request, id):
    selected_category = ProductCategory.objects.get(id=id)
    form = CategoryAdminForm(instance=selected_category)
    if request.method == 'POST':
        form = CategoryAdminForm(instance=selected_category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:categories_read'))
    context = {
        'title': 'Административная панель - Редактирование категории',
        'form': form,
        'selected_category': selected_category,
    }
    return render(request, 'admins/admin-categories-update_delete.html', context)


@user_passes_test(enter_validate)
def admin_categories_delete(request, id):
    category = ProductCategory.objects.get(id=id)
    category.delete()
    return HttpResponseRedirect(reverse('admins:categories_read'))


@user_passes_test(enter_validate)
def admin_goods_read(request):
    context = {
        'title': 'Административная панель - Продукты',
        'admin_goods': Product.objects.all(),
    }
    return render(request, 'admins/admin-goods-read.html', context)


@user_passes_test(enter_validate)
def admin_goods_create(request):
    form = GoodAdminForm()
    if request.method == 'POST':
        form = GoodAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:goods_read'))
    context = {
        'title': 'Административная панель - Создание продукта',
        'form': form,
    }
    return render(request, 'admins/admin-goods-create.html', context)


@user_passes_test(enter_validate)
def admin_goods_update(request, id):
    selected_good = Product.objects.get(id=id)
    form = GoodAdminForm(instance=selected_good)
    if request.method == 'POST':
        form = GoodAdminForm(instance=selected_good, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:goods_read'))
    context = {
        'title': 'Административная панель - Редактирование продукта',
        'form': form,
        'selected_good': selected_good,
    }
    return render(request, 'admins/admin-goods-update-delete.html', context)


@user_passes_test(enter_validate)
def admin_goods_delete(request, id):
    good = Product.objects.get(id=id)
    good.delete()
    return HttpResponseRedirect(reverse('admins:goods_read'))
