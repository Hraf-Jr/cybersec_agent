from agents.general_agent import general_response
from agents.best_practices_agent import best_practices_response
from agents.phishing_agent import phishing_response
from agents.network_agent import network_response
from agents.uphf_agent import uphf_response
from agents.security_agent import security_response, is_dangerous_question
from agents.vpn_agent import vpn_response

from memory.conversation_memory import detect_topic, get_last_topic, is_follow_up_question


def response_by_topic(topic):
    """
    Retourne la réponse correspondant à un thème détecté.
    """

    if topic == "phishing":
        return phishing_response()

    if topic == "wifi":
        return network_response()

    if topic == "vpn":
        return vpn_response()

    if topic == "best_practices":
        return best_practices_response()

    if topic == "uphf":
        return uphf_response()

    return general_response()


def follow_up_response_by_topic(topic, question):
    """
    Retourne une réponse adaptée lorsqu'il s'agit d'une question de suivi.
    """

    question = question.lower()

    if topic == "phishing":
        if "cliqué" in question or "clique" in question:
            return (
                "Si vous avez déjà cliqué sur un lien suspect, il faut éviter de saisir vos identifiants. "
                "Si vous les avez déjà saisis, changez immédiatement votre mot de passe, activez la double authentification "
                "et signalez le message au service informatique ou à l’organisme concerné."
            )
        return phishing_response()

    if topic == "vpn":
        if "installer" in question or "installation" in question:
            return (
                "Pour installer un VPN, il faut d’abord utiliser le service recommandé par votre établissement ou votre organisation. "
                "En général, les étapes sont les suivantes : télécharger le client VPN officiel, l’installer, se connecter avec ses identifiants, "
                "puis choisir le profil ou le serveur adapté. Dans un contexte universitaire, il faut suivre la documentation officielle de l’établissement."
            )
        return vpn_response()

    if topic == "wifi":
        return network_response()

    if topic == "best_practices":
        return best_practices_response()

    if topic == "uphf":
        return uphf_response()

    return general_response()


def generate_response(user_question, conversation_history=None):
    """
    Analyse la question de l'utilisateur et sélectionne l'agent le plus adapté.
    """

    question = user_question.lower()

    # 1. Vérification des demandes dangereuses
    if is_dangerous_question(question):
        return security_response()

    # 2. Gestion du multi-tours en priorité si la question ressemble à une question de suivi
    if is_follow_up_question(question):
        last_topic = get_last_topic(conversation_history)

        if last_topic:
            return follow_up_response_by_topic(last_topic, question)

    # 3. Détection directe du thème
    current_topic = detect_topic(question)

    if current_topic:
        return response_by_topic(current_topic)

    # 4. Réponse générale par défaut
    return general_response()