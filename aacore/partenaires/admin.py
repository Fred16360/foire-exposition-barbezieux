from django.contrib import admin

from partenaires.models import VideoPartenaire

# Register your models here.
class VideoPartenaireAdmin(admin.ModelAdmin):
    model = VideoPartenaire
    list_display = ['titre', 'video_url', 'img_url', 'actif']

admin.site.register(VideoPartenaire, VideoPartenaireAdmin)