from django.db import models

# Create your models here.

class Post(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.CharField(max_length=100)


def __str__(self):
    return f"L'article {self.titre} a été publié le {date_publication} par {self.auteur}"