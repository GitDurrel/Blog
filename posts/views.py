from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def posts_lists(request):

    posts = Post.objects.all()
    data = list(posts.values('id', 'titre', 'contenu', 'auteur', 'date_publication'))

    return JsonResponse({'posts': data})

@csrf_exempt
def add_posts(request):
    if request.method == 'POST':
        try:
            # Charger les données envoyées dans le corps de la requête
            data = json.loads(request.body)
            
            # Créer un nouveau post
            post = Post.objects.create(
                titre=data['titre'],
                contenu=data['contenu'],
                auteur=data['auteur']
            )
            
            # Retourner une réponse JSON confirmant l'ajout
            return JsonResponse({'message': 'Post créé avec succès', 'id': post.id}, status=201)
        
        except KeyError as e:
            return JsonResponse({'error': f'Clé manquante: {str(e)}'}, status=400)
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


def posts_details(request, pk):
    # Récupérer le post en fonction de l'identifiant (pk)
    post = get_object_or_404(Post, pk=pk)
    
    # Retourner le post en format JSON
    data = {
        'id': post.id,
        'titre': post.titre,
        'contenu': post.contenu,
        'auteur': post.auteur,
        'date_publication': post.date_publication
    }
    
    return JsonResponse({'post': data})

