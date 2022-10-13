from django.shortcuts import render, redirect
from sfm.models import ServiceFinancierMobile
from authentication.models import User
from sfm.forms import SFMForm
import xml.etree.ElementTree as xml

# Create your views here.

def add_sfm(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    form = SFMForm()
    if request.method == 'POST':
        form = SFMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-sfm')
    return render(request, 'sfm/form_sfm.html', context={'form' : form, 'menus' : menus})

def list_sfm(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')
    sfm_list = ServiceFinancierMobile.objects.all()
    res = ''

    if request.GET.get('export'):
        res = export_xml_sfm(request)
        
        

    if para1 and para2: 
        sfm_list = ServiceFinancierMobile.objects.filter(date__gte=para1, date__lte=para2)


    return render(request, 'sfm/list_sfm.html', context={'sfm_list' : sfm_list, 'class' : res, 'menus' : menus})


def edit_sfm(request, sfm_id):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    current_sfm = ServiceFinancierMobile.objects.get(id=sfm_id)
    edit_form = SFMForm(instance=current_sfm)
    if request.method == 'POST':
        edit_form = SFMForm(request.POST, instance=current_sfm)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('list-sfm')

    return render(request, 'sfm/form_sfm.html', context={'form' : edit_form, 'menus' : menus}) 




def export_xml_sfm(request):
    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')

    sfm_list = ServiceFinancierMobile.objects.filter(date__gte=para1, date__lte=para2)

    root = xml.Element("declarationsfm")

    s01 = xml.SubElement(root, "debutperiode")
    s01.text = para1
    s02 = xml.SubElement(root, "finperiode")
    s02.text = para2

    c1  = xml.Element("statistiques")
    
    root.append(c1)
    
    for item in sfm_list:
        c1_c = xml.Element("sfm", code=item.code_SFM)
        c1.append(c1_c)
        s1_1 = xml.SubElement(c1_c, 'valeur')
        s1_1.text = str(item.valeur)
        s1_2 = xml.SubElement(c1_c, 'details')
        s1_2.text = str(item.details)

        

    tree=xml.ElementTree(root)
    with open('test.xml', 'a+b') as files:
        tree.write(files)
    
    return 'success'