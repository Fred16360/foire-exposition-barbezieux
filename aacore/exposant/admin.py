from django.contrib import admin
from .models import Categorie, Exposant


# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    model = Categorie
    list_display = ['numero', 'nom_id', 'nom_categorie', 'is_actif']

admin.site.register(Categorie, CategorieAdmin)


class ExposantAdmin(admin.ModelAdmin):
    model = Exposant
    list_display = ['nom_exposant', 'adresse', 'code_postal', 'ville', 'num_tel']

admin.site.register(Exposant, ExposantAdmin)