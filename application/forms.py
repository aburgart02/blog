from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    passwordConfirm = forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
