from django.db import models

# Create your models here.


class DeclarationRatio(models.Model):
    date = models.DateField(auto_now=True)
    code_identifiant_ratio = models.CharField(verbose_name="code identifiant le ratio", max_length=20)
    intitule_ratio = models.TextField(verbose_name="intitule du ratio")
    taux = models.DecimalField(verbose_name="taux", max_digits=5, decimal_places=2)