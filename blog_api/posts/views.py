from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

# Create your views here.


def posts_lists(request):

    posts = Post.objects.all()
    data = list(posts.values('id', 'titre', 'contenu', 'auteur', 'date_publication'))
    
    return JsonResponse({'posts': data})


def add_posts():
    pass


def posts_details():
    pass
