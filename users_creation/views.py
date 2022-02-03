from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, ListView
from django.urls import reverse

from users_creation.forms import RegisterForm, LoginForm


class Register(CreateView):
    form_class = RegisterForm
    success_url = '/users/'
    template_name = 'registration.html'


class NewLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('users:user_list')

class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'user_list.html'

    def get_queryset(self):
        return User.objects.all()