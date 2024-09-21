from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from application.models import User
from application.forms import RegistrationForm, LoginForm


def main(request):
    return render(request, "main.html")


def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = User(username=username, password=password, email=email)
        user.save()

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        return redirect('/')
    else:
        registration_form = RegistrationForm()
        return render(request, "registration.html", {"form": registration_form})


def login_controller(request):
    if request.method == "POST":
        user = User.objects.get(username=request.POST.get("username"))
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/')
    else:
        login_form = LoginForm()
        return render(request, "login.html", {"form": login_form})


def logout_controller(request):
    logout(request)
    return redirect('/')
