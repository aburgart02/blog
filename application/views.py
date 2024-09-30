from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from application.models import User, Article, Comment
from application.forms import RegistrationForm, LoginForm, AddArticleForm


def main(request):
    articles = Article.objects.all()
    return render(request, "main.html", context={"articles": articles})


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
        if user.password != request.POST.get("password"):
            return HttpResponse('Unauthorized', status=401)
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
    return render(request, "account.html", context={"articles": articles})


def get_article(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = article.comments.all()
    return render(request, "article.html", context={"article": article, "comments": comments})


def get_articles_by_topic(request, topic):
    articles = Article.objects.filter(topic=topic)
    return render(request, "articles_by_topic.html", context={"articles": articles, "topic": topic})


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


def add_comment(request, article_id):
    user = User.objects.get(username=request.user.username)
    article = Article.objects.get(id=article_id)
    text = request.POST.get("text")
    comment = Comment(text=text, articleId=article, userId=user)
    comment.save()
    return redirect('/article/' + str(article_id))


def get_profile(request, username):
    if username == request.user.username:
        return redirect('/account')
    user = User.objects.get(username=username)
    articles = user.articles.all()
    return render(request, "profile.html", context={"articles": articles, "username": username})


def delete_user(request, username):
    if not request.user.is_superuser:
        return HttpResponse('Unauthorized', status=401)
    user = User.objects.get(username=username)
    user.delete()
    return redirect('/administrator')


def edit_user(request, username):
    if not request.user.is_superuser:
        return HttpResponse('Unauthorized', status=401)
    if request.method == "POST":
        user = User.objects.get(username=username)
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.password = request.POST.get("password")
        user.save()
        return redirect('/administrator')
    else:
        user = User.objects.get(username=username)
        return render(request, "edit_user.html", {"user": user})


def administrator(request):
    if not request.user.is_superuser:
        return HttpResponse('Unauthorized', status=401)
    users = User.objects.all()
    return render(request, "admin.html", context={"users": users})
