from django.shortcuts import render

# Create your views here.
def edition_2019(request):
    head_title = "Vie de l'édition 2019"
    return render(request, 'vie_edition_2019.html', {'head_title': head_title})


def edition_2022(request):
    head_title = "Vie de l'édition 2022"
    return render(request, 'vie_edition_2022.html', {'head_title': head_title})


def test(request):
    head_title = "TEST"
    return render(request, 'test.html', {'head_title': head_title})