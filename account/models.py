from django.conf import settings
from django.db import models
# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50)
    menus = models.ManyToManyField(settings.MENU_MODEL, blank=True)

    def __str__(self):
        return f'{self.name}'

class Account(models.Model): 
    status = models.BooleanField(default=True)
    is_del = models.BooleanField(default=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.role.name}'



