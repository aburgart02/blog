from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField('email adress', unique=True)
    telephone = models.CharField(max_length=20)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=100000)
    topic = models.CharField(max_length=200)
    date = models.DateTimeField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
