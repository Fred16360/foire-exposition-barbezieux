"""aacore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from accueil import views

urlpatterns = [
    path('admin1fm2dm3am/', admin.site.urls),
    path('', views.index, name="index"),
    path('animation/', include('animation.urls')),
    path('exposant/', include('exposant.urls')),
    path('partenaires/', include('partenaires.urls')),
    path('actualites/', include('actualites.urls')),
    path('infosfoire/', include('infosfoire.urls')),
    path('menus/', include('menus.urls')),
    path('djga/', include('google_analytics.urls')),
    path('sendemail/', include('sendemail.urls')),
    path('cookies', views.cookies, name="cookies"),
    path('mentions-legales', views.mentions_legales, name="mentions_legales"),
]
