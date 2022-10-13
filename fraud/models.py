from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Fraud(models.Model):

    VOL     = 'VOL'
    PERTE   = 'PERTE'
    ARNAQUE = 'ARNAQUE'

    FRAUD_CHOICES = [
        (VOL, 'Vol'),
        (PERTE, 'Perte'),
        (ARNAQUE, 'Arnaque')
    ]
    client = models.CharField(verbose_name='client id', max_length=255)
    type_fraud = models.CharField(verbose_name='type de fraude', choices=FRAUD_CHOICES, max_length=7)
    date = models.DateField(auto_now=True)
    nombre_transactions = models.IntegerField(verbose_name='nombre de transaction', validators=[MinValueValidator(1)])
    montant_transactions = models.IntegerField(verbose_name='montant transactions', validators=[MinValueValidator(1)])
    dispositif_gestion = models.TextField(verbose_name='dispositif de gestion')