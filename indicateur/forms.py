from django import forms
from indicateur.models import IndicateurFinancier

class IFinForm(forms.ModelForm):
    class Meta:
        model = IndicateurFinancier
        fields = '__all__'