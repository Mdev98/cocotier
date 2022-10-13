from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from account.models import Account
from fraud.models import Fraud
from incident.models import DeclarationIncident
from indicateur.models import IndicateurFinancier
from placement.models import PlacementFinancier
from ratio.models import DeclarationRatio
from sfm.models import ServiceFinancierMobile
from reclamation.models import DeclarationReclamation

# Create your views here.

@login_required
def home(request):

    
    frauds = { 'name': 'Déclaration de fraude' , 'number': len(Fraud.objects.all())}
    incidents = {'name' : "Déclaration d'incident", 'number' : len(DeclarationIncident.objects.all())}
    indicateurs = {'name' : "Indicateur Financier",  'number' : len(IndicateurFinancier.objects.all())}
    placements = {'name' : "Placement Financier" ,'number' : len(PlacementFinancier.objects.all())}
    ratios = {'name' : "Déclaration ration", 'number' : len(DeclarationRatio.objects.all())}
    sfm = {'name' : "Service Financier Mobile", 'number' : len(ServiceFinancierMobile.objects.all())}
    reclamations = {'name' : 'Déclaration reclamation', 'number' : len(DeclarationReclamation.objects.all())}

    dashboard_data = [frauds, incidents, indicateurs, placements, ratios, sfm, reclamations]

    print(dashboard_data)
    
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()

    accounts = Account.objects.all()
    del_accounts = Account.objects.filter(is_del=True)
    inactif_accounts = Account.objects.filter(status=False)
    
    return render(request, 'main/home.html', context={'menus' : menus, 'accounts': accounts, 'del_accounts' : del_accounts, 'inactif_accounts': inactif_accounts, 'dashboard_data' : dashboard_data})