from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['nom', 'prenom']

admin.site.register(Contact, ContactAdmin)