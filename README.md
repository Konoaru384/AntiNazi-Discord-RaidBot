# AntiNazi-Discord-RaidBot
Un bot discord pour raid les discord néo-nazi/fasciste.

## Fonctionnalités principales

- **Suppression massive de salons** : Le bot supprime tous les salons existants sur le serveur cible, effaçant ainsi leur espace de communication
- **Création de salons personnalisés** : Crée automatiquement de nouveaux salons avec des messages prédéfinis pour remplacer leur contenu par le nôtre
- **Bannissement sélectif** : Bannit tous les membres du serveur à l'exception de ceux figurant sur la liste noire, désorganisant ainsi leur communauté
- **Messages privés massifs** : Envoie des messages privés aux membres avant de les bannir, s'assurant que notre message soit bien reçu

## Installation et configuration

### Prérequis

- Python 3.7 ou supérieur
- Bibliothèques requises : discord.py, asyncio
- Un compte bot Discord avec les permissions nécessaires

### Configuration des intents Discord

Pour que Fachonuker fonctionne correctement, vous devez activer les "Privileged Gateway Intents" dans le Developer Portal Discord. C'est une étape cruciale que beaucoup oublient, mais sans laquelle le bot ne pourra pas fonctionner correctement^1,2^.

Voici comment faire :

1. Rendez-vous sur https://discord.com/developers/applications
2. Sélectionnez votre application/bot
3. Allez dans l'onglet "Bot"
4. Faites défiler jusqu'à "Privileged Gateway Intents"
5. Activez les deux options suivantes^3,4^ :
   - **Server Members Intent** (nécessaire pour accéder à la liste des membres)
   - **Message Content Intent** (nécessaire pour lire le contenu des messages)
6. Sauvegardez les modifications

Ces intents sont essentiels car ils donnent au bot les permissions nécessaires pour voir les membres et lire les messages, sans quoi il ne pourrait pas accomplir sa mission^5^.

### Configuration du bot

1. Remplacez `"VOTRE_TOKEN_ICI"` par le token de votre bot Discord
2. Modifiez la liste `BLACKLISTED_IDS` pour y ajouter les ID des utilisateurs à ne pas bannir
3. Personnalisez `SALONS_CONFIG` pour définir les salons et messages à créer
4. Exécutez le script et suivez les instructions pour configurer les options de démarrage

## Utilisation

1. Invitez le bot sur le serveur cible avec les permissions nécessaires
2. Tapez `+test` dans n'importe quel canal du serveur
3. Le bot exécutera automatiquement la procédure de confinement selon les options sélectionnées

Une fois la commande lancée, Fachonuker entre en action. Il supprime d'abord tous les salons existants, puis crée les nouveaux avec vos messages personnalisés. En parallèle, il peut envoyer des messages privés aux membres et les bannir, selon les options que vous avez sélectionnées au démarrage. Le tout se déroule de manière synchronisée pour un impact maximal.

## Options de configuration

Au démarrage, Fachonuker vous proposera de configurer les options suivantes :

- **Bannissement des membres** : Choisissez si vous voulez bannir tous les membres du serveur
- **Envoi de messages privés** : Décidez si les membres recevront un MP avant d'être bannis

Ces options vous permettent de personnaliser l'intervention selon vos besoins et la situation spécifique du serveur cible.

## Personnalisation

### Messages et salons

Modifiez la liste `SALONS_CONFIG` pour personnaliser les salons créés et les messages envoyés :

```python
SALONS_CONFIG = [
    ("nom_du_salon", "message_a_envoyer"),
    ("autre_salon", "autre_message"),
]
```

C'est ici que vous pouvez laisser libre cours à votre créativité. Les messages peuvent être directs, sarcastiques ou informatifs, selon l'impact que vous souhaitez avoir.

### Liste noire

Ajoutez les ID des utilisateurs à protéger dans `BLACKLISTED_IDS` :

```python
BLACKLISTED_IDS = [
    ID_UTILISATEUR_1,
    ID_UTILISATEUR_2,
]
```

Cette fonctionnalité est importante si vous avez des alliés sur le serveur cible que vous ne voulez pas bannir accidentellement.

## Avertissement

Ce bot est conçu exclusivement pour une utilisation légale et éthique contre les serveurs propageant la haine et l'idéologie nazie. L'utilisateur est responsable de respecter les lois applicables et les conditions d'utilisation de Discord. N'utilisez ce bot que contre des serveurs qui violent clairement les conditions d'utilisation de Discord en propageant la haine raciale, l'antisémitisme ou d'autres formes de discrimination.

Fachonuker est un outil puissant, et comme tout outil, il doit être utilisé avec responsabilité. Notre objectif est de lutter contre la haine, pas de devenir ce que nous combattons.
