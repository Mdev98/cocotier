"""cocotier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentication.views
import account.views
import fraud.views
import placement.views
import indicateur.views
import sfm.views
import reclamation.views
import ratio.views
import incident.views
import main.views
import monetique.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_page, name='logout'),
    path('', main.views.home, name='home'),
    path('account/add/', account.views.create_account, name='create-account'),
    path('account/list/', account.views.list_account, name='list-account'),
    path('account/edit/<int:account_id>/', account.views.edit_account, name='edit-account'),
    path('fraud/add/', fraud.views.add_fraud, name='create-fraud'),
    path('fraud/list/', fraud.views.list_fraud, name='list-fraud'),
    path('fraud/edit/<int:fraud_id>/', fraud.views.edit_fraud, name='edit-fraud'),
    path('placement/add/', placement.views.add_placement, name='add-placement'),
    path('placement/list/', placement.views.list_placement, name='list-placement'),
    path('placement/edit/<int:placement_id>/', placement.views.edit_placement, name='edit-placement'),
    path('indicateur/add/', indicateur.views.add_ifin, name='add-ifin'),
    path('indicateur/list/', indicateur.views.list_ifin, name='list-ifin'),
    path('indicateur/edit/<int:indicateur_id>/', indicateur.views.edit_ifin, name='edit-ifin'),
    path('sfm/add/', sfm.views.add_sfm, name='add-sfm'),
    path('sfm/list/', sfm.views.list_sfm, name='list-sfm'),
    path('sfm/edit/<int:sfm_id>/', sfm.views.edit_sfm, name='edit-sfm'),
    path('reclamation/add/', reclamation.views.add_reclamation, name='add-reclamation'),
    path('reclamation/list/', reclamation.views.list_reclamation, name='list-reclamation'),
    path('reclamation/edit/<int:reclamation_id>/', reclamation.views.edit_reclamation, name='edit-reclamation'),
    path('ratio/add/', ratio.views.add_ratio, name='add-ratio'),
    path('ratio/list/', ratio.views.list_ratio, name='list-ratio'),
    path('ratio/edit/<int:ratio_id>/', ratio.views.edit_ratio, name='edit-ratio'),
    path('incident/add/', incident.views.add_incident, name='add-incident'),
    path('incident/list/', incident.views.list_incident, name='list-incident'),
    path('incident/edit/<int:incident_id>/', incident.views.edit_incident, name='edit-incident'),
    path('monetique/add/', monetique.views.add_controle, name='add-controle'),
    path('monetique/list/', monetique.views.list_controle, name='list-controle'),
    path('monetique/edit/<int:monetique_id>/', monetique.views.edit_controle, name='edit-controle')
]
