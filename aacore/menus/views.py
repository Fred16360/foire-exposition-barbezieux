from django.shortcuts import render

# Create your views here.
def jeudi_midi(request):
    head_title = "Menu du Jeudi Midi"
    return render(request, 'jeudi_midi.html', {'hread_title': head_title})


def vendredi_midi(request):
    head_title = "Menu du Vendredi Midi"
    return render(request, 'vendredi_midi.html', {'hread_title': head_title})


def vendredi_soir(request):
    head_title = "Menu du Vendredi Soir"
    return render(request, 'vendredi_soir.html', {'hread_title': head_title})


def samedi_midi(request):
    head_title = "Menu du Samedi Midi"
    return render(request, 'samedi_midi.html', {'hread_title': head_title})


def samedi_soir(request):
    head_title = "Menu du Samedi Soir"
    return render(request, 'samedi_soir.html', {'hread_title': head_title})


def dimanche_midi(request):
    head_title = "Menu du Dimanche Midi"
    return render(request, 'dimanche_midi.html', {'hread_title': head_title})


def dimanche_soir(request):
    head_title = "Menu du Dimanche Soir"
    return render(request, 'dimanche_soir.html', {'hread_title': head_title})