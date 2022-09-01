from django.shortcuts import render

# Create your views here.
def reglement_concours_pineau(request):
    head_title = "Règlement du concours de Pineau et eaux de vie"
    return render(request,'reglement_concours_pineau.html', {'head_title': head_title})


def animations_vendredi(request):
    head_title = "Animations du Vendredi"
    return render(request,'vendredi-02-09-2022.html', {'head_title': head_title})


def animations_samedi(request):
    head_title = "Animations du Samedi"
    return render(request,'samedi-03-09-2022.html', {'head_title': head_title})


def animations_dimanche(request):
    head_title = "Animations du Dimanche"
    return render(request,'dimanche-04-09-2022.html', {'head_title': head_title})


def autres_animations(request):
    head_title = "Autres Animations"
    return render(request,'autres_animations.html', {'head_title': head_title})


def animations_cheval(request):
    head_title = "Animations CHEVAL"
    return render(request,'animations_cheval.html', {'head_title': head_title})