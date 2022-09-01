from django.urls import path
from . import views 


urlpatterns = [
    path('horaires_tarifs', views.horaires_tarifs, name='horaires_tarifs'),
    path('resto_buvettes_foire', views.resto_buvettes_foire, name='resto_buvettes_foire'),
    path('espace_gastronomie', views.espace_gastronomie, name='espace_gastronomie'),

]