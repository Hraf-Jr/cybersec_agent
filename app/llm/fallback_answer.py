import os
import requests


OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)


def is_incomplete_response(text):
    if not text:
        return True

    text = text.strip()

    return not text.endswith((".", "!", "?", "»"))


def call_ollama(prompt, num_predict=350):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.2,
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
    prompt = (
        "La réponse suivante est coupée.\n"
        "Complète uniquement la fin de la dernière phrase ou du dernier point.\n"
        "Ne recommence pas la réponse depuis le début.\n"
        "N'ajoute pas d'introduction.\n"
        "N'ajoute pas de nouveau sujet.\n"
        "Termine proprement par une phrase complète.\n\n"
        f"Réponse coupée : {partial_response}\n\n"
        "Suite :"
    )

    continuation = call_ollama(prompt, num_predict=120)

    if continuation:
        return partial_response.strip() + " " + continuation.strip()

    return partial_response


def clean_answer(answer):
    forbidden_starts = [
        "Bienvenue !",
        "Bonjour !",
        "Je suis CyberSec Agent",
        "En tant que CyberSec Agent"
    ]

    for start in forbidden_starts:
        if answer.startswith(start):
            answer = answer.replace(start, "", 1).strip()

    return answer.strip()


def generate_defensive_answer_with_ollama(user_question, previous_question=None):
    context_part = ""

    if previous_question:
        context_part = (
            f"Question précédente : {previous_question}\n"
            "La question actuelle peut être une question de suivi. "
            "Si c'est le cas, réponds en gardant ce contexte.\n\n"
        )

    prompt = (
        "Tu es un assistant pédagogique spécialisé en cybersécurité défensive.\n"
        "L'utilisateur pose une question sur un concept qui n'est pas dans la base de connaissances.\n\n"
        "Règles obligatoires :\n"
        "- réponds directement au concept demandé ;\n"
        "- commence directement par une définition du concept ;\n"
        "- ne commence jamais par Bonjour, Bienvenue ou Je suis CyberSec Agent ;\n"
        "- ne fais jamais d'introduction générale sur la cybersécurité ;\n"
        "- ne liste jamais les sujets que tu peux traiter ;\n"
        "- ne dis jamais 'je suis là pour vous aider' ;\n"
        "- ne parle pas de mots de passe, phishing, VPN ou Wi-Fi sauf si c'est lié à la question ;\n"
        "- donne une réponse courte, claire et pédagogique ;\n"
        "- explique en 2 ou 3 parties maximum : définition, risque, protection ;\n"
        "- reste uniquement dans un cadre défensif et légal ;\n"
        "- ne donne aucune méthode offensive exploitable ;\n"
        "- termine toujours par une phrase complète.\n\n"
        f"{context_part}"
        f"Question utilisateur : {user_question}\n\n"
        "Réponse directe :"
    )

    try:
        answer = call_ollama(prompt, num_predict=300)
        answer = clean_answer(answer)

        if is_incomplete_response(answer):
            answer = complete_incomplete_response(answer)
            answer = clean_answer(answer)

        if answer:
            return "Réponse générée avec Ollama/Mistral :\n\n" + answer

        return (
            "Je n’ai pas trouvé ce sujet dans la base de connaissances, "
            "mais je peux vous aider sur les principes défensifs liés à la cybersécurité."
        )

    except Exception as error:
        print(f"Fallback Ollama indisponible. Erreur : {error}")
        return (
            "La couche IA locale n’est pas disponible pour générer une réponse complémentaire."
        )