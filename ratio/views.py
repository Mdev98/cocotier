from django.shortcuts import render, redirect
from authentication.models import User
from ratio.models import DeclarationRatio
from ratio.forms import RatioForm
import xml.etree.ElementTree as xml


# Create your views here.


def add_ratio(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    form = RatioForm()
    if request.method == 'POST':
        form = RatioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-ratio')
    return render(request, 'ratio/ratio_form.html', context={'form' : form, 'menus' : menus})

def list_ratio(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')

    res = ''
    ratio_list = DeclarationRatio.objects.all()

    if request.GET.get('export'):
        res = export_xml_ratio(request)
        
        

    if para1 and para2: 
        ratio_list = DeclarationRatio.objects.filter(date__gte=para1, date__lte=para2)


    return render(request, 'ratio/ratio_list.html', context={'ratio_list' : ratio_list, 'class' : res, 'menus' : menus})


def edit_ratio(request, ratio_id):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    current_ratio = DeclarationRatio.objects.get(id=ratio_id)
    edit_form = RatioForm(instance=current_ratio)
    if request.method == 'POST':
        edit_form = RatioForm(request.POST, instance=current_ratio)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('list-ratio')

    return render(request, 'ratio/ratio_form.html', context={'form' : edit_form, 'menus' : menus}) 

def export_xml_ratio(request):
    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')

    ratio_list = DeclarationRatio.objects.filter(date__gte=para1, date__lte=para2)

    root = xml.Element("declarationratios")
    c1  = xml.Element("ratios")
    
    root.append(c1)

    s01 = xml.SubElement(root, "debutperiode")
    s01.text = para1
    s02 = xml.SubElement(root, "finperiode")
    s02.text = para2
    


    for item in ratio_list:
        c1_c = xml.Element("ratio", code=item.code_identifiant_ratio)
        c1.append(c1_c)
        s1_1 = xml.SubElement(c1_c, 'intitule')
        s1_1.text = item.intitule_ratio
        s1_2 = xml.SubElement(c1_c, 'taux')
        s1_2.text = str(item.taux)

        

    tree=xml.ElementTree(root)
    with open('test.xml', 'a+b') as files:
        tree.write(files)
    
    return 'success'
