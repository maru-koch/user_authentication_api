from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length= 200, unique=True)
    password_1 = models.CharField(max_length=100)
    password_2 = models.CharField(max_length= 100)



