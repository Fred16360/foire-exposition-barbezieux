from django.urls import path
from . import views 


urlpatterns = [
    path('jeudi_midi', views.jeudi_midi, name="jeudi_midi"),
    path('vendredi_midi', views.vendredi_midi, name="vendredi_midi"),
    path('vendredi_soir', views.vendredi_soir, name="vendredi_soir"),
    path('samedi_midi', views.samedi_midi, name="samedi_midi"),
    path('samedi_soir', views.samedi_soir, name="samedi_soir"),
    path('dimanche_midi', views.dimanche_midi, name="dimanche_midi"),
    path('dimanche_soir', views.dimanche_soir, name='dimanche_soir'),
]