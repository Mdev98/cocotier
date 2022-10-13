from django.db import models
from django.conf import settings
from account.models import Role

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()


    def __str__(self):
        return f'{self.name}'


