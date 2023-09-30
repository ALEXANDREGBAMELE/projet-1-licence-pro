from django.shortcuts import render
from django.http import HttpResponse
from .forms import MatriculeForm
from .model import Etudiant

def home(request):
    return render(request,'index.html')

def article(request):
    return render(request,'footer.html')

def contact(request):
    return render(request,'contact.html')

def formation(request):
    return render(request,'formation.html')

def resultat_bts(request):
    return render(request,'resultat_bts.html')

def resultat_message(request):
    return render(request,'resultat_message.html')



def verifier_admission(request):
    if request.method == 'POST':
        # Si le formulaire est soumis, traitez les données du formulaire
        form = MatriculeForm(request.POST)
        if form.is_valid():
            matricule_etudiant = form.cleaned_data['matricule']
            try:
                etudiant = Etudiant.objects.get(matricule_etudiant=matricule_etudiant)
                somme_des_notes = etudiant.calculer_somme_des_notes()
                est_admis = etudiant.est_admis()

                if est_admis:
                    message = f"L'étudiant avec le matricule {matricule_etudiant} est admis avec une somme de notes de {somme_des_notes}."
                else:
                    message = f"L'étudiant avec le matricule {matricule_etudiant} n'est pas admis avec une somme de notes de {somme_des_notes}."

                return render(request, 'resultat_admission.html', {'message': message})
            except Etudiant.DoesNotExist:
                message = "L'étudiant avec ce matricule n'existe pas."
                return render(request, 'resultat_admission.html', {'message': message})
    else:
        # Si le formulaire n'est pas soumis, affichez le formulaire vide
        form = MatriculeForm()
    return render(request, 'verifier_admission.html', {'form': form})
