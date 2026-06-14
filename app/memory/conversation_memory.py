def detect_topic(question):
    question = question.lower()

    if any(word in question for word in [
        "phishing", "hameçonnage", "hameconnage", "mail suspect",
        "email suspect", "arnaque", "lien suspect", "faux mail"
    ]):
        return "phishing"

    if any(word in question for word in [
        "wifi", "wi-fi", "réseau wifi", "box", "routeur",
        "wpa", "wpa2", "wpa3", "wps", "ssid"
    ]):
        return "wifi"

    if any(word in question for word in [
        "vpn", "réseau privé virtuel", "tunnel sécurisé",
        "eduVPN", "eduvpn", "accès distant"
    ]):
        return "vpn"

    if any(word in question for word in [
        "mot de passe", "password", "mdp", "2fa",
        "double authentification", "authentification", "compte"
    ]):
        return "passwords"

    if any(word in question for word in [
        "uphf", "université", "ent", "compte universitaire",
        "direction du numérique", "dnum"
    ]):
        return "uphf"

    if any(word in question for word in [
        "virus", "malware", "cheval de troie", "trojan",
        "spyware", "keylogger", "logiciel malveillant"
    ]):
        return "malware"

    if any(word in question for word in [
        "ransomware", "rançongiciel", "rancongiciel", "rançon", "rancon"
    ]):
        return "ransomware"

    if any(word in question for word in [
        "mise à jour", "mise a jour", "update", "patch", "correctif"
    ]):
        return "updates"

    if any(word in question for word in [
        "sauvegarde", "backup", "restaurer", "perte de données",
        "perte de donnees"
    ]):
        return "backups"

    if any(word in question for word in [
        "wifi public", "réseau public", "reseau public",
        "hotspot", "aéroport", "gare"
    ]):
        return "public_wifi"

    if any(word in question for word in [
        "messagerie chiffrée", "messagerie chiffree",
        "signal", "whatsapp", "chiffrement", "bout en bout"
    ]):
        return "encrypted_messaging"

    if any(word in question for word in [
        "manipulation", "ingénierie sociale", "ingenierie sociale",
        "usurpation", "faux technicien"
    ]):
        return "social_engineering"

    if any(word in question for word in [
        "téléphone", "telephone", "smartphone", "android", "iphone"
    ]):
        return "smartphone"

    return None


def is_follow_up_question(question):
    question = question.lower()

    follow_up_markers = [
        "et si",
        "comment faire",
        "et après",
        "et apres",
        "comment l'installer",
        "comment l’installer",
        "comment l installer",
        "comment installer",
        "comment s'en protéger",
        "comment sen proteger",
        "comment s en proteger",
        "s'en protéger",
        "sen proteger",
        "s en proteger",
        "comment se protéger",
        "comment se proteger",
        "comment le faire",
        "comment ça marche",
        "comment ca marche",
        "je fais quoi",
        "que faire",
        "pourquoi",
        "explique",
        "plus précisément",
        "plus precisement",
        "donne plus"
    ]

    return any(marker in question for marker in follow_up_markers)

def get_last_context_question(conversation_history):
    """
    Récupère la dernière vraie question de contexte.
    On ignore les questions trop courtes comme :
    'explique', 'pourquoi', 'comment faire', etc.
    """

    ignored_followups = [
        "explique",
        "pourquoi",
        "comment",
        "comment faire",
        "comment s'en protéger",
        "comment s’en protéger",
        "comment se protéger",
        "comment l'installer",
        "comment l installer",
        "et après",
        "et apres",
        "que faire"
    ]

    for message in reversed(conversation_history):
        if message["role"] == "user":
            content = message["content"].lower().strip()

            if content in ignored_followups:
                continue

            if is_follow_up_question(content):
                continue

            return message["content"]

    return None
    
def get_last_topic(conversation_history):
    for message in reversed(conversation_history):
        if message["role"] == "user":
            topic = detect_topic(message["content"])
            if topic:
                return topic

    return None

def get_last_user_question(conversation_history):
    for message in reversed(conversation_history):
        if message["role"] == "user":
            return message["content"]

    return None