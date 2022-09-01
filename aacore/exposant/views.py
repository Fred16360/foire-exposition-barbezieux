from django.shortcuts import render

from .models import Exposant, Categorie


# Create your views here.
def exposants(request):
    head_title = "FOIRE EXPOSITION BARBEZIEUX"
    return render(request, 'exposants.html', {'head_title': head_title})


def espaces_publicitaires(request):
    head_title = "Les espaces publicitaires"
    return render(request, 'espaces_publicitaires.html', {'head_title': head_title})


def dossier_admission(request):
    head_title = "Les dossiers d'admission"
    return render(request, 'dossier_admission.html', {'head_title': head_title})


def dossier_autres(request):
    head_title = "Dossier d'admission"
    return render(request, 'dossier_autres.html', {'head_title': head_title})


def dossier_gastronomie(request):
    head_title = "Dossier d'admission Gastronomie"
    return render(request, 'dossier_gastronomie.html', {'head_title': head_title})


def espaces_exposition(request):
    head_title = "Les espaces d'exposition"
    return render(request, 'espaces_exposition.html', {'head_title': head_title})

    
def air_libre(request):
    head_title = "Air libre"
    return render(request, 'air_libre.html', {'head_title': head_title})


def camion_exposition(request):
    head_title = "Camion d'exposition"
    return render(request, 'camion_exposition.html', {'head_title': head_title})


def stand(request):
    head_title = "Stand"
    return render(request, 'stand.html', {'head_title': head_title})


def module_3x3(request):
    head_title = "Le module 3x3"
    return render(request, 'module_3x3.html', {'head_title': head_title})


def chapiteau(request):
    head_title = "Le chapiteau"
    return render(request, 'chapiteau.html', {'head_title': head_title})


def liste_exposants(request):
    head_title = "Liste des exposants"

    list_exposants = Exposant.objects.all().order_by('categorie__numero','nom_exposant')
    list_categories = Categorie.objects.filter(is_actif=True)

    return render(request, 'liste_exposants.html', {'head_title': head_title, 'list_exposants': list_exposants, 'list_categories':list_categories})