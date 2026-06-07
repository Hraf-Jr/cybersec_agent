import os
import requests


OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)


def is_incomplete_response(text):
    """
    Vérifie si la réponse semble coupée au milieu d'une phrase.
    """

    if not text:
        return True

    text = text.strip()

    return not text.endswith((".", "!", "?", "»"))


def call_ollama(prompt, num_predict=400):
    """
    Appelle Ollama/Mistral avec un prompt donné.
    """

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.3,
                "top_p": 0.9,
                "num_predict": num_predict
            }
        },
        timeout=120
    )

    response.raise_for_status()

    result = response.json()
    return result.get("response", "").strip()


def complete_incomplete_response(partial_response):
    """
    Demande à Ollama de compléter une réponse coupée.
    """

    prompt = (
        "La réponse suivante est coupée au milieu d'une phrase.\n"
        "Complète uniquement la fin de la réponse en français.\n"
        "Ne recommence pas depuis le début.\n"
        "N'ajoute pas de nouveau sujet.\n\n"
        f"Réponse coupée : {partial_response}\n\n"
        "Suite :"
    )

    continuation = call_ollama(prompt, num_predict=120)

    if continuation:
        return partial_response.strip() + " " + continuation.strip()

    return partial_response


def improve_response_with_ollama(user_question, base_response):
    """
    Reformule une réponse de base avec Ollama/Mistral.
    Si la réponse est coupée, elle est complétée automatiquement.
    """

    prompt = (
        "Tu es CyberSec Agent, un assistant pédagogique spécialisé en cybersécurité défensive.\n"
        "Ton rôle est d'aider des étudiants et des utilisateurs non experts à comprendre les risques numériques.\n\n"
        "Consignes importantes :\n"
        "- réponds uniquement dans un cadre défensif et légal ;\n"
        "- reformule la réponse de base sans changer son sens ;\n"
        "- rends la réponse plus claire, plus naturelle et plus pédagogique ;\n"
        "- structure la réponse avec des points simples si nécessaire ;\n"
        "- n'invente pas d'informations non présentes dans la réponse de base ;\n"
        "- ne donne jamais de méthode offensive, de piratage ou de contournement ;\n"
        "- garde un ton professionnel, rassurant et accessible ;\n"
        "- termine toujours ta réponse par une phrase complète.\n\n"
        f"Question de l'utilisateur : {user_question}\n\n"
        f"Réponse de base contrôlée : {base_response}\n\n"
        "Réponse finale améliorée :"
    )

    try:
        improved_response = call_ollama(prompt, num_predict=450)

        if is_incomplete_response(improved_response):
            improved_response = complete_incomplete_response(improved_response)

        if improved_response:
            return "Réponse reformulée avec Ollama/Mistral :\n\n" + improved_response

        return base_response

    except Exception as error:
        print(f"Ollama indisponible, réponse JSON utilisée. Erreur : {error}")
        return base_response