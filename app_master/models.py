from django.db import models

class Hobbies(models.Model):
    type_hobby = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.type_hobby

class Formateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hobbies = models.ForeignKey(Hobbies, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Apprenant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hobbies = models.ForeignKey(Hobbies, on_delete=models.CASCADE)
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom} {self.prenom}'
