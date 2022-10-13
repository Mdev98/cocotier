from sfm.models import ServiceFinancierMobile
from django import forms

class SFMForm(forms.ModelForm):
    class Meta:
        model = ServiceFinancierMobile
        fields = '__all__'