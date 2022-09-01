from django.shortcuts import render

# Create your views here.
def horaires_tarifs(request):
    head_title = "Horaires & Tarifs"
    return render(request, 'horaires_tarifs.html', {'head_title': head_title})


def resto_buvettes_foire(request):
    head_title = "Resto et buvettes de la Foire"
    return render(request, 'resto_buvettes_foire.html', {'head_title': head_title})


def espace_gastronomie(request):
    head_title = "L'espace gastronomie"
    return render(request, 'espace_gastronomie.html', {'head_title': head_title})

