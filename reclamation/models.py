from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class DeclarationReclamation(models.Model):
    date = models.DateField(auto_now=True)
    nbr_global_reclamation_enregistre = models.IntegerField(verbose_name="nombre global de reclamations enregistrées", validators=[MinValueValidator(0)], blank=True, null=True)
    nbr_global_reclamation_traite = models.IntegerField(verbose_name="nombre global de reclamations traitées", validators=[MinValueValidator(0)], blank=True, null=True)
    nbr_reclamation_enregistre = models.IntegerField(verbose_name="nombre de reclamations enregistrées", validators=[MinValueValidator(0)])
    motif_reclamation = models.TextField(verbose_name="motif de la reclamation")
    nbr_reclamation_traite = models.IntegerField(verbose_name="nombre de reclamations traitées", validators=[MinValueValidator(0)])