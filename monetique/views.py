from msilib.schema import Control
from django.shortcuts import render, redirect
from monetique.forms import Monetique
from monetique.models import ControleMonetique
from authentication.models import User

# Create your views here.

def add_controle(request):
    form = Monetique()
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    if request.method == 'POST':
        form = Monetique(request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)

        if form.is_valid():
            monetique = form.save(commit=False)
            monetique.solde_total_comptes_cantonnement = monetique.calcul_solde_total_comptes_cantonnement
            monetique.ecart_compte_cantonnement = monetique.calcul_ecart_compte_cantonnement
            monetique.ecart_comptabilite = monetique.calcul_ecart_comptabilite
            monetique.ecart_comptabilite_compte_cantonnement = monetique.calcul_ecart_comptabilite_compte_cantonnement
            form.save()
            return redirect('list-controle')
    return render(request, 'monetique/monetique_form.html', context={'form': form, 'menus' : menus})

def list_controle(request):

    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    monetiques = ControleMonetique.objects.all()

    return render(request, 'monetique/monetique_list.html', context={'monetiques' : monetiques, 'menus': menus})

def edit_controle(request, controle_id):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()

    current_controle = ControleMonetique.objects.get(id=controle_id)
    edit_form = ControleMonetique(instance=current_controle)

    if request.method == 'POST':
        edit_form = ControleMonetique(request.POST, instance=current_controle)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('edit-controle')

    return render(request, 'monetique/monetique_form.html', context={'form' : edit_form, 'menus' : menus})

def export_xml(request):
    pass