# sendemail/forms.py

from django import forms
from django.forms import ModelForm
from sendemail.models import Contact
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    nom = forms.CharField(
        label="Nom",
        required=True,
        widget=forms.TextInput(attrs={
            "style": "width:100%"
        })
    )
    prenom = forms.CharField(
        label="Prénom",
        required=True,
        widget=forms.TextInput(attrs={
            "style": "width:100%"
        })
    )
    societe = forms.CharField(
        label="Société",
        required=False,
        widget=forms.TextInput(attrs={
            "style": "width:100%"
        })
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.TextInput(attrs={
            "style": "width:100%"
        })
    )
    sujet = forms.CharField(
        label="Sujet",
        required=True,
        widget=forms.TextInput(attrs={
            "style": "width:100%"
        })
    )
    message = forms.CharField(
        label="Message",
        required=True,
        widget=forms.Textarea(attrs={
            "style": "width:100%"
        })
    )

    captcha = ReCaptchaField(
        label="",
        widget=ReCaptchaV2Checkbox(attrs={
            "style": "margin-top:15px"
        })
        )

