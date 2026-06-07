# CyberSec Agent

CyberSec Agent est un chatbot de sensibilisation à la cybersécurité.

Il permet de poser des questions sur les mots de passe, le phishing, le Wi-Fi, les VPN ou les bonnes pratiques numériques. Le projet repose sur une architecture agentique, une base de connaissances JSON et une couche IA locale avec Ollama/Mistral pour reformuler les réponses.

## Fonctionnalités

- Interface web avec Streamlit
- Agents spécialisés par thème
- Base de connaissances JSON
- Mémoire conversationnelle simple
- Filtrage des demandes dangereuses
- Reformulation avec Ollama/Mistral
- Tests unitaires avec Pytest
- Lancement possible avec Docker

## Architecture

```text
cybersec_agent/
├── app/
│   ├── main.py
│   ├── orchestrator.py
│   ├── data_loader.py
│   ├── agents/
│   ├── data/
│   ├── memory/
│   └── llm/
├── docs/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Prérequis

- Python 3.12
- Git
- Ollama
- Docker Desktop, si lancement avec Docker

## Installation

```bash
git clone https://github.com/Hraf-Jr/cybersec_agent.git
cd cybersec_agent
pip install -r requirements.txt
```

Le fichier `requirements.txt` contient :

```text
streamlit
pytest
requests
```

## Installation de Ollama/Mistral

Installer Ollama, puis télécharger le modèle Mistral :

```bash
ollama pull mistral
```

Vérifier l’installation :

```bash
ollama list
```

## Lancement local

```bash
python -m streamlit run app/main.py
```

L’application est disponible sur :

```text
http://localhost:8501
```

## Lancement avec Docker

Ollama doit être lancé sur la machine hôte.

```bash
docker compose up --build
```

Puis ouvrir :

```text
http://localhost:8501
```

Arrêter Docker :

```bash
docker compose down
```

## Tests

```bash
python -m pytest
```

Résultat attendu :

```text
6 passed
```

Les tests vérifient la détection des thèmes, les questions de suivi et le filtrage des demandes dangereuses.

## Exemples de questions

```text
Comment reconnaître un mail de phishing ?
Comment sécuriser mon Wi-Fi ?
Pourquoi utiliser un VPN ?
Comment créer un bon mot de passe ?
Comment pirater un compte ?
```

La dernière question doit être refusée par l’agent de sécurité.

## Fonctionnement général

1. L’utilisateur pose une question.
2. L’orchestrateur identifie le thème.
3. L’agent de sécurité filtre les demandes dangereuses.
4. Un agent spécialisé produit une réponse contrôlée.
5. Ollama/Mistral reformule la réponse.
6. La réponse finale est affichée.

## Remarque sur l’IA

Ollama/Mistral est utilisé comme couche IA locale pour reformuler les réponses.  
La réponse de base reste contrôlée par les agents et la base JSON afin d’éviter les réponses dangereuses ou incohérentes.

## Auteurs

Projet réalisé dans le cadre du projet informatique ICy S8.

Équipe :

- Achraf
- Anis
- Saad
- Adnane
- Othmane