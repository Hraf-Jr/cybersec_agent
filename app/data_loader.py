import json
from pathlib import Path


def load_knowledge_base():
    """
    Charge la base de connaissances depuis le fichier JSON.
    """

    base_path = Path(__file__).parent / "data" / "knowledge_base.json"

    with open(base_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_response(topic):
    """
    Retourne la réponse associée à un thème.
    """

    knowledge_base = load_knowledge_base()

    if topic in knowledge_base:
        return knowledge_base[topic]["response"]

    return knowledge_base["general"]["response"]