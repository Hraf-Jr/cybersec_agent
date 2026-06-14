from agents.general_agent import general_response
from agents.best_practices_agent import best_practices_response
from agents.phishing_agent import phishing_response
from agents.network_agent import network_response
from agents.uphf_agent import uphf_response
from agents.security_agent import security_response, is_dangerous_question
from agents.vpn_agent import vpn_response
from data_loader import get_response

from llm.ollama_client import improve_response_with_ollama
from llm.intent_classifier import classify_intent_with_ollama
from llm.fallback_answer import generate_defensive_answer_with_ollama

from memory.conversation_memory import (
    detect_topic,
    get_last_topic,
    is_follow_up_question,
    get_last_user_question,
    get_last_context_question
)

def is_greeting(question):
    question = question.lower().strip()

    greetings = [
        "bonjour",
        "salut",
        "hello",
        "hey",
        "coucou",
        "bonsoir",
        "bjr",
        "slt"
    ]

    return question in greetings


def greeting_response():
    return (
        "Bonjour ! Je suis CyberSec Agent. "
        "Je peux vous aider sur les mots de passe, le phishing, le Wi-Fi, les VPN, "
        "les malwares, les sauvegardes, les mises à jour ou les bonnes pratiques de cybersécurité."
    )
def is_out_of_base_security_concept(question):
    question = question.lower()

    keywords = [
        "spoofing",
        "usurpation",
        "man in the middle",
        "man-in-the-middle",
        "mitm",
        "honeypot",
        "xss",
        "injection sql",
        "sql injection",
        "dns poisoning",
        "dns spoofing",
        "csrf",
        "zero day",
        "zero-day",
        "brute force",
        "siem",
        "ids",
        "ips",
        "pare-feu",
        "firewall",
        "certificat ssl",
        "tls",
        "sandbox",
        "rootkit",
        "botnet"
    ]

    return any(keyword in question for keyword in keywords)

def response_by_topic(topic):

    if topic == "phishing":
        return phishing_response()

    if topic == "wifi":
        return network_response()

    if topic == "vpn":
        return vpn_response()

    if topic == "passwords":
        return get_response("passwords")

    if topic == "best_practices":
        return best_practices_response()

    if topic == "uphf":
        return uphf_response()

    if topic == "malware":
        return get_response("malware")

    if topic == "ransomware":
        return get_response("ransomware")

    if topic == "updates":
        return get_response("updates")

    if topic == "backups":
        return get_response("backups")

    if topic == "public_wifi":
        return get_response("public_wifi")

    if topic == "encrypted_messaging":
        return get_response("encrypted_messaging")

    if topic == "social_engineering":
        return get_response("social_engineering")

    if topic == "smartphone":
        return get_response("smartphone")

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

def final_response(user_question, base_response):
    """
    Améliore la réponse avec Ollama/Mistral.
    """

    return improve_response_with_ollama(user_question, base_response)


def generate_response(user_question, conversation_history):
    question = user_question.lower()

    # 1. Salutations simples
    if is_greeting(question):
        return greeting_response()

    # 2. Filtre de sécurité prioritaire
    if is_dangerous_question(question):
        return security_response()
    
    if is_out_of_base_security_concept(question):
        return generate_defensive_answer_with_ollama(user_question)

    last_topic = get_last_topic(conversation_history)
    previous_question = get_last_user_question(conversation_history)

    current_topic = detect_topic(question)
    follow_up = is_follow_up_question(question)

    if follow_up:
        context_question = get_last_context_question(conversation_history)

        if context_question:
            context_topic = detect_topic(context_question)

            if context_topic and context_topic != "general":
                base_response = follow_up_response_by_topic(context_topic, user_question)
                return final_response(user_question, base_response)

            return generate_defensive_answer_with_ollama(
                user_question,
                previous_question=context_question
            )

        return (
            "Pouvez-vous préciser le sujet dont vous parlez ? "
            "Par exemple : phishing, VPN, honeypot, DNS poisoning ou mot de passe."
        )

    if current_topic and current_topic != "general":
        base_response = response_by_topic(current_topic)
        return final_response(user_question, base_response)

    classification = classify_intent_with_ollama(user_question, last_topic)

    if classification:
        classified_topic = classification.get("topic")
        is_follow_up = classification.get("is_follow_up", False)

        if is_follow_up and previous_question:
            previous_topic = detect_topic(previous_question)

            if previous_topic and previous_topic != "general":
                base_response = follow_up_response_by_topic(previous_topic, user_question)
                return final_response(user_question, base_response)

            print("QUESTION ACTUELLE :", user_question)
            print("QUESTION PRECEDENTE :", previous_question)
            print("FOLLOW UP :", follow_up)
            
            return generate_defensive_answer_with_ollama(
                user_question,
                previous_question=previous_question
                
            )

        if classified_topic and classified_topic not in ["general", "unknown"]:
            base_response = response_by_topic(classified_topic)
            return final_response(user_question, base_response)

    return generate_defensive_answer_with_ollama(user_question)