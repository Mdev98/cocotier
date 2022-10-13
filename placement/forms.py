from django import forms
from placement.models import PlacementFinancier

class PlacementForm(forms.ModelForm):
    class Meta:
        model = PlacementFinancier
        fields = '__all__'
        exclude = ('total',)