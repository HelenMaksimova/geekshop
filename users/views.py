from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import HttpResponseRedirect, render
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
        user = form.save()
        if send_verify_mail(user):
            print('success sending')
            messages.success(self.request, 'Регистрация прошла успешно! '
                                           'Письмо с кодом активации направлено на электронную почту!')
            return HttpResponseRedirect(self.success_url)
        else:
            print('fail sending')
            messages.error(self.request, 'Что-то пошло не так! '
                                         'Не удалось отправить письмо с кодом активации!')
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


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


def verify(request, email, activation_key):
    user = User.objects.filter(email=email).first()
    if user:
        auth.logout(request)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
        return render(request, 'users/verify.html')


def send_verify_mail(user):
    link = reverse('users:verify', args=[user.email, user.activation_key])
    title = 'Подтверждение учётной записи Geekshop'
    message = f'Для подтверждения учётной записи перейдите по ссылке:\n{settings.DOMAIN}{link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
