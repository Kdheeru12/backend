from django.contrib.auth.models import User

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    website = models.CharField(max_length=150)