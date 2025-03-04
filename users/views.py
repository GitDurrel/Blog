from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User

# Create your views here.

def users_lists():
    users = User.objects.all()
    data = list(users.values('id', 'nom', 'email', 'date_inscription'))

    return JsonResponse({'users': data})


@csrf_exempt 
def add_users(request):
    if request.method == 'POST':
        try:
            # Charger les données envoyées dans le corps de la requête
            data = json.loads(request.body)
            
            # Créer un nouveau utilisateur
            user = User.objects.create(
                nom=data['nom'],
                email=data['email'],
                date_inscription=data['date_inscription']
            )
            
            # Retourner une réponse JSON confirmant l'ajout
            return JsonResponse({'message': 'Utilisateur créé avec succès', 'id': user.id}, status=201)
        
        except KeyError as e:
            return JsonResponse({'error': f'Clé manquante: {str(e)}'}, status=400)
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


