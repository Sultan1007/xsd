from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class New(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    photo = models.ImageField(upload_to="photo")
    link = models.CharField(max_length=200)
    date = models.DateField()


class Law(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    category = models.ForeignKey("Category", null=True, on_delete=models.CASCADE)
    date = models.DateField()


class Publication(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=300)
    category = models.ForeignKey("Category", null=True, on_delete=models.CASCADE)
    date = models.DateField()


class Favourite(models.Model):
    bools = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    link_to_news = models.ForeignKey(New, null=True, on_delete=models.CASCADE, related_name="favourite")


class Category(models.Model):
    title = models.CharField(max_length=200)
