from django.urls import path

from users.views import logout, UserCreateView, UserLoginView, UserUpdateView, verify

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('logout/', logout, name='logout'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='profile'),
    path('verify/<email>/<activation_key>/', verify, name='verify'),
]
