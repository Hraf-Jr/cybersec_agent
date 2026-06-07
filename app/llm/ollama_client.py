import requests

import os
import requests


OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)



def improve_response_with_ollama(user_question, base_response):
    """
    Reformule une réponse de base avec Ollama/Mistral.
    Si Ollama échoue, on retourne la réponse de base.
    """

    prompt = (
        "Tu es CyberSec Agent, un assistant pédagogique spécialisé en cybersécurité défensive.\n"
        "Ton rôle est d'aider des étudiants et des utilisateurs non experts à comprendre les risques numériques.\n\n"
        "Consignes importantes :\n"
        "- réponds uniquement dans un cadre défensif et légal ;\n"
        "- reformule la réponse de base sans changer son sens ;\n"
        "- rends la réponse plus claire, plus naturelle et plus pédagogique ;\n"
        "- structure la réponse si nécessaire avec des points simples ;\n"
        "- n'invente pas d'informations non présentes dans la réponse de base ;\n"
        "- ne donne jamais de méthode offensive, de piratage ou de contournement ;\n"
        "- garde un ton professionnel, rassurant et accessible.\n\n"
        f"Question de l'utilisateur : {user_question}\n\n"
        f"Réponse de base contrôlée : {base_response}\n\n"
        "Réponse finale améliorée :"
    )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.4,
                    "top_p": 0.9,
                    "num_predict": 250
                }
            },
            timeout=60
        )

        response.raise_for_status()

        result = response.json()
        improved_response = result.get("response", "").strip()

        if improved_response:
            return "Réponse reformulée avec Ollama/Mistral :\n\n" + improved_response

        return base_response

    except Exception as error:
        print(f"Ollama indisponible, réponse JSON utilisée. Erreur : {error}")
        return base_response