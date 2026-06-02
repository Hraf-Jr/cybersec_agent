# Proposition et cadrage du projet

## 1. Présentation de la solution proposée

Nous proposons de développer une application web nommée **CyberSec Agent**.

Cette application prendra la forme d’un chatbot dédié à l’apprentissage et à la sensibilisation à la cybersécurité. L’utilisateur pourra poser des questions en langage naturel et recevoir des réponses claires, pédagogiques et adaptées à son niveau.

Le chatbot aura pour objectif d’aider les utilisateurs à mieux comprendre les risques numériques du quotidien et à appliquer de bonnes pratiques de sécurité.

## 2. Objectifs spécifiques

Les objectifs du projet sont les suivants :

- fournir des informations simples et fiables sur la cybersécurité ;
- guider l’utilisateur dans l’application de bonnes pratiques ;
- gérer des échanges en plusieurs messages grâce à une mémoire de conversation ;
- répondre à des questions liées à certains dispositifs de sécurité de l’UPHF ;
- proposer une interface accessible depuis un PC ;
- respecter une architecture agentique ;
- fournir une application dockerisée ;
- maintenir le projet avec Git.

## 3. Périmètre fonctionnel retenu

La version principale du projet comprendra les fonctionnalités suivantes :

- interface de discussion avec un champ de saisie ;
- affichage des messages utilisateur et des réponses du chatbot ;
- traitement de questions liées aux mots de passe ;
- traitement de questions liées au phishing ;
- traitement de questions liées à la sécurité Wi-Fi ;
- traitement de questions liées aux VPN ;
- traitement de questions liées aux bonnes pratiques générales ;
- réponses sur certaines actions de cybersécurité à l’UPHF ;
- conservation du contexte de conversation ;
- architecture composée de plusieurs agents spécialisés ;
- exécution de l’application avec Docker.

## 4. Fonctionnalités bonus possibles

Si le temps le permet, les fonctionnalités suivantes pourront être ajoutées :

- commande vocale ;
- quiz de sensibilisation à la cybersécurité ;
- historique sauvegardé des conversations ;
- amélioration graphique de l’interface ;
- recherche dans des documents internes ;
- ajout d’un mode débutant / intermédiaire.

Ces fonctionnalités ne sont pas prioritaires. La priorité reste de livrer une version stable, fonctionnelle et démontrable.

## 5. Architecture agentique proposée

L’application sera organisée autour d’un orchestrateur principal chargé d’analyser la question de l’utilisateur et de sélectionner l’agent le plus adapté.

Les agents prévus sont :

- **Agent général cybersécurité** : répond aux questions générales sur les risques numériques ;
- **Agent bonnes pratiques** : donne des conseils concrets pour améliorer la sécurité ;
- **Agent phishing** : aide à reconnaître les tentatives d’hameçonnage ;
- **Agent réseau / Wi-Fi** : explique comment sécuriser une connexion réseau ;
- **Agent UPHF** : répond aux questions liées aux dispositifs de sécurité de l’université ;
- **Agent sécurité** : filtre les demandes dangereuses ou offensives.

L’objectif de cette architecture est de rendre le chatbot plus structuré, plus maintenable et plus facilement extensible.

## 6. Choix technologiques

Les technologies retenues sont :

| Besoin | Technologie proposée |
|---|---|
| Interface utilisateur | Streamlit |
| Langage principal | Python |
| Backend / logique chatbot | Python |
| Gestion des agents | Code Python modulaire |
| Base de connaissances | Fichiers JSON ou Markdown |
| Mémoire conversationnelle | Session Streamlit ou fichier local |
| Tests | Pytest et tests manuels |
| Conteneurisation | Docker |
| Versioning | Git / GitHub |

Le choix de Streamlit permet de créer rapidement une interface web simple et efficace. Python facilite la mise en place des agents, de la logique conversationnelle et des tests.

## 7. Organisation du dépôt Git

Le dépôt du projet sera organisé de la manière suivante :

```text
cybersec_agent/
│
├── app/
│   ├── main.py
│   ├── agents/
│   ├── data/
│   └── memory/
│
├── docs/
│   ├── 01_analyse_besoins.md
│   ├── 02_proposition.md
│   ├── 03_conception_technique.md
│   └── 04_developpement_tests.md
│
├── tests/
│
├── docker/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```text

## 8. Planification du projet

| Période | Travail prévu |
|---|---|
| Jour 1 | Création du dépôt Git, répartition des rôles |
| Jours 1 à 3 | Analyse des besoins |
| Jours 3 à 4 | Proposition et cadrage du projet |
| Jours 5 à 6 | Conception technique et architecture |
| Jours 6 à 8 | Développement de l’application |
| Jours 8 à 9 | Tests, correction et dockerisation |
| Jours 9 à 10 | Préparation de la démonstration et soutenance |

## 9. Risques et solutions prévues

| Risque | Conséquence | Solution |
|---|---|---|
| Projet trop ambitieux | Retard ou application incomplète | Prioriser une version minimale fonctionnelle |
| Difficulté d’intégration d’un modèle IA | Chatbot instable | Prévoir une base de réponses contrôlées |
| Mauvaise gestion du multi-tours | Réponses incohérentes | Ajouter une mémoire de conversation simple |
| Docker non fonctionnel | Problème lors de la démonstration | Tester Docker régulièrement |
| Réponses dangereuses | Problème éthique et sécurité | Ajouter un agent de filtrage |
| Mauvaise répartition du travail | Perte de temps | Définir les rôles dès le début |

## 10. Version minimale attendue

La version minimale qui devra absolument fonctionner est la suivante :

- l’utilisateur ouvre l’application ;
- il pose une question liée à la cybersécurité ;
- le chatbot identifie le thème de la question ;
- un agent spécialisé génère une réponse ;
- la réponse est affichée dans l’interface ;
- l’utilisateur peut poser une question complémentaire ;
- l’application conserve le contexte de l’échange ;
- l’application peut être lancée avec Docker.

## 11. Conclusion

La solution proposée vise à produire un chatbot simple, clair et démontrable, tout en respectant les contraintes du sujet. Le projet sera développé progressivement, en commençant par une version minimale fonctionnelle avant d’ajouter des fonctionnalités complémentaires.

Cette approche permet de limiter les risques, de garantir une démonstration stable et de répondre aux exigences principales du cahier des charges.