from django.shortcuts import render, redirect
from indicateur.models import IndicateurFinancier
from indicateur.forms import IFinForm
from authentication.models import User
import xml.etree.ElementTree as xml


# Create your views here.


def add_ifin(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    form = IFinForm()
    if request.method == 'POST':
        form = IFinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-ifin')
    return render(request, 'indicateur/indicateur_form.html', context={'form' : form, 'menus' : menus})

def list_ifin(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')
    ifin_list = IndicateurFinancier.objects.all()
    res = ''

    if request.GET.get('export'):
        res = export_xml_ifin(request)
        

    if para1 and para2: 
        ifin_list = IndicateurFinancier.objects.filter(date__gte=para1, date__lte=para2)


    return render(request, 'indicateur/list_indicateur.html', context={'ifin_list' : ifin_list, 'class': res, 'menus' : menus})


def edit_ifin(request, indicateur_id):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    current_ifin = IndicateurFinancier.objects.get(id=indicateur_id)
    edit_form = IFinForm(instance=current_ifin)
    if request.method == 'POST':
        edit_form = IFinForm(request.POST, instance=current_ifin)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('list-ifin')

    return render(request, 'indicateur/indicateur_form.html', context={'form' : edit_form, 'menus' : menus})

def export_xml_ifin(request):

    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')
    ifin_list = IndicateurFinancier.objects.filter(date__gte=para1, date__lte=para2)

    root = xml.Element("indicateurfinancier")
    s1 = xml.SubElement(root, 'debutperiode')
    s1.text = para1
    s2 = xml.SubElement(root, 'finperiode')
    s2.text = para2

    c1 = xml.Element("indicateurs")
    root.append(c1)
    
    

    for item in ifin_list:
        c2 = xml.Element('indicateur', code=item.code_indicateur)
        c1.append(c2)
        s3 = xml.SubElement(c2, 'intitule')
        s3.text = item.indicateur
        s4 = xml.SubElement(c2, 'valeur')
        s4.text = str(item.valeur)

    tree=xml.ElementTree(root)
    with open('test.xml', 'a+b') as files:
        tree.write(files)

    return 'success'