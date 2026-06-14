import json
import os
import requests


OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)


ALLOWED_TOPICS = [
    "phishing",
    "wifi",
    "vpn",
    "passwords",
    "best_practices",
    "uphf",
    "malware",
    "ransomware",
    "updates",
    "backups",
    "public_wifi",
    "encrypted_messaging",
    "social_engineering",
    "smartphone",
    "general",
    "unknown"
]


def classify_intent_with_ollama(question, last_topic=None):
    """
    Utilise Ollama/Mistral pour classifier l'intention de l'utilisateur.
    Cette fonction aide à comprendre les fautes d'orthographe,
    les formulations différentes et les questions de suivi.
    """

    prompt = (
        "Tu es un classificateur d'intention pour un chatbot de cybersécurité défensive.\n"
        "Tu dois analyser la question utilisateur et retourner uniquement un JSON valide.\n\n"
        "Thèmes possibles :\n"
        "- phishing : mails suspects, hameçonnage, liens suspects, arnaques\n"
        "- wifi : réseau Wi-Fi, routeur, box, WPA, WPS\n"
        "- vpn : VPN, tunnel sécurisé, accès distant, installation VPN\n"
        "- best_practices : mots de passe, 2FA, sauvegardes, mises à jour, bonnes pratiques\n"
        "- uphf : compte universitaire, ENT, contexte UPHF, université\n"
        "- unknown : si la question parle d’un concept cybersécurité qui n’est pas dans les thèmes connus, comme XSS, injection SQL, honeypot, man-in-the-middle, pare-feu, IDS, SIEM, chiffrement, certificat, etc.\n"
        "- general : question générale ou non claire\n\n"
        "Tu dois aussi dire si la question est une question de suivi.\n"
        "Une question de suivi est une question courte qui dépend du sujet précédent, par exemple :\n"
        "\"comment l'installer\", \"et après\", \"comment faire\", \"ça marche comment\", \"je fais quoi\".\n\n"
        f"Sujet précédent : {last_topic}\n"
        f"Question utilisateur : {question}\n\n"
        "Réponds uniquement avec ce format JSON, sans explication :\n"
        "{\n"
        "  \"topic\": \"vpn\",\n"
        "  \"is_follow_up\": true\n"
        "}"
    )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0,
                    "num_predict": 80
                }
            },
            timeout=30
        )

        response.raise_for_status()

        result = response.json()
        text = result.get("response", "").strip()

        start = text.find("{")
        end = text.rfind("}") + 1

        if start == -1 or end == 0:
            return None

        data = json.loads(text[start:end])

        topic = data.get("topic", "general")
        is_follow_up = data.get("is_follow_up", False)

        if topic not in ALLOWED_TOPICS:
            topic = "general"

        return {
            "topic": topic,
            "is_follow_up": bool(is_follow_up)
        }

    except Exception as error:
        print(f"Classification Ollama indisponible. Erreur : {error}")
        return None