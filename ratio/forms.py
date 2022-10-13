from django import forms
from ratio.models import DeclarationRatio

class RatioForm(forms.ModelForm):
    class Meta:
        model = DeclarationRatio
        fields = '__all__'