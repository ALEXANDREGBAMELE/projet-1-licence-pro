from django.urls import path

from . import views

urlpatterns = [
    path("", views.liste_etudiant, name="liste"),
    path("register", views.register, name="register"),
    path("<int:etudiant_id>/", views.detail, name="detail"),

]
