from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from products.models import ProductCategory, Product
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, CategoryAdminForm, GoodAdminForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def enter_validate(user):
    return user.is_staff


@user_passes_test(enter_validate)
def index(request):
    context = {
        'title': 'Административная панель',
    }
    return render(request, 'admins/index.html', context)


class AdminUserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'
    extra_context = {'title': 'Административная панель - Пользователи'}

    @method_decorator(user_passes_test(enter_validate))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AdminUserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admins:users_read')

    @method_decorator(user_passes_test(enter_validate))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AdminUserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:users_read')

    @method_decorator(user_passes_test(enter_validate))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AdminUserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:users_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(enter_validate))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AdminCategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'
    extra_context = {'title': 'Административная панель - Категории'}

    @method_decorator(user_passes_test(enter_validate))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AdminCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = CategoryAdminForm
    template_name = 'admins/admin-categories-create.html'
    success_url = reverse_lazy('admins:categories_read')

    @method_decorator(user_passes_test(enter_validate))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AdminCategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = CategoryAdminForm
    context_object_name = 'category'
    template_name = 'admins/admin-categories-update_delete.html'
    success_url = reverse_lazy('admins:categories_read')

    @method_decorator(user_passes_test(enter_validate))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AdminCategoryDeleteView(DeleteView):
    model = ProductCategory
    context_object_name = 'category'
    template_name = 'admins/admin-categories-update_delete.html'
    success_url = reverse_lazy('admins:categories_read')

    @method_decorator(user_passes_test(enter_validate))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AdminGoodListView(ListView):
    model = Product
    template_name = 'admins/admin-goods-read.html'
    extra_context = {'title': 'Административная панель - Продукты'}

    @method_decorator(user_passes_test(enter_validate))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AdminGoodCreateView(CreateView):
    model = Product
    form_class = GoodAdminForm
    template_name = 'admins/admin-goods-create.html'
    success_url = reverse_lazy('admins:goods_read')

    @method_decorator(user_passes_test(enter_validate))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AdminGoodUpdateView(UpdateView):
    model = Product
    form_class = GoodAdminForm
    context_object_name = 'good'
    template_name = 'admins/admin-goods-update-delete.html'
    success_url = reverse_lazy('admins:goods_read')

    @method_decorator(user_passes_test(enter_validate))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AdminGoodDeleteView(DeleteView):
    model = Product
    context_object_name = 'good'
    template_name = 'admins/admin-goods-update-delete.html'
    success_url = reverse_lazy('admins:goods_read')

    @method_decorator(user_passes_test(enter_validate))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
