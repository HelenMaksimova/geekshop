from django.shortcuts import render, HttpResponseRedirect
from users.forms import LoginUserForm, RegistrationUserForm, ProfileUserForm
from users.models import User
from django.urls import reverse, reverse_lazy
from django.contrib import auth, messages
from baskets.models import Basket
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class UserLoginView(LoginView):
    form_class = LoginUserForm
    extra_context = {'title': 'GeekShop - Авторизация'}
    template_name = 'users/login.html'


class UserCreateView(CreateView):
    model = User
    form_class = RegistrationUserForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login', )
    extra_context = {'title': 'GeekShop - Регистрация'}

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Регистрация прошла успешно!')
        return HttpResponseRedirect(self.success_url)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = ProfileUserForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(
            {
                'title': 'GeekShop - Личный кабинет',
                'baskets': Basket.objects.filter(user=self.request.user),
            }
        )
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Профиль успешно изменён!')
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
