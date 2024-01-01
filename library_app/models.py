from django.db import models

class Auteur(models.Model):
    code_auteur = models.AutoField(primary_key=True)
    nom_auteur = models.CharField(max_length=100)
    prenom_auteur = models.CharField(max_length=100)

class Livre(models.Model):
    code_livre = models.AutoField(primary_key=True)
    titre_livre = models.CharField(max_length=200)
    nbre_page = models.IntegerField()
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)

class Adherent(models.Model):
    code_adh = models.AutoField(primary_key=True)
    nom_adh = models.CharField(max_length=100)
    nbr_emprunts_adh = models.IntegerField()

class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    date_emprunt = models.DateField()
