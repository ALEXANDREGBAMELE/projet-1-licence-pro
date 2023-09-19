from django.shortcuts import render
from django.http import HttpResponse

def liste_etudiant(request):
    return render(request,'liste-etudiant.html')