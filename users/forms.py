from django.contrib.auth.forms import AuthenticationForm
from users.models import User
from django import forms


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationUserForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ()
