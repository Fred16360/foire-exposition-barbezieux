from django.db import models

# Create your models here.
class Contact(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    societe = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=50)
    sujet = models.CharField(max_length=50)
    message = models.TextField()
