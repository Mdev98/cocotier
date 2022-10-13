from incident.models import DeclarationIncident
from django import forms

class IncidentForm(forms.ModelForm):
    class Meta:
        model = DeclarationIncident
        fields = '__all__'