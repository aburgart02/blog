from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=20)


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=100000)
    topic = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20)
    articleId = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
