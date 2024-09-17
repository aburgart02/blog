from django import forms


class RegistrationForm(forms.Form):
    login = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    passwordConfirm = forms.CharField()


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()


class LogoutForm(forms.Form):
    lorem_ipsum = forms.CharField()