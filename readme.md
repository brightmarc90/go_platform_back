# Projet Tsumego - API
## Description
Le projet Tsumego - API est la partie back-end d'une plateforme web destinée au jeu de go. Cette API est développée en **django** un framework **python**.

L'objectif de cette plateforme est de vulgariser le jeu de go en mettant a disposition des amateurs et des passionnés des ressources et des outils.

Les endpoints de cette API doivent permettre via une application front :
- de créer des nouveaux membres
- d'authentifier les membres
- de proposer une bibliothèque de problèmes de jeu de go (tsumego)
- de résoudre des tsumegos ou de donner la solution aux visiteurs
- aux membres de proposer de nouveaux problèmes à ajouter à la bibliothèque
- aux administrateurs de valider les problèmes soumis et de les publier ou non
- d'accéder à des statistiques sur des parties de jeu de go déjà jouées sur différents tournois en combinant plusieurs critères.
## Installation
**1-** Cloner le dépôt
```bash
git clone https://github.com/brightmarc90/go_platform_back.git
cd go_plateform_back
```
**2-** Créer votre environnement de travail
```bash
python -m venv venv
```
**3-** Activez votre environnement de travail 
sous Windows
```bash
venv\Scripts\activate
```
sous Mac ou Linux
```bash
source venv/bin/activate
```
**4-** Installer les dépendances
```bash
pip install -r requirements.txt
```
## Configuration
**1-** Créer une nouvelle base deonnée dans votre Mysql nommée: **``go_platform_db``** 
**2-** Lancer les migration pour créer les tables de la base de données
```bash
python manage.py migrate
```
**3-** Lancer la commande suivante pour peupler la base de données
```bash
python manage.py seed_db
```
## Utilisation
Pour lancer le projet exécutez la commande suivante
```bash
python manage.py runserver
```
Pour accéder à la documentation des endpoints de l'API ajouter `/swagger` à l'url de base de l'API.
## Auteurs
- **Marc AKPOTO-K** - [Github](https://github.com/brightmarc90)
- **Jonathan MBAYA** - [Github](https://github.com/JonathanMbaya)
- **Fanna IBRAHIM** - [Github](https://github.com/IFDevM)
## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENCE](https://github.com/brightmarc90/go_platform_back/blob/main/LICENSE) pour plus de détails.