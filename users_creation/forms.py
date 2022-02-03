from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models

ADMIN = 1
PREMIUM = 2
SIMPLE = 3
USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (PREMIUM, 'PREMIUM'),
    (SIMPLE, 'SIMPLE')
)
MALE = 1
FEMALE = 2
OTHER = 3
GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
    (OTHER, 'OTHER')
)

class RegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    # date_of_birth = forms.DateField(label='', input_formats= ['%Y-%m-%d'], required=True)
    education = forms.CharField(required=True)
    country = forms.CharField(required=True)
    region = forms.CharField(required=True)
    city = forms.CharField(required=True)
    # photo = forms.ImageField(required=True)
    # label = 'buy date', input_formats = ['%Y-%m-%d'], initial = date.today)
    class Meta:
        model = models.UserCreation
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "user_type",
            "phone_number",
            "gender",
            "education",
            "country",
            "region",
            "city",
        )
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username', 'id': 'hello'}
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'email', 'id': 'em'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'password', 'id': 'hi'}
    ))


