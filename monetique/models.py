from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class ControleMonetique(models.Model):
    date = models.DateField(auto_now=True)
    valeur_initiale_monetique = models.IntegerField(verbose_name="valeur initial monnaie electronique en circulation", validators=[MinValueValidator(0)])
    nouvelle_emission_monetique = models.IntegerField(verbose_name="nouvelle emission de monnaie electronique", validators=[MinValueValidator(0)])
    destruction_monetique = models.IntegerField(verbose_name="destruction de monnaie electronique", validators=[MinValueValidator(0)])
    valeur_finale_totale_monetique = models.IntegerField(verbose_name="valeur finale totale de la monnaie electronique en circulation", validators=[MinValueValidator(0)])
    solde_compte_cantonnement = models.IntegerField(verbose_name='solde du compte de cantonnement', validators=[MinValueValidator(0)])
    solde_total_comptes_cantonnement = models.IntegerField(verbose_name='solde total des comptes de cantonnement', default=0)
    solde_niveau_comptabilite = models.IntegerField(verbose_name='solde au niveau de la comptabilite', validators=[MinValueValidator(0)])
    ecart_compte_cantonnement = models.IntegerField(verbose_name='ecart compte de cantonnement', default=0)
    ecart_comptabilite = models.IntegerField(verbose_name='ecart comptabilite', default=0)
    ecart_comptabilite_compte_cantonnement = models.IntegerField(verbose_name='ecart comptabilite comptabilite', default=0)
    nombre_transaction = models.IntegerField(verbose_name='nombre de transactions', validators=[MinValueValidator(0)])
    valeur_transaction = models.IntegerField(verbose_name='valeur des transactions', validators=[MinValueValidator(0)])
    date_operation = models.DateField(auto_now=True)
    reference = models.CharField(max_length=255)
    nature_operation = models.CharField(max_length=255)
    montant = models.IntegerField(validators=[MinValueValidator(0)])
    observations = models.TextField()

    @property
    def calcul_solde_total_comptes_cantonnement(self):
        self.solde_total_comptes_cantonnement += self.solde_compte_cantonnement
        print(self.solde_total_comptes_cantonnement)
        return self.solde_total_comptes_cantonnement

    @property
    def calcul_ecart_compte_cantonnement(self):
        self.ecart_compte_cantonnement = self.solde_total_comptes_cantonnement - self.valeur_finale_totale_monetique
        print(self.ecart_compte_cantonnement)
        return self.ecart_compte_cantonnement

    @property
    def calcul_ecart_comptabilite(self):
        self.ecart_comptabilite = self.solde_niveau_comptabilite - self.valeur_finale_totale_monetique
        print(self.ecart_comptabilite)
        return self.ecart_comptabilite

    @property
    def calcul_ecart_comptabilite_compte_cantonnement(self):
        self.ecart_comptabilite_compte_cantonnement = self.solde_total_comptes_cantonnement - self.solde_niveau_comptabilite
        print(self.ecart_comptabilite_compte_cantonnement)
        return self.ecart_comptabilite_compte_cantonnement


