from agents.general_agent import general_response
from agents.vpn_agent import vpn_response
from agents.best_practices_agent import best_practices_response
from agents.phishing_agent import phishing_response
from agents.network_agent import network_response
from agents.uphf_agent import uphf_response
from agents.security_agent import security_response, is_dangerous_question


def generate_response(user_question, conversation_history=None):
    """
    Analyse la question de l'utilisateur et sélectionne l'agent le plus adapté.
    """

    question = user_question.lower()

    # 1. Vérification des demandes dangereuses
    if is_dangerous_question(question):
        return security_response()

    # 2. Agent phishing
    phishing_keywords = [
        "phishing", "hameçonnage", "mail suspect", "email suspect",
        "lien suspect", "arnaque", "pièce jointe", "expéditeur"
    ]

    if any(keyword in question for keyword in phishing_keywords):
        return phishing_response()

    # 3. Agent réseau / Wi-Fi
    network_keywords = [
        "wifi", "wi-fi", "réseau", "box", "routeur",
        "wpa", "wps", "connexion", "internet"
    ]

    if any(keyword in question for keyword in network_keywords):
        return network_response()
    
        # Agent VPN
    vpn_keywords = [
        "vpn", "réseau privé virtuel", "tunnel sécurisé",
        "connexion sécurisée", "ressources internes"
    ]

    if any(keyword in question for keyword in vpn_keywords):
        return vpn_response()

    # 4. Agent UPHF
    uphf_keywords = [
        "uphf", "université", "vpn universitaire", "mfa",
        "double authentification", "ent", "compte universitaire"
    ]

    if any(keyword in question for keyword in uphf_keywords):
        return uphf_response()

    # 5. Agent bonnes pratiques
    best_practices_keywords = [
        "mot de passe", "password", "2fa", "authentification",
        "sécuriser", "protéger", "sauvegarde", "mise à jour",
        "bonnes pratiques", "compte"
    ]

    if any(keyword in question for keyword in best_practices_keywords):
        return best_practices_response()

    # 6. Réponse générale par défaut
    return general_response()