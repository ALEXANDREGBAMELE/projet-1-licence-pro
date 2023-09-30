from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Etudiant,Note,Filiere,Matiere

def liste_etudiant(request):
    return render(request,'liste-etudiant.html')

def register(request):
    return render(request,'register.html')


def enregistrer_donnees(request):
    if request.method == 'POST':
        matricule = request.POST['matricule']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        date_naissance = request.POST['date_naissance']
        telephone = request.POST['telephone']
        
        # Valider les données si nécessaire
        
        # Enregistrer les données dans la base de données
        etudiant = Etudiant(matricule=matricule, nom=nom, prenom=prenom, date_naissance=date_naissance, telephone=telephone)
        etudiant.save()
        
        # Rediriger vers une page de confirmation ou une autre vue
        # return redirect('confirmation')
    
    return render(request, 'register.html')

def detail(request, etudiant_id):
    return HttpResponse("You're looking at etudiant %s." % etudiant_id)

# def index(request):
#     liste_etudiant = Question.objects.order_by("-nom_etudiant")[:5]
#     output = ", ".join([q.question_text for q in liste_etudiant])
#     return HttpResponse(output)

