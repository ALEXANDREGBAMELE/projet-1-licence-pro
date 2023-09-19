from django.db import models

# Create your models here.
class Etudiant(models.Model):
    id_etudiant = models.BigIntegerField(default=0)
    nom_etudiant = models.CharField(max_length=255)
    prenom_etudiant = models.CharField(max_length=255)
    age_etudiant = models.CharField(max_length=255)
    mail_etudiant = models.CharField(max_length=255)
    tel_etudiant = models.CharField(max_length=255)
    etudiant_password = models.CharField(max_length=255)
    
class Article(models.Model):
    id_article = models.BigIntegerField(default=0)
    libelle_article = models.CharField(max_length=255)
    contenu_article = models.CharField(max_length=255)
    date_artcle = models.DateTimeField("Date publication article")