# sendemail/views.py

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    head_title = "Contact"
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            societe = form.cleaned_data['societe']
            sujet = form.cleaned_data['sujet']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            entete = "Nom : " + nom + "\n" + "Prénom : " + prenom + "\n" + "Société : " + societe + "\n" + "Message :" + "\n"
            message = entete + message
            try:
                send_mail(sujet, message, email, ['foire.expo-barbezieux@wanadoo.fr', 'frederic.marzat@aliceadsl.fr'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form, 'head_title': head_title})

def successView(request):
    head_title = "Contact : email envoyé"
    return render(request, "success.html", {'head_title': head_title})