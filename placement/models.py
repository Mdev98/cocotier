from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class PlacementFinancier(models.Model):
    date = models.DateField(auto_now=True)
    depot_a_vue = models.IntegerField(verbose_name='depot a vue', validators=[MinValueValidator(1)])
    depot_a_terme = models.IntegerField(verbose_name='depot a terme', validators=[MinValueValidator(1)])
    titre_acquis = models.IntegerField(verbose_name='titre acquis', validators=[MinValueValidator(1)])
    total = models.IntegerField(verbose_name='total', validators=[MinValueValidator(1)], blank=True, null=True)