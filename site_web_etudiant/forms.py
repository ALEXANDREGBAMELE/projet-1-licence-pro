from django import forms

class MatriculeForm(forms.Form):
    matricule = forms.CharField(label='Matricule de l\'étudiant', max_length=255)
