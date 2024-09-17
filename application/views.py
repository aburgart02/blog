from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, logout
from application.models import User as MyUser
from application.forms import RegistrationForm, LoginForm, LogoutForm


def index(request):
    return render(request, "index.html")


def page(request):
    print(request.user)
    return render(request, "test.html")


def registration(request):
    if request.method == "POST":
        user_login = request.POST.get("login")
        password = request.POST.get("password")
        role = "user"
        email = request.POST.get("email")

        user = MyUser(email=email, password=password)
        user.save()

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        print(user.email)

        return HttpResponse()
    else:
        registration_form = RegistrationForm()
        return render(request, "registration.html", {"form": registration_form})


def login_login(request):
    if request.method == "POST":
        m_user = MyUser.objects.get(email=request.POST.get("email"))
        #user = User.objects.create_user(m_user.login, m_user.email, m_user.password)
        login(request, m_user, backend='django.contrib.auth.backends.ModelBackend')
        print(m_user.email)
        return HttpResponse()
    else:
        login_form = LoginForm()
        return render(request, "login.html", {"form": login_form})


def logout_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponse()
    else:
        logout_form = LogoutForm()
        return render(request, "logout.html", {"form": logout_form})
