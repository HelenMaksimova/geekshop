import hashlib
import random
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User, UserProfile
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator


def validate_up_letters(value):
    up_letters_count = len([letter for letter in value if letter.isupper()])
    if up_letters_count > 2:
        raise ValidationError(
            _('%(value)s contains too many uppercase letters'),
            params={'value': value},
        )


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationUserForm(UserCreationForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя'}),
        validators=[validate_up_letters, MinLengthValidator(3, _('username is too short'))])
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self):
        user = super().save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class ProfileUserForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    birthday = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date', 'class': 'form-control py-4'}, format=('%Y-%m-%d')), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email', 'birthday')


class UserAdditionalProfileForm(forms.ModelForm):
    about_me = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4'}), required=False)
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}), required=False)
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}), choices=UserProfile.GENDER_CHOICES, required=False)
    tagline = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}), required=False)

    class Meta:
        model = UserProfile
        fields = ('about_me', 'age', 'gender', 'tagline')
