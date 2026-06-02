from data_loader import get_response


def general_response():
    """
    Réponse générale lorsque le thème précis n'est pas détecté.
    """

    return get_response("general")