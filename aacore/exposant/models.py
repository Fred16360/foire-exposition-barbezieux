from statistics import mode
from django.db import models

# Create your models here.
class Categorie(models.Model):
    numero = models.PositiveSmallIntegerField()
    nom_id = models.CharField(max_length=30)
    nom_categorie = models.CharField(max_length=100)
    is_actif = models.BooleanField()

    class Meta:
        ordering = ('numero',)

    def __str__(self):
        return self.nom_categorie


class Exposant(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT)
    nom_exposant = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=50)
    num_tel = models.CharField(max_length=20)

    class Meta:
        ordering = ('nom_exposant',)

    def __str__(self):
        return self.nom_exposant