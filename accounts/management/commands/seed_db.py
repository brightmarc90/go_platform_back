from django.core.management.base import BaseCommand
from accounts.models import Role, Permission, Role_Permission
from go_games.models import Tsumego
import os
import json

class Command(BaseCommand):
    help = 'Remplissment de la BD avec les données de base'

    def handle(self, *args, **kwargs):
        # Supprime tous les anciens enregistrements
        Role_Permission.objects.all().delete()
        Role.objects.all().delete()
        Permission.objects.all().delete()
        Tsumego.objects.all().delete()

        # Création des rôles par défaut
        roles = ["Joueur", "Editeur", "Administrateur"]
        for role in roles:
            Role.objects.create(name=role)
        # création des permissions par défaut
        tables = [
            {"name": "Role", "low_name": "role"},
            {"name": "User", "low_name": "user"},
            {"name": "Role_permission", "low_name": "role_permission"},
            {"name": "Tsumego", "low_name": "tsumego"},
                ]
        for table in tables:
            Permission.objects.create(action="CREATE_"+table['name'], description="Can create "+table['low_name'])
            Permission.objects.create(action="READ_"+table['name'], description="Can read "+table['low_name'])
            Permission.objects.create(action="UPDATE_"+table['name'], description="Can update "+table['low_name'])
            Permission.objects.create(action="DELETE_"+table['name'], description="Can delete "+table['low_name'])
        # création des role_permission
            # pour le profil joueur
        Role_Permission.objects.create(role=Role.objects.get(name="Joueur"), permission=Permission.objects.get(action="UPDATE_User"))
        Role_Permission.objects.create(role=Role.objects.get(name="Joueur"), permission=Permission.objects.get(action="CREATE_Tsumego"))
            # pour le profil éditeur
        Role_Permission.objects.create(role=Role.objects.get(name="Editeur"), permission=Permission.objects.get(action="UPDATE_User"))
        Role_Permission.objects.create(role=Role.objects.get(name="Editeur"), permission=Permission.objects.get(action="READ_Tsumego"))
        Role_Permission.objects.create(role=Role.objects.get(name="Editeur"), permission=Permission.objects.get(action="UPDATE_Tsumego"))
        Role_Permission.objects.create(role=Role.objects.get(name="Editeur"), permission=Permission.objects.get(action="DELETE_Tsumego"))
            # pour le profil admin
        for permission in Permission.objects.all():
            Role_Permission.objects.create(role=Role.objects.get(name="Administrateur"), permission=permission)
        # importation des tsumegos
        file_path = os.path.join(os.getcwd(), 'db_files', 'tsumegos.json')
        with open(file_path, 'r') as jsonFile:
            data = json.load(jsonFile)
        for tsumego in data:
            Tsumego.objects.create(problem_desc=tsumego, status=True, difficulty=tsumego['difficulty'])

        self.stdout.write(self.style.SUCCESS('BD remplie avec succès!'))