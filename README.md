# Projet Flask

## Description du Projet

Nous réalisons un projet en Flask, en groupe de deux, dans lequel nous développons une application web permettant la gestion de livres. L'application offre plusieurs fonctionnalités clés :

- **Ajout et affichage de livres** : Les utilisateurs peuvent consulter une liste de livres enregistrés dans la base de données.
- **Favoris** : Les utilisateurs connectés peuvent ajouter des livres à leur liste de favoris et consulter cette liste à tout moment.
- **Système d'authentification** : L'application dispose d'un système de login et d'enregistrement permettant aux utilisateurs de se connecter pour accéder à certaines fonctionnalités.
- **Gestion des auteurs** : Les informations sur les auteurs sont également stockées dans la base de données et peuvent être modifiées ou supprimées.

## Fonctionnalités Principales

1. **Enregistrement et connexion des utilisateurs** : Les utilisateurs doivent se connecter pour ajouter des livres à leurs favoris. L'authentification est gérée via Flask-Login.
   
2. **Gestion des livres** : Chaque utilisateur peut consulter la liste des livres disponibles, avec la possibilité de voir les détails de chaque livre.

3. **Favoris** : Les utilisateurs connectés peuvent ajouter ou retirer des livres de leurs favoris.

4. **Base de données SQLAlchemy** : Nous utilisons SQLAlchemy pour la gestion de la base de données, qui stocke :
   - Les informations des **livres** (titre, description, etc.).
   - Les informations des **auteurs** (nom, biographie, etc.).
   - Les informations sur les utilisateurs et leurs favoris.

## Technologies Utilisées

- **Flask** : Framework web pour Python.
- **SQLAlchemy** : ORM (Object Relational Mapping) pour gérer la base de données relationnelle.
- **Flask-Login** : Pour la gestion de l'authentification des utilisateurs.
- **HTML/CSS** : Pour la structure et le style de l'interface utilisateur.

## Organisation du Projet

Le projet est réalisé en groupe de deux. Nous travaillons ensemble pour développer les différentes fonctionnalités et assurer une intégration fluide de la base de données avec SQLAlchemy.

## Base de Données

Nous utilisons une base de données relationnelle avec SQLAlchemy pour stocker les informations suivantes :

- **Utilisateurs** : Informations liées aux utilisateurs (nom, identifiants, mot de passe hashé).
- **Livres** : Liste des livres disponibles avec leurs détails (titre, auteur, description).
- **Auteurs** : Informations sur les auteurs de livres.
- **Favoris** : Relation entre les utilisateurs et leurs livres favoris.

## Conclusion

Ce projet nous permet de renforcer nos compétences en développement web avec Flask et SQLAlchemy, tout en abordant des concepts clés tels que l'authentification des utilisateurs, la gestion des bases de données, et l'interaction dynamique avec l'utilisateur à travers les formulaires et les favoris.

