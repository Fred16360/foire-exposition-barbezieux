from django.db import models

# Create your models here.
class VideoPartenaire(models.Model):
    titre = models.CharField(max_length=50)
    video_url = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    actif = models.BooleanField(default=1)
