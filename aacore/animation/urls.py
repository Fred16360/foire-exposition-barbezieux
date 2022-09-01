from django.urls import path
from . import views 


urlpatterns = [
    path('reglement_concours_pineau', views.reglement_concours_pineau, name="reglement_concours"),
    path('animations_vendredi', views.animations_vendredi, name='animations_vendredi'),
    path('animations_samedi', views.animations_samedi, name='animations_samedi'),
    path('animations_dimanche', views.animations_dimanche, name='animations_dimanche'),
    path('autres_animations', views.autres_animations, name='autres_animations'),
    path('animations_cheval', views.animations_cheval, name="animations_cheval"),
]