from django.shortcuts import render, redirect
from reclamation.forms import ReclamationForm
from authentication.models import User
from reclamation.models import DeclarationReclamation
import xml.etree.ElementTree as xml

# Create your views here.


def add_reclamation(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    form = ReclamationForm()
    if request.method == 'POST':
        form = ReclamationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-reclamation')
    return render(request, 'reclamation/reclamation_form.html', context={'form' : form, 'menus' : menus})

def list_reclamation(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')
    reclamation_list = DeclarationReclamation.objects.all()
    res = ''
    for l in reclamation_list:
        print(l.nbr_reclamation_enregistre)

    if request.GET.get('export'):
        res = export_xml_reclamation(request)
        
        

    if para1 and para2: 
        reclamation_list = DeclarationReclamation.objects.filter(date__gte=para1, date__lte=para2)


    return render(request, 'reclamation/reclamation_list.html', context={'reclamation_list' : reclamation_list, 'class' : res, 'menus' : menus})


def edit_reclamation(request, declaration_id):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    current_reclamation = DeclarationReclamation.objects.get(id=declaration_id)
    edit_form = DeclarationReclamation(instance=current_reclamation)
    if request.method == 'POST':
        edit_form = DeclarationReclamation(request.POST, instance=current_reclamation)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('list-placement')

    return render(request, 'reclamation/reclamation_form.html', context={'edit_form' : edit_form, 'menus' : menus}) 

def export_xml_reclamation(request):
    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')

    nbr_global_reclamation_enregistre = 0
    nbr_global_reclamation_traite = 0
    incident_list = DeclarationReclamation.objects.filter(date__gte=para1, date__lte=para2)

    root = xml.Element("declarationreclamation")
    c1  = xml.Element("declaration")
    c2  = xml.Element("detailsreclamation")
    
    root.append(c1)
    root.append(c2)

    s01 = xml.SubElement(c1, "debutperiode")
    s01.text = para1
    s02 = xml.SubElement(c1, "finperiode")
    s02.text = para2
    


    for item in incident_list:

        nbr_global_reclamation_enregistre += item.nbr_reclamation_enregistre
        nbr_global_reclamation_traite += item.nbr_reclamation_traite

        c2_c = xml.Element("reclamation")
        c2.append(c2_c)
        s2_1 = xml.SubElement(c2_c, 'nbenregistre')
        s2_1.text = str(item.nbr_reclamation_enregistre)
        s2_2 = xml.SubElement(c2_c, 'motif')
        s2_2.text = item.motif_reclamation
        s2_3 = xml.SubElement(c2_c, 'nbtraite')
        s2_3.text = str(item.nbr_reclamation_traite)

    s03 = xml.SubElement(c1, "nbenregistre")
    s03.text = str(nbr_global_reclamation_enregistre)
    s04 = xml.SubElement(c1, "nbtraite")
    s04.text = str(nbr_global_reclamation_traite)

    return 'success'