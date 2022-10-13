from os import access
from django.db import models
from django.contrib.auth.models import AbstractUser
from account.models import Account

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    superAdmin = models.BooleanField(default=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.email}'