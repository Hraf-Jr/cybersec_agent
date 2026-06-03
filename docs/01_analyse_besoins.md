# Rapport d’analyse des besoins

## 1. Introduction

### 1.1 Contexte du projet

Ce projet consiste à concevoir et développer un chatbot, ou agent conversationnel, dédié à l’apprentissage et à la sensibilisation à la cybersécurité.

L’objectif est de proposer un outil simple et accessible permettant à un utilisateur de poser des questions liées à la sécurité informatique, d’obtenir des réponses compréhensibles et d’être guidé dans l’application de bonnes pratiques numériques.

Le chatbot devra notamment traiter des sujets comme :

- les mots de passe ;
- le phishing ;
- la sécurité Wi-Fi ;
- les VPN ;
- les mises à jour ;
- les sauvegardes ;
- la messagerie sécurisée ;
- la sécurité des comptes ;
- les bonnes pratiques numériques ;
- certaines actions de sécurité liées au contexte universitaire de l’UPHF.

Le projet doit aboutir à une application fonctionnelle, démontrable, contenue dans un environnement Docker et versionnée avec Git.

### 1.2 Présentation de l’équipe

Le projet est réalisé par une équipe de cinq étudiants. Afin d’organiser efficacement le travail, les rôles sont répartis de la manière suivante.

| Membre | Rôle principal | Missions associées |
|---|---|---|
| Achraf | Coordination / Git / documentation | Organisation du dépôt Git, suivi de l’avancement, rédaction des rapports, intégration des contributions |
| Anis | Interface utilisateur | Développement de l’interface web, ergonomie, affichage de la conversation |
| Saad | Orchestrateur et logique agentique | Mise en place du routage des questions vers les agents spécialisés |
| Adnane | Agents cybersécurité et base de connaissances | Création des agents, rédaction des contenus cybersécurité, structuration des réponses |
| Othmane | Tests, Docker et déploiement | Tests fonctionnels, tests de sécurité, préparation du Docker et de la démonstration |

Cette répartition pourra évoluer au cours du projet selon les difficultés rencontrées et l’avancement de chaque partie.

---

## 2. Analyse du cahier des charges

### 2.1 Compréhension générale du besoin

Le cahier des charges demande de créer un agent conversationnel destiné à l’apprentissage et à l’éveil à la cybersécurité.

Le besoin principal est donc de fournir un outil pédagogique capable d’aider des utilisateurs non spécialistes à mieux comprendre les risques numériques et à adopter de bonnes pratiques.

Le chatbot ne doit pas seulement répondre à une question isolée. Il doit aussi être capable de gérer une conversation en plusieurs étapes, c’est-à-dire conserver un minimum de contexte pour répondre à des questions complémentaires.

Exemple :

- utilisateur : Comment reconnaître un mail de phishing ?
- chatbot : Il explique les signes d’un mail suspect.
- utilisateur : Et si j’ai déjà cliqué ?
- chatbot : Il comprend que la question concerne encore le phishing et donne des conseils adaptés.

Le projet doit également suivre une architecture agentique. Cela signifie que le système doit être organisé autour de plusieurs composants ou agents ayant chacun un rôle précis, plutôt que d’avoir un seul bloc de code qui répond à tout.

### 2.2 Besoins fonctionnels identifiés

Les besoins fonctionnels correspondent aux actions que le chatbot doit permettre.

Le système devra permettre à l’utilisateur de :

- poser une question en langage naturel ;
- obtenir une réponse claire et structurée ;
- recevoir des conseils sur les mots de passe ;
- comprendre les risques liés au phishing ;
- obtenir des recommandations pour sécuriser un réseau Wi-Fi ;
- comprendre l’utilité d’un VPN ;
- être guidé sur les bonnes pratiques de navigation, de messagerie et de gestion des comptes ;
- poser des questions liées à certaines pratiques de sécurité dans le contexte de l’UPHF ;
- poursuivre une conversation déjà commencée ;
- demander des précisions sur une réponse précédente ;
- utiliser une interface simple depuis un ordinateur ;
- visualiser l’historique de la conversation ;
- réinitialiser la conversation si nécessaire.

### 2.3 Besoins non fonctionnels identifiés

Les besoins non fonctionnels décrivent les qualités attendues de l’application.

Le chatbot devra être :

- simple à utiliser ;
- compréhensible pour un utilisateur débutant ;
- suffisamment rapide pour une démonstration fluide ;
- stable lors de la soutenance ;
- maintenable par l’équipe projet ;
- extensible afin d’ajouter de nouveaux agents ou de nouveaux thèmes ;
- sécurisé dans le traitement des demandes ;
- limité aux usages défensifs et pédagogiques ;
- exécutable dans un conteneur Docker ;
- documenté pour faciliter l’installation et l’utilisation ;
- versionné avec Git afin de permettre le travail en équipe.

### 2.4 Contraintes du cahier des charges

Le cahier des charges impose plusieurs contraintes importantes :

- le projet est réalisé en groupe ;
- le temps de développement est limité ;
- plusieurs rendus intermédiaires sont demandés ;
- l’application doit être démontrable à la fin du projet ;
- le projet doit utiliser Git pour le travail collaboratif et le versioning ;
- l’application doit être contenue dans Docker ;
- le chatbot doit suivre une architecture agentique ;
- l’application doit être accessible sur PC ou mobile ;
- le chatbot doit utiliser une saisie texte et éventuellement une commande vocale ;
- les outils utilisés sont au choix, mais il faut faire attention aux solutions payantes.

### 2.5 Premiers éléments de réponse aux points clés du cahier des charges

Pour répondre au cahier des charges, nous proposons de développer une application web nommée **CyberSec Agent**.

L’application reposera sur :

- une interface web simple ;
- un orchestrateur chargé d’analyser les questions ;
- plusieurs agents spécialisés ;
- une base de connaissances cybersécurité ;
- une mémoire conversationnelle ;
- un filtre de sécurité ;
- une couche d’intelligence artificielle locale basée sur Ollama/Mistral ;
- une exécution via Docker ;
- un dépôt GitHub pour le travail collaboratif.

L’objectif est de construire d’abord une version minimale stable, puis d’ajouter progressivement des fonctionnalités plus avancées.

La première version reposera sur des réponses contrôlées à partir d’une base de connaissances afin de garantir la fiabilité du chatbot. Ensuite, Ollama avec le modèle Mistral pourra être intégré pour reformuler ou enrichir les réponses et rendre la conversation plus naturelle.

---

## 3. Description initiale de la solution

### 3.1 Présentation générale de la solution

La solution proposée est un chatbot de sensibilisation à la cybersécurité nommé **CyberSec Agent**.

L’utilisateur accède à une interface web, saisit une question, puis reçoit une réponse adaptée au thème demandé. Le chatbot analyse la question, identifie le sujet principal et appelle l’agent spécialisé correspondant.

Les thèmes principaux prévus sont :

- cybersécurité générale ;
- mots de passe ;
- phishing ;
- sécurité Wi-Fi ;
- VPN ;
- bonnes pratiques numériques ;
- contexte UPHF ;
- filtrage des demandes dangereuses.

### 3.2 Fonctionnalités principales prévues

La version principale du projet devra contenir les fonctionnalités suivantes :

- interface de discussion ;
- saisie d’une question en langage naturel ;
- affichage de la réponse du chatbot ;
- historique de conversation ;
- réinitialisation de la discussion ;
- détection du thème de la question ;
- sélection automatique de l’agent adapté ;
- réponses pédagogiques sur la cybersécurité ;
- filtrage des demandes offensives ou dangereuses ;
- base de connaissances modifiable ;
- intégration d’une couche IA locale avec Ollama/Mistral ;
- exécution avec Docker.

### 3.3 Architecture initiale envisagée

L’architecture initiale sera organisée autour des composants suivants :

| Composant | Rôle |
|---|---|
| Interface web | Permet à l’utilisateur de poser ses questions et de lire les réponses |
| Orchestrateur | Analyse la question et choisit l’agent le plus adapté |
| Agent général cybersécurité | Répond aux questions générales |
| Agent bonnes pratiques | Donne des conseils de sécurité applicables |
| Agent phishing | Aide à reconnaître les tentatives d’hameçonnage |
| Agent réseau / Wi-Fi | Donne des conseils sur la sécurité réseau |
| Agent VPN | Explique l’utilité et les limites d’un VPN |
| Agent UPHF | Répond aux questions liées au contexte universitaire |
| Agent sécurité | Refuse les demandes offensives ou dangereuses |
| Base de connaissances | Stocke les réponses et informations de référence |
| Mémoire conversationnelle | Conserve le contexte des échanges |
| Ollama/Mistral | Reformule ou enrichit les réponses générées par les agents à l’aide d’un modèle IA local |
| Docker | Permet de lancer l’application dans un environnement contrôlé |

### 3.4 Principe de fonctionnement

Le fonctionnement général sera le suivant :

1. l’utilisateur saisit une question ;
2. l’interface transmet la question au système ;
3. l’orchestrateur analyse la question ;
4. le système vérifie si la demande est dangereuse ;
5. l’orchestrateur sélectionne l’agent adapté ;
6. l’agent récupère une réponse dans la base de connaissances ;
7. Ollama/Mistral peut reformuler ou enrichir la réponse ;
8. la réponse finale est affichée à l’utilisateur ;
9. l’échange est ajouté à l’historique de conversation.

### 3.5 Justification de l’utilisation de Ollama/Mistral

Ollama/Mistral est envisagé comme couche d’intelligence artificielle du projet.

Cependant, cette couche IA ne remplace pas toute l’architecture du chatbot. Les agents spécialisés et la base de connaissances restent au cœur du fonctionnement afin de conserver des réponses contrôlées et fiables.

Ollama permet d’exécuter localement un modèle d’intelligence artificielle. Le modèle Mistral est utilisé pour reformuler les réponses générées par les agents afin de les rendre plus naturelles et plus pédagogiques.

Ollama/Mistral sera utilisé pour :

- reformuler les réponses ;
- rendre les explications plus naturelles ;
- améliorer le ton pédagogique ;
- enrichir légèrement les réponses sans sortir du cadre défensif ;
- montrer l’intégration d’une brique IA locale dans le projet ;
- éviter de dépendre d’une API payante.

Cette approche permet de respecter l’objectif d’un chatbot agentique tout en ajoutant une dimension IA.

### 3.6 Périmètre de la version minimale

La version minimale à livrer devra absolument permettre de :

- lancer l’application ;
- poser une question ;
- obtenir une réponse cybersécurité ;
- tester plusieurs thèmes : phishing, Wi-Fi, VPN, mots de passe ;
- gérer un historique de conversation ;
- refuser une demande dangereuse ;
- lancer l’application via Docker ;
- présenter le projet à partir du dépôt GitHub.

### 3.7 Fonctionnalités secondaires possibles

Si le temps le permet, les fonctionnalités suivantes pourront être ajoutées :

- commande vocale ;
- quiz de sensibilisation ;
- mode débutant / avancé ;
- sauvegarde persistante des conversations ;
- recherche dans des documents ;
- amélioration graphique de l’interface ;
- enrichissement de la base de connaissances ;
- amélioration du prompt utilisé par Ollama/Mistral.

---

## 4. Planification et méthodologie

### 4.1 Grandes étapes du projet

Le projet sera réalisé progressivement afin d’éviter de développer une solution trop complexe dès le départ.

| Étape | Travail prévu |
|---|---|
| Étape 1 | Création du dépôt GitHub et répartition des rôles |
| Étape 2 | Analyse du cahier des charges et rédaction du rapport d’analyse |
| Étape 3 | Proposition et cadrage de la solution |
| Étape 4 | Conception technique de l’architecture |
| Étape 5 | Développement de l’interface web |
| Étape 6 | Développement de l’orchestrateur |
| Étape 7 | Développement des agents spécialisés |
| Étape 8 | Mise en place de la base de connaissances |
| Étape 9 | Ajout de la mémoire conversationnelle |
| Étape 10 | Intégration de Ollama/Mistral |
| Étape 11 | Tests fonctionnels, tests de sécurité et tests Docker |
| Étape 12 | Préparation de la démonstration et de la soutenance |

### 4.2 Méthodologie de travail au sein de l’équipe

L’équipe adoptera une méthode de travail progressive et collaborative.

Les principes retenus sont :

- travailler avec un dépôt GitHub commun ;
- faire des commits réguliers ;
- répartir les tâches par rôle ;
- éviter que plusieurs personnes modifient le même fichier en même temps ;
- faire régulièrement des points d’avancement ;
- tester l’application après chaque ajout important ;
- conserver une version minimale fonctionnelle à tout moment.

Chaque membre devra récupérer les dernières modifications avant de travailler avec la commande `git pull`, puis envoyer son travail avec `git add`, `git commit` et `git push`.

### 4.3 Outils de travail collaboratif et de suivi

Les outils envisagés sont :

| Outil | Utilisation |
|---|---|
| GitHub | Hébergement du code, versioning et collaboration |
| Git | Suivi des modifications |
| VS Code | Développement |
| Markdown | Rédaction des rapports |
| Streamlit | Interface web du chatbot |
| Python | Développement de la logique applicative |
| Ollama/Mistral | Couche IA locale pour reformulation des réponses |
| Docker | Conteneurisation de l’application |
| Pytest | Tests automatisés |
| Discord / Teams / WhatsApp | Communication rapide entre membres |

### 4.4 Objectifs spécifiques du projet

Les objectifs spécifiques doivent être précis, réalistes et mesurables.

| Objectif | Critère de validation |
|---|---|
| Créer une interface de chatbot | L’utilisateur peut saisir une question et voir une réponse |
| Mettre en place une architecture agentique | Plusieurs agents spécialisés sont présents dans le code |
| Répondre à plusieurs thèmes cybersécurité | Le chatbot répond sur phishing, mots de passe, Wi-Fi, VPN et bonnes pratiques |
| Gérer le multi-tours | Le chatbot peut prendre en compte un thème précédent |
| Ajouter un filtre de sécurité | Les demandes offensives sont refusées |
| Intégrer Ollama/Mistral | Une réponse peut être reformulée ou enrichie par une brique IA locale |
| Dockeriser l’application | L’application se lance avec Docker |
| Tester le fonctionnement | Des scénarios de tests sont documentés |
| Préparer une démonstration | Un parcours de démonstration est prêt pour la soutenance |

### 4.5 Identification et évaluation des risques

| Risque | Impact possible | Niveau | Solution envisagée |
|---|---|---|---|
| Projet trop ambitieux | Retard ou fonctionnalités incomplètes | Élevé | Prioriser une version minimale fonctionnelle |
| Mauvaise répartition des tâches | Travail désorganisé | Moyen | Définir clairement les rôles dès le début |
| Conflits Git | Perte de temps ou écrasement de fichiers | Moyen | Faire des pulls réguliers et éviter de modifier les mêmes fichiers |
| Modèle IA trop lourd | Lenteur ou impossibilité d’exécution sur certaines machines | Élevé | Prévoir une réponse JSON de secours et tester un modèle léger |
| Ollama non disponible sur une machine | La reformulation IA ne fonctionne pas | Élevé | Prévoir une réponse contrôlée de secours issue du JSON |
| Solution IA payante | Dépassement des contraintes du projet | Moyen | Privilégier les outils gratuits ou open source |
| Réponses IA incorrectes | Mauvaise information donnée à l’utilisateur | Élevé | Garder une base de connaissances contrôlée et limiter le rôle de l’IA à la reformulation |
| Réponses dangereuses | Risque éthique et non-respect du cadre défensif | Élevé | Ajouter un agent de sécurité et filtrer les demandes offensives |
| Docker non fonctionnel | Problème lors de la démonstration | Moyen | Tester Docker régulièrement pendant le développement |
| Manque de temps | Démonstration incomplète | Élevé | Avancer par étapes et garder une version fonctionnelle |
| Interface peu claire | Mauvaise expérience utilisateur | Faible | Utiliser une interface simple avec Streamlit |
| Base de connaissances insuffisante | Réponses trop limitées | Moyen | Ajouter progressivement les thèmes essentiels |

### 4.6 Risque spécifique lié à l’intelligence artificielle

L’intégration d’une intelligence artificielle peut poser plusieurs problèmes.

Un modèle IA local peut être trop lourd pour certaines machines, ce qui peut entraîner de la lenteur ou empêcher l’exécution correcte de l’application. L’utilisation d’une IA en ligne ou cloud peut aussi poser des questions de coût, de disponibilité ou de dépendance à une connexion Internet.

Pour limiter ce risque, la solution retenue sera hybride :

- la base de connaissances JSON fournira une réponse fiable de secours ;
- Ollama/Mistral sera utilisé comme couche complémentaire ;
- si Ollama n’est pas disponible, le chatbot pourra quand même fonctionner avec les réponses contrôlées ;
- le rôle de l’IA sera limité à la reformulation ou à l’enrichissement contrôlé des réponses ;
- les réponses dangereuses seront filtrées avant toute génération ;
- le modèle utilisé devra rester suffisamment léger pour fonctionner sur une machine classique.

Cette stratégie permet d’obtenir un chatbot stable tout en intégrant une vraie composante IA locale.

### 4.7 Conclusion de l’analyse

L’analyse du cahier des charges montre que le projet ne consiste pas seulement à créer un simple chatbot. Il s’agit de développer une application complète combinant une interface utilisateur, une architecture agentique, une base de connaissances, une mémoire conversationnelle, une couche IA locale et un système de filtrage de sécurité.

La priorité sera de construire une version minimale stable et démontrable, puis d’ajouter progressivement les améliorations comme Ollama/Mistral, la mémoire multi-tours avancée, Docker et les tests.

Cette organisation permet de répondre aux exigences du projet tout en limitant les risques techniques liés au temps, aux performances machine et à l’intégration de l’intelligence artificielle.