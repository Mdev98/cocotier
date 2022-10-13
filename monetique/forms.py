from django import forms
from monetique.models import ControleMonetique

class Monetique(forms.ModelForm):
    class Meta:
        model = ControleMonetique
        exclude = ('ecart_compte_cantonnement', 'ecart_comptabilite', 'ecart_comptabilite_compte_cantonnement', 'solde_total_comptes_cantonnement',)