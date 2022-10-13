from fraud.models import Fraud
from django import forms

class FraudForm(forms.ModelForm):
    class Meta:
        model = Fraud
        fields = '__all__'