from django.shortcuts import get_object_or_404, render, redirect
from account.models import Account
from authentication.models import User
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_account(request): 
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    user_form = forms.CreationUserForm()
    account_form = forms.AccountForm()
    message = ""
    class_error = ""
    if request.method == 'POST':
        user_form = forms.CreationUserForm(request.POST)
        account_form = forms.AccountForm(request.POST)
        if all([user_form.is_valid(), account_form.is_valid()]):
            account = account_form.save()
            user = user_form.save(commit=False)
            user.account = account
            user.save()   
            return redirect('list-account')
        else:
            message = "An error has occur"
            class_error = "erreur-creation"
    return render(request, 'account/create_account.html', context={'user_form' : user_form, 'account_form' : account_form, 'message' : message, 'class_error' : class_error, 'menus' : menus})



@login_required
def list_account(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    accounts = Account.objects.all()
    

    
    return render(request, 'account/list_account.html', context={'accounts': accounts, 'menus' : menus})


@login_required
def edit_account(request,account_id): 
    account = get_object_or_404(Account, id=account_id)
    edit_form = forms.EditAccountForm(instance=account)
    delete_form = forms.DeleteAccountForm(instance=account)
    if request.method == 'POST':
        if 'edit_account' in request.POST:
            edit_form = forms.EditAccountForm(request.POST, instance=account)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('list-account')
        if 'delete_account' in request.POST:
            delete_form = forms.DeleteAccountForm(request.POST, instance=account)
           
            if delete_form.is_valid():
                
                u = delete_form.save(commit=False)
                u.is_del = True
                u.save()
                return redirect('list-account')
    return render(request, 'account/edit_account.html', context={'edit_form': edit_form, 'delete_form' : delete_form, 'account' : account})