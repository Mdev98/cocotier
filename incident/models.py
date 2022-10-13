from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class DeclarationIncident(models.Model):
    date_enregistrement = models.DateField(auto_now=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    severite = models.CharField(verbose_name='severite', max_length=20)
    type_incident = models.CharField(verbose_name='type incident', max_length=255)
    cause = models.CharField(verbose_name='cause', max_length=255)
    impact = models.CharField(verbose_name="impacte", max_length=255)
    solution = models.TextField(verbose_name="solution")
    nombre_carte_capture = models.IntegerField(verbose_name="nombre de carte capturée", validators=[MinValueValidator(0)], blank=True, null=True, default=0)
    motif_capture = models.TextField(verbose_name="motif de capture", blank=True, null=True)
    mesure_prise = models.TextField(verbose_name="mesure prise", blank=True, null=True)