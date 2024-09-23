from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from application.models import User, Article
from application.forms import RegistrationForm, LoginForm, AddArticleForm


def main(request):
    articles = Article.objects.all()
    data = {"articles": articles}
    return render(request, "main.html", context=data)


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


def account(request):
    user = User.objects.get(username=request.user.username)
    articles = user.articles.all()
    data = {"articles": articles}
    return render(request, "account.html", context=data)


def add_article(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        title = request.POST.get("title")
        text = request.POST.get("text")
        topic = request.POST.get("topic")
        article = Article(title=title, text=text, topic=topic, userId=user)
        article.save()
        return redirect('/account')
    else:
        add_article_form = AddArticleForm()
        return render(request, "add_article.html", {"form": add_article_form})


def edit_article(request, article_id):
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        article = user.articles.get(id=article_id)
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        article.topic = request.POST.get("topic")
        article.save()
        return redirect('/account')
    else:
        user = User.objects.get(username=request.user.username)
        article = user.articles.get(id=article_id)
        return render(request, "edit_article.html", {"article": article})


def delete_article(request, article_id):
    user = User.objects.get(username=request.user.username)
    article = user.articles.get(id=article_id)
    article.delete()
    return redirect('/account')
