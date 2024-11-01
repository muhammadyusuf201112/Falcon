from django.contrib.auth.hashers import make_password
from django.forms import ModelForm, Form, CharField, PasswordInput

from apps.models import User


class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return make_password(password)


class UserLoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(max_length=30, widget=PasswordInput)