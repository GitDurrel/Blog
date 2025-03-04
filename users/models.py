from django.db import models

# Create your models here.

class User(models.Model):
    nom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_inscription = models.DateTimeField()


def __str__(self):
    return f"{self.nom} ({self.email})"