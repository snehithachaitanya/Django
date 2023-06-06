from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


# Create your models here.

class horrorDB(models.Model):
    name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=30,null=True)
    message = models.CharField(max_length=30, null=True)

class actionDB(models.Model):
    name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=30,null=True)
    message = models.CharField(max_length=30, null=True)

class DevDB(models.Model):
    name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=30,null=True)
    message = models.CharField(max_length=30, null=True)

class newsDB(models.Model):
    name = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)
    page = models.PositiveIntegerField()
    side = models.CharField(max_length=30, null=True)

class pompletDB(models.Model):
    name = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)
    page = models.PositiveIntegerField()
    fold = models.CharField(max_length=30, null=True)

class instaDB(models.Model):
    name = models.CharField(max_length=20, null=True)
    ig = models.CharField(max_length=30, null=True)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
