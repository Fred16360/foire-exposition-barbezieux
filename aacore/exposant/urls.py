from django.urls import path
from . import views 


urlpatterns = [
    path('exposants', views.exposants, name="exposants"),
    path('espaces_publicitaires', views.espaces_publicitaires, name="espaces_publicitaires"),
    path('dossier_admission', views.dossier_admission, name="dossier_admission"),
    path('dossier_autres', views.dossier_autres, name="dossier_autres"),
    path('dossier_gastronomie', views.dossier_gastronomie, name="dossier_gastronomie"),
    path('espaces_exposition', views.espaces_exposition, name="espaces_exposition"),
    path('air_libre', views.air_libre, name="air_libre"),
    path('camion_exposition', views.camion_exposition, name="camion_exposition"),
    path('stand', views.stand, name="stand"),
    path('module_3x3', views.module_3x3, name="module_3x3"),
    path('chapiteau', views.chapiteau, name="chapiteau"),
    path('liste_exposants', views.liste_exposants, name='liste_exposants'),
]