from django.shortcuts import render
from partenaires.models import VideoPartenaire
import random

# Create your views here.
def partenaires(request):
    head_title = "Nos partenaires"
    return render(request, 'partenaires.html', {'head_title': head_title})


def videos_list(request):
    head_title = "Vidéos de nos partenaires"

    list_video = VideoPartenaire.objects.filter(actif=True)
    '''
    list_video_id = []
    for video in list_video:
        list_video_id.append(video.id)

    random_video_id = random.choice(list_video_id)
    random_video = VideoPartenaire.objects.filter(id=random_video_id)
    '''
    return render(request, 'videos.html', {'head_title': head_title, 'list_video':list_video})