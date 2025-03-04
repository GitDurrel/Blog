from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from .models import User
import json

class UserTests(TestCase):

    def setUp(self):
        # Préparer des données pour les tests
        self.user = User.objects.create(nom="Jane Doe", email="jane.doe@example.com", date_inscription="2025-03-04T12:00:00")

    def test_users_list(self):
        # Test pour vérifier la liste des utilisateurs
        response = self.client.get(reverse('users_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.json())  # Vérifier que 'users' est dans la réponse JSON

    def test_add_user(self):
        # Test pour vérifier l'ajout d'un utilisateur
        data = {
            "nom": "John Doe",
            "email": "john.doe@example.com",
            "date_inscription": "2025-03-04T12:00:00"
        }
        response = self.client.post(reverse('add_user'), data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.json())  # Vérifier que la réponse contient un message
        self.assertEqual(response.json()['message'], 'Utilisateur créé avec succès')
