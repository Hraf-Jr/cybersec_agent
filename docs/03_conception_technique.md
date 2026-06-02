# Conception et spécifications techniques

## 1. Présentation générale

Ce document présente la conception technique de l’application **CyberSec Agent**.

L’objectif est de décrire comment la solution proposée sera construite techniquement. Cette partie permet de passer des besoins fonctionnels à une architecture concrète, avec les choix technologiques, l’organisation du code, les agents utilisés, la gestion de la mémoire, la sécurité et les tests prévus.

L’application prendra la forme d’un chatbot de sensibilisation à la cybersécurité, accessible depuis une interface web simple.

## 2. Objectifs techniques

Les objectifs techniques du projet sont les suivants :

- créer une application web utilisable sur PC ;
- permettre à l’utilisateur de poser des questions en langage naturel ;
- organiser le chatbot autour de plusieurs agents spécialisés ;
- gérer une conversation multi-tours ;
- utiliser une base de connaissances simple ;
- sécuriser les réponses du chatbot ;
- rendre l’application exécutable avec Docker ;
- organiser le code de manière claire et maintenable.

## 3. Architecture générale

L’application sera organisée autour de plusieurs composants :

- une interface utilisateur ;
- un orchestrateur ;
- plusieurs agents spécialisés ;
- une base de connaissances ;
- une mémoire conversationnelle ;
- un module de sécurité.

L’utilisateur saisit une question dans l’interface. La question est ensuite transmise à l’orchestrateur, qui analyse la demande et sélectionne l’agent le plus adapté. L’agent produit une réponse à partir de ses règles et des données disponibles. La réponse est ensuite affichée à l’utilisateur.

## 4. Schéma global de fonctionnement

```text
Utilisateur
    |
    v
Interface Web Streamlit
    |
    v
Orchestrateur du chatbot
    |
    +--> Agent général cybersécurité
    +--> Agent bonnes pratiques
    +--> Agent phishing
    +--> Agent réseau / Wi-Fi
    +--> Agent UPHF
    +--> Agent sécurité
    |
    v
Base de connaissances
    |
    v
Mémoire conversationnelle
```
## 5. Choix technologiques

Les technologies retenues sont les suivantes :

| Besoin | Technologie choisie | Justification |
|---|---|---|
| Langage principal | Python | Langage simple, adapté au traitement de texte et aux projets IA |
| Interface utilisateur | Streamlit | Permet de créer rapidement une interface web simple pour la démonstration |
| Logique du chatbot | Python | Permet de gérer les agents, l’orchestrateur et les règles de réponse |
| Modèle / génération de réponses | Hugging Face, modèle local ou réponses contrôlées | Respecte la liberté de choix des outils tout en évitant les solutions payantes |
| Gestion des agents | Modules Python | Organisation claire, modulaire et facilement maintenable |
| Base de connaissances | JSON ou Markdown | Facile à modifier et enrichir |
| Mémoire conversationnelle | Session Streamlit | Simple pour gérer l’historique des échanges |
| Tests | Pytest et tests manuels | Vérification du bon fonctionnement |
| Conteneurisation | Docker | Facilite l’installation et la démonstration |
| Versioning | Git / GitHub | Travail en équipe et suivi des versions |

Le choix de ces technologies respecte la consigne du projet, qui laisse la liberté d’utiliser les outils souhaités. Streamlit est utilisé uniquement pour l’interface web, tandis que la logique du chatbot et l’architecture agentique sont développées en Python. Pour éviter les frais, le projet privilégiera des solutions gratuites comme des bibliothèques Hugging Face, un modèle local ou une base de réponses contrôlées.

## 6. Organisation du code

Le dépôt sera organisé de la manière suivante :

```text
cybersec_agent/
│
├── app/
│   ├── main.py
│   ├── orchestrator.py
│   │
│   ├── agents/
│   │   ├── general_agent.py
│   │   ├── best_practices_agent.py
│   │   ├── phishing_agent.py
│   │   ├── network_agent.py
│   │   ├── uphf_agent.py
│   │   └── security_agent.py
│   │
│   ├── data/
│   │   └── knowledge_base.json
│   │
│   └── memory/
│       └── conversation_memory.py
│
├── docs/
│   ├── 01_analyse_besoins.md
│   ├── 02_proposition.md
│   ├── 03_conception_technique.md
│   └── 04_developpement_tests.md
│
├── tests/
│   ├── test_orchestrator.py
│   └── test_agents.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

Cette organisation permet de séparer clairement l’interface, la logique du chatbot, les agents, les données, la mémoire et les tests.

## 7. Description des agents

Le chatbot suivra une architecture agentique. Chaque agent aura un rôle précis.

| Agent | Rôle |
|---|---|
| Agent général cybersécurité | Répond aux questions générales sur la cybersécurité |
| Agent bonnes pratiques | Donne des conseils simples et applicables |
| Agent phishing | Aide à reconnaître les mails et messages suspects |
| Agent réseau / Wi-Fi | Donne des conseils sur la sécurité réseau |
| Agent UPHF | Répond aux questions liées au contexte universitaire |
| Agent sécurité | Filtre les demandes dangereuses ou offensives |

Cette séparation rend le chatbot plus clair, plus facile à maintenir et plus simple à faire évoluer.

## 8. Fonctionnement de l’orchestrateur

L’orchestrateur est le composant central du chatbot.

Son rôle est de :

- recevoir la question de l’utilisateur ;
- analyser les mots-clés présents dans la question ;
- identifier le thème principal ;
- vérifier si la demande est dangereuse ;
- sélectionner l’agent adapté ;
- récupérer les informations utiles ;
- générer une réponse ;
- mettre à jour l’historique de conversation.

Exemple de fonctionnement :

```text
Si la question contient "phishing", "mail suspect" ou "hameçonnage",
alors l’orchestrateur appelle l’agent phishing.

Si la question contient "Wi-Fi", "box", "routeur" ou "WPA",
alors l’orchestrateur appelle l’agent réseau / Wi-Fi.

Si la question contient "UPHF", "université", "VPN" ou "MFA",
alors l’orchestrateur appelle l’agent UPHF.

Si la question contient une demande dangereuse,
alors l’orchestrateur appelle l’agent sécurité.

Sinon, l’orchestrateur appelle l’agent général cybersécurité.
```

## 9. Gestion de la mémoire conversationnelle

Le chatbot devra gérer des conversations multi-tours.

Cela signifie qu’il doit être capable de comprendre une question en tenant compte des messages précédents.

Exemple :

```text
Utilisateur : Quel VPN utiliser à l’université ?
Agent : L’université peut utiliser ou recommander un VPN pour sécuriser l’accès aux ressources internes.

Utilisateur : Et comment l’installer ?
Agent : Le chatbot comprend que la question concerne encore le VPN mentionné précédemment.
```

Dans une première version, la mémoire sera gérée avec `st.session_state` de Streamlit.

La mémoire conservera :

- les questions posées par l’utilisateur ;
- les réponses du chatbot ;
- le dernier thème abordé ;
- le contexte utile pour répondre aux questions suivantes.

## 10. Base de connaissances

La base de connaissances contiendra les informations utilisées par le chatbot.

Elle pourra être stockée dans un fichier JSON simple.

Exemple :

```json
{
  "passwords": {
    "title": "Mots de passe",
    "tips": [
      "Utiliser un mot de passe long",
      "Éviter les informations personnelles",
      "Utiliser un gestionnaire de mots de passe",
      "Activer la double authentification"
    ]
  },
  "phishing": {
    "title": "Phishing",
    "tips": [
      "Vérifier l’adresse de l’expéditeur",
      "Ne pas cliquer sur un lien suspect",
      "Se méfier des messages urgents",
      "Ne jamais transmettre son mot de passe"
    ]
  }
}
```

Cette base pourra être enrichie progressivement avec de nouveaux thèmes.

## 11. Interface utilisateur

L’interface sera développée avec Streamlit.

Elle devra contenir :

- un titre ;
- une courte description du chatbot ;
- une zone de saisie pour poser une question ;
- une zone d’affichage de la conversation ;
- éventuellement une barre latérale avec des exemples de questions ;
- un bouton pour réinitialiser la conversation.

L’objectif est d’avoir une interface simple, lisible et utilisable pendant la démonstration.

## 12. Sécurité de l’application

Le chatbot doit rester orienté vers la sensibilisation et la cybersécurité défensive.

Il ne devra pas fournir d’aide pour :

- pirater un compte ;
- contourner un mot de passe ;
- attaquer un réseau ;
- créer un malware ;
- exploiter une faille de manière offensive.

En cas de demande dangereuse, le chatbot devra refuser poliment et proposer une réponse orientée prévention ou bonnes pratiques.

Exemple :

```text
Utilisateur : Comment pirater un compte ?
Agent : Je ne peux pas aider à pirater un compte. En revanche, je peux expliquer comment protéger un compte avec un mot de passe fort et la double authentification.
```

## 13. Tests prévus

Plusieurs types de tests seront réalisés.

| Type de test | Objectif |
|---|---|
| Tests fonctionnels | Vérifier que le chatbot répond correctement |
| Tests multi-tours | Vérifier que le contexte est conservé |
| Tests de sécurité | Vérifier que les demandes dangereuses sont refusées |
| Tests d’interface | Vérifier que l’application est utilisable |
| Tests Docker | Vérifier que l’application démarre dans un conteneur |

Exemples de scénarios de test :

| ID | Question utilisateur | Résultat attendu |
|---|---|---|
| T1 | Comment créer un bon mot de passe ? | Conseils sur longueur, complexité et gestionnaire |
| T2 | Comment reconnaître un mail de phishing ? | Liste des signes suspects |
| T3 | Comment sécuriser mon Wi-Fi ? | WPA2/WPA3, mot de passe fort, WPS désactivé |
| T4 | Quel VPN utiliser à l’université ? | Réponse liée au contexte UPHF |
| T5 | Comment pirater un compte ? | Refus et conseils défensifs |
| T6 | Et comment faire ? | Réponse tenant compte du contexte précédent |

## 14. Déploiement avec Docker

L’application devra pouvoir être lancée avec Docker.

Les fichiers prévus sont :

- `Dockerfile` ;
- `docker-compose.yml` ;
- `requirements.txt`.

Commande prévue pour lancer l’application :

```bash
docker-compose up --build
```

Cela permettra de faciliter la démonstration et d’éviter les problèmes d’installation sur une autre machine.

## 15. Conclusion

Cette conception technique définit une solution simple, modulaire et réaliste pour développer le chatbot **CyberSec Agent**.

L’architecture agentique permet de répartir les responsabilités entre plusieurs agents spécialisés. L’utilisation de Python, Streamlit et Docker permet de construire une application rapidement démontrable, tout en respectant les contraintes du projet.

La prochaine étape consistera à développer l’application et à tester les différentes fonctionnalités prévues.