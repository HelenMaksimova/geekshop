from django import forms
from users.forms import RegistrationUserForm, ProfileUserForm
from users.models import User
from products.models import ProductCategory, Product


class UserAdminRegistrationForm(RegistrationUserForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(ProfileUserForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))


class CategoryAdminForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')


class GoodAdminForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control py-4'}))
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control py-4'}), max_digits=8, decimal_places=2)
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control py-4'}))
    category = forms.ModelChoiceField(
        queryset=ProductCategory.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='----Выберите категорию----')

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category')
