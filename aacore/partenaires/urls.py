from django.urls import path
from . import views 


urlpatterns = [
    path('partenaires', views.partenaires, name="partenaires"),
    path('liste_videos', views.videos_list, name="list_videos"),
]