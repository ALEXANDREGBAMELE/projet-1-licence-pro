from django.urls import path

from . import views

urlpatterns = [
    path("", views.liste_etudiant, name="liste")
    
]