from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Пароль')


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль')
