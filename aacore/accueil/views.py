from django.shortcuts import render
import random

# Create your views here.
def index(request):
    head_title = "FOIRE EXPOSITION BARBEZIEUX"
    my_list = [1, 2]
    rand_num = random.choice(my_list)
    if rand_num == 1:
        file600 = '/static/videos/batiland600.jpg'
        file350 = '/static/videos/batiland600.jpg'
        video_pub = '/static/videos/2022/batiland.mp4'
    if rand_num == 2:
        file600 = '/static/videos/leclub600.jpg'
        file350 = '/static/videos/leclub600.jpg'
        video_pub = '/static/videos/2022/le_club.mp4'

    return render(request, 'index.html', {'head_title': head_title, 'file600': file600, 'file350': file350, 'video_pub': video_pub})


def cookies(request):
    head_title = "Cookies"
    return render(request, 'cookies.html', {'head_title': head_title})


def mentions_legales(request):
    head_title = "Mentions légales"
    site_name = "foire-exposition-barbezieux.fr"
    proprietaire = "Foire Exposition de Barbezieux"
    return render(request, 'mentions_legales.html', {'head_title': head_title, 'site_name': site_name, 'proprietaire': proprietaire})