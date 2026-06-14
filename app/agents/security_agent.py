def is_dangerous_question(question):
    """
    Détecte les demandes dangereuses ou offensives.
    """

    dangerous_keywords = [
        "pirater",
        "hack",
        "hacker",
        "voler un compte",
        "mot de passe de quelqu'un",
        "trouver le mot de passe",
        "cracker",
        "contourner",
        "attaquer un réseau",
        "keylogger",
        "exploiter une faille"
    ]

    return any(keyword in question for keyword in dangerous_keywords)


def security_response():
    """
    Réponse lorsque la demande est dangereuse.
    """

    return (
        "Je ne peux pas aider à réaliser une action offensive ou illégale. "
        "En revanche, je peux vous aider à comprendre les risques et à protéger vos comptes, "
        "vos appareils ou votre réseau. Par exemple, vous pouvez utiliser un mot de passe fort, "
        "activer la double authentification et maintenir vos logiciels à jour."
    )