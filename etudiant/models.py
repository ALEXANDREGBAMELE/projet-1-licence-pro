from django.db import models

# Create your models here.
class Filiere(models.Model):
    designation_filiere = models.CharField(max_length=255)

class Matiere(models.Model):
    designation_matiere = models.CharField(max_length=255)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, null=True)

class Etudiant(models.Model):
    matricule_etudiant = models.CharField(max_length=255)
    nom_etudiant = models.CharField(max_length=255)
    prenom_etudiant = models.CharField(max_length=255)
    age_etudiant = models.CharField(max_length=255)
    mail_etudiant = models.CharField(max_length=255)
    tel_etudiant = models.CharField(max_length=255)
    password_etudiant = models.CharField(max_length=255)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE,null=True)
    

class Note(models.Model):
    etudiants = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    matieres = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    notes = models.IntegerField(default=0)
