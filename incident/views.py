from ssl import SSL_ERROR_WANT_X509_LOOKUP
from textwrap import indent
from xml.dom import minicompat
from django.shortcuts import render, redirect
from incident.forms import IncidentForm
from incident.models import DeclarationIncident
import xml.etree.ElementTree as xml
from collections import Counter 
from operator import itemgetter  
from authentication.models import User

from django.forms.models import model_to_dict

# Create your views here.


def add_incident(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    form = IncidentForm()
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)
        if form.is_valid():
            form.save()
            return redirect('list-incident')
    return render(request, 'incident/form_incident.html', context={'form' : form, 'menus' : menus})

def list_incident(request):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')
    incident_list = DeclarationIncident.objects.all()
    res = ''

    if request.GET.get('export'):
        res = export_xml_incident(request)
        

    if para1 and para2: 
        incident_list = DeclarationIncident.objects.filter(date_enregistrement__gte=para1, date_enregistrement__lte=para2)


    return render(request, 'incident/list_incident.html', context={'incident_list' : incident_list, 'class' : res, 'menus' : menus})


def edit_incident(request, incident_id):
    account = User.objects.get(id=request.user.id).account
    menus = account.role.menus.all()
    current_incident = DeclarationIncident.objects.get(id=incident_id)
    edit_form = IncidentForm(instance=current_incident)
    if request.method == 'POST':
        edit_form = IncidentForm(request.POST, instance=current_incident)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('list-incident')

    return render(request, 'incident/form_incident.html', context={'form' : edit_form, 'menus' : menus})   

#A Faire
def export_xml_incident(request):
    para1 = request.GET.get('date_debut')
    para2 = request.GET.get('date_fin')

    incidents = DeclarationIncident.objects.filter(date_enregistrement__gte=para1, date_enregistrement__lte=para2)



    # Transform incidents from django class type to simple list of object

    incident_list = [] #list of dict

    for instance in incidents:
        item = model_to_dict(instance)
        incident_list.append(item)

    # Construction of XML

    root = xml.Element("declarationincident")

    subchild_01 = xml.SubElement(root, 'debutperiode')
    subchild_01.text = para1

    subchild_02 = xml.SubElement(root, 'finperiode')
    subchild_02.text = para2


    # elt constitutif

    child_1 = xml.Element("eltconstitutif")
    root.append(child_1)

    child_1_1 = xml.Element('elt', code="DINC_1")
    child_1.append(child_1_1)
    subchild_1 = xml.SubElement(child_1_1, 'intitule')
    subchild_1.text = "Nombre d'incidents constates"
    subchild_2 = xml.SubElement(child_1_1, 'valeur')
    subchild_2.text = str(len(incident_list))

   

    child_1_2 = xml.Element('elt', code="DINC_3")
    child_1.append(child_1_2)
    subchild_1_2 = xml.SubElement(child_1_2, 'intitule')
    subchild_1_2.text = "Duree de resolution d'incidents la plus longues en minutes"
    subchild_1_3 = xml.SubElement(child_1_2, 'valeur')

    longuest = 0
    for incident in incident_list:

        time = incident['date_fin'] - incident['date_debut']
        minutes = time.total_seconds() / 60

        if minutes > longuest:
            longuest = int(minutes)

    subchild_1_3.text = str(longuest)


    child_1_3 = xml.Element('elt', code="DINC_5")
    child_1.append(child_1_3)
    subchild_1_4 = xml.SubElement(child_1_3, 'intitule')
    subchild_1_4.text = "Nombre de cartes capturees"
    subchild_1_3 = xml.SubElement(child_1_3, 'valeur')

    nbr_carte_total = 0

    for incident in incident_list:
        nbr_carte_total += incident['nombre_carte_capture']

    subchild_1_3.text = str(nbr_carte_total)
    









    # Group incident by type

    incident_by_type = Counter(map(itemgetter('type_incident'), incident_list)) 
    temp = incident_by_type.most_common() #list of tuples 
    occurences_by_type = [] #list of dict
    dict_occurences = dict((x, y) for x, y in temp)
    occurences_by_type.append(dict_occurences)

    # Fiche Descriptive

    child_2  = xml.Element("fichedescriptiveincident")
    root.append(child_2)
    for occurence in occurences_by_type:
        
        for key, value in occurence.items(): 

            child_2_1 = xml.Element("incident")
            child_2.append(child_2_1)

            subchild_1 = xml.SubElement(child_2_1, 'nombre')
            subchild_1.text = str(value)
            subchild_2 = xml.SubElement(child_2_1, 'descriptif')
            subchild_2.text = key
            subchild_3 = xml.SubElement(child_2_1, 'mesureprise')
            for incident in incident_list:
                if incident['type_incident'] == key:
                    subchild_3.text = incident['solution']

    
    # Fiche motif capture

    child_3 = xml.Element('fichemotifcapture')
    root.append(child_3)


    # Group incident by capture

    incident_by_capture = Counter(map(itemgetter('motif_capture'), incident_list)) 
    temp = incident_by_capture.most_common() #list of tuples 
    occurences_by_capture = [] #list of dict
    dict_occurences_by_capture = dict((x, y) for x, y in temp)
    occurences_by_capture.append(dict_occurences_by_capture)

    for occurence in occurences_by_capture:
        

        
        for key, value in occurence.items(): 
            print(value)
            child_3_1 = xml.Element("capture")
            child_3.append(child_3_1)
            subchild_1 = xml.SubElement(child_3_1, 'nombre')
            subchild_1.text = str(value)
            subchild_2 = xml.SubElement(child_3_1, 'motif')
            subchild_2.text = key
            
            
            for incident in incident_list:
                if incident['motif_capture'] == key and len(incident['motif_capture']) > 0:
                    subchild_3 = xml.SubElement(child_3_1, 'mesureprise')
                    subchild_3.text = incident['mesure_prise']



    tree=xml.ElementTree(root)
    with open('test.xml', 'a+b') as files:
        tree.write(files)

    




    


            


   
#{'id': 1, 'date_debut': datetime.date(2022, 2, 2), 'date_fin': datetime.date(2022, 4, 4), 'severite': 'C_2', 'type_incident': 'Vol', 'cause': 'Une cause', 'impact': 'Un impact', 'solution': 'Solution', 'nombre_carte_capture': 32, 'motif_capture': 'Motif de capture', 'mesure_prise': 'Mesure prise'}


    # incident_list = list(incidents)
    # print(type(incident_list))
    # print(incident_list[0].desc)

    # root = xml.Element("declarationincident")

    # s1 = xml.SubElement(root, 'debutperiode')
    # s1.text = para1
    # s2 = xml.SubElement(root, 'finperiode')
    # s2.text = para2

    # c1  = xml.Element("eltconstitutif")
    # c2  = xml.Element("fichedescriptiveincident")
    # c3  = xml.Element("fichemotifcapture")
    # root.append(c1)
    # root.append(c2)
    # root.append(c3)


    

    # print(occurences[0][1])

    # for incident, i, y in occurences:
    #     print(incident ,i)
        

    # for i in range(len(occurences)):
    #     print(occurences[i][i+1])


    #     c1_c = xml.Element("elt", code=incidfent.severite)
    #     c1.append(c1_c)
    #     s1_1 = xml.SubElement(c1_c,'intitule')
    #     s1_1.text = incidfent.desc

     
        

    # tree=xml.ElementTree(root)
    # with open('test.xml', 'a+b') as files:
    #     tree.write(files)

    return 'success'