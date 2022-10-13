from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from placement.forms import PlacementForm
from placement.models import PlacementFinancier
import xml.etree.ElementTree as xml


def add_placement(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    form = PlacementForm()
    if request.method == 'POST':
        form = PlacementForm(request.POST)
        if form.is_valid():
            total = form.cleaned_data['depot_a_vue'] + form.cleaned_data['depot_a_terme'] + form.cleaned_data['titre_acquis']
            form.total = total
            P = form.save(commit=False)
            P.total = total
            form.save()
            return redirect('list-placement')
    return render(request, 'placement/placement_form.html', context={'form' : form, 'menus' : menus})

def list_placement(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')
    placement_list = PlacementFinancier.objects.all()
    res = ''

    if request.GET.get('export'):
        res = export_xml_placement(request)
        

    if para1 and para2: 
        placement_list = PlacementFinancier.objects.filter(date__gte=para1, date__lte=para2)


    return render(request, 'placement/list_placement.html', context={'placement_list' : placement_list, 'class' : res, 'menus' : menus})


def edit_placement(request, placement_id):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    current_placement = PlacementFinancier.objects.get(id=placement_id)
    edit_form = PlacementForm(instance=current_placement)
    if request.method == 'POST':
        edit_form = PlacementForm(request.POST, instance=current_placement)
        if edit_form.is_valid():
            
            total = edit_form.cleaned_data['depot_a_vue'] + edit_form.cleaned_data['depot_a_terme'] + edit_form.cleaned_data['titre_acquis']
            P = edit_form.save(commit=False)
            P.total = total
            P.save()
            return redirect('list-placement')

    return render(request, 'placement/placement_form.html', context={'edit_form' : edit_form, 'menus' : menus})

    
def export_xml_placement(request):

    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')

    depot_a_vue = 0
    depot_a_terme = 0
    titre_acquis = 0
    total = 0

    placement_list = PlacementFinancier.objects.filter(date__gte=para1, date__lte=para2)

    root = xml.Element("placementfinancier")
    # c1  = xml.Element("placement")
    # root.append(root)
    s1 = xml.SubElement(root, 'debutperiode')
    s1.text = para1
    s2 = xml.SubElement(root, 'finperiode')
    s2.text = para2
    
    

    for item in placement_list:
        depot_a_vue += item.depot_a_vue
        depot_a_terme += item.depot_a_terme
        titre_acquis += item.titre_acquis
        total += item.total

    s3 = xml.SubElement(root, 'depotavue')
    s3.text= str(depot_a_vue)
    s4 = xml.SubElement(root, 'depotaterme')
    s4.text = str(depot_a_terme)
    s5 = xml.SubElement(root, 'titreacquis')
    s5.text = str(titre_acquis)
    s6 = xml.SubElement(root, 'total')
    s6.text = str(total)
    tree=xml.ElementTree(root)
    with open('test.xml', 'a+b') as files:
        tree.write(files)

    return 'success'