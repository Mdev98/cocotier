from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fraud.forms import FraudForm
from fraud.models import Fraud
from authentication.models import User
import xml.etree.ElementTree as xml

# Create your views here.

@login_required
def add_fraud(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    form = FraudForm()
    if request.method == 'POST':
        form = FraudForm(request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)
        if form.is_valid():
            form.save()
            return redirect('list-fraud')
    return render(request, 'fraud/fraud_form.html', context={'form' : form, 'menus' : menus})

@login_required
def list_fraud(request):

    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()

    fraud_list = Fraud.objects.all()
    res = ''

    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')
    

    if request.GET.get('export'):
        res = export_xml_fraud(request)

    if para1 and para2: 
        fraud_list = Fraud.objects.filter(date__gte=para1, date__lte=para2)


    return render(request, 'fraud/list_fraud.html', context={'fraud_list' : fraud_list, 'class' : res, 'menus' : menus})

@login_required
def edit_fraud(request, fraud_id):

    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()

    current_fraud = Fraud.objects.get(id=fraud_id)
    edit_form = FraudForm(instance=current_fraud)

    if request.method == 'POST':
        edit_form = FraudForm(request.POST, instance=current_fraud)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('list-fraud')

    return render(request, 'fraud/fraud_form.html', context={'form' : edit_form, 'menus' : menus})

def export_xml_fraud(request):

    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')

    nb_transaction = 0
    val_transaction = 0

    fraud_list = Fraud.objects.filter(date__gte=para1, date__lte=para2)
    

    root = xml.Element("declarationfraude")
    c1  = xml.Element("declaration")
    root.append(c1)
    s1 = xml.SubElement(c1, 'debutperiode')
    s1.text = para1
    s2 = xml.SubElement(c1, 'finperiode')
    s2.text = para2
    c2  = xml.Element("fichedescriptive")
    root.append(c2)
    

    for item in fraud_list:
        c2_c1 = xml.Element("typefraude", code=item.type_fraud)
        c2.append(c2_c1)
        nb_transaction += item.nombre_transactions
        val_transaction += item.montant_transactions
        s4 = xml.SubElement(c2_c1, 'description')
        s4.text= item.type_fraud
        s5 = xml.SubElement(c2_c1, 'nbtransaction')
        s5.text= str(item.nombre_transactions)
        s6 = xml.SubElement(c2_c1, 'valeurtransaction')
        s6.text= str(item.montant_transactions)
        s7 = xml.SubElement(c2_c1, 'dispositifgestion')
        s7.text= item.dispositif_gestion


    
    s3 = xml.SubElement(c1, 'nbtransaction')
    s3.text= str(nb_transaction)
    s4 = xml.SubElement(c1, 'valeurtransaction')
    s4.text = str(val_transaction)

    tree=xml.ElementTree(root)
    with open('test.xml', 'a+b') as files:
        tree.write(files)

    return 'success'