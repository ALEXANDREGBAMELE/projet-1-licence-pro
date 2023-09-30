from django.contrib import admin
from .models import Filiere,Note,Etudiant,Matiere

# Register your models here.
admin.site.register(Etudiant)
admin.site.register(Filiere)
admin.site.register(Matiere)
admin.site.register(Note)
