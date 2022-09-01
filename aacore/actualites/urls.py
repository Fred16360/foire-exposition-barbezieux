from django.urls import path
from . import views 


urlpatterns = [
    path('vie_edition_2019', views.edition_2019, name="edition_2019"),
    path('vie_edition_2022', views.edition_2022, name="edition_2022"),
    path('test', views.test, name='test'),
]