from django.db import models

# Create your models here.

class ServiceFinancierMobile(models.Model):
    date = models.DateField(auto_now=True)
    code_SFM = models.CharField(verbose_name="code lié au SFM", max_length=20)
    valeur = models.DecimalField(verbose_name="valeur", max_digits=5, decimal_places=2)
    details = models.TextField(verbose_name="details")
