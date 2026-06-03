def detect_topic(question):
    """
    Détecte le thème principal d'une question utilisateur.
    """

    question = question.lower()

    if any(word in question for word in ["phishing", "hameçonnage", "mail suspect", "email suspect", "arnaque", "lien suspect"]):
        return "phishing"

    if any(word in question for word in ["wifi", "wi-fi", "réseau", "box", "routeur", "wpa", "wps"]):
        return "wifi"

    if any(word in question for word in ["vpn", "réseau privé virtuel", "tunnel sécurisé"]):
        return "vpn"

    if any(word in question for word in ["mot de passe", "password", "2fa", "authentification", "compte"]):
        return "best_practices"

    if any(word in question for word in ["uphf", "université", "mfa", "compte universitaire"]):
        return "uphf"

    if " ent " in f" {question} ":
        return "uphf"

    return None


def get_last_topic(conversation_history):
    """
    Récupère le dernier thème détecté dans l'historique de conversation.
    """

    if not conversation_history:
        return None

    for message in reversed(conversation_history):
        if message["role"] == "user":
            topic = detect_topic(message["content"])
            if topic:
                return topic

    return None


def is_follow_up_question(question):
    """
    Détecte si la question semble être une question de suivi.
    """

    question = question.lower().strip()

    follow_up_markers = [
        "et si",
        "comment faire",
        "et après",
        "comment l'installer",
        "comment l’installer",
        "comment le faire",
        "que faire",
        "pourquoi",
        "explique",
        "plus précisément",
        "donne plus",
        "j'ai déjà",
        "j’ai déjà"
    ]

    return any(marker in question for marker in follow_up_markers)