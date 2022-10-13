from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class IndicateurFinancier(models.Model):
    date = models.DateField(auto_now=True)
    code_indicateur = models.CharField(verbose_name='code indicateur', max_length=20)
    indicateur = models.CharField(verbose_name='indicateur', max_length=150)
    valeur = models.IntegerField(verbose_name='valeur', validators=[MinValueValidator(1)])