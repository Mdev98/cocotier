
from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Account, Role

class CreationUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')
        help_texts = {
            'username': None,
            'email': None,
            'password': None
        }

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('role',)


class EditAccountForm(forms.ModelForm):
    edit_account = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Account
        fields = ('status',)

        
class DeleteAccountForm(forms.ModelForm):
    delete_account = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Account
        fields = []

