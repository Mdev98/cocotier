from django import forms
from reclamation.models import DeclarationReclamation

class ReclamationForm(forms.ModelForm):
    class Meta:
        model = DeclarationReclamation
        fields = ('nbr_reclamation_enregistre', 'motif_reclamation', 'nbr_reclamation_traite')