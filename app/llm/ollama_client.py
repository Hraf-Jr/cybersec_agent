import requests


def improve_response_with_ollama(user_question, base_response):
    """
    Reformule une réponse de base avec Ollama/Mistral.
    Si Ollama échoue, on retourne la réponse de base.
    """

    prompt = (
        "Tu es un assistant pédagogique spécialisé en cybersécurité.\n"
        "Reformule la réponse suivante en français clair, naturel et concis.\n"
        "Garde exactement le même sens.\n"
        "N'ajoute aucun conseil offensif ou dangereux.\n\n"
        f"Question utilisateur : {user_question}\n"
        f"Réponse de base : {base_response}\n\n"
        "Réponse reformulée :"
    )

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
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