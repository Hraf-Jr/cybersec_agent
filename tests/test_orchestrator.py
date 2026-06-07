from app.memory.conversation_memory import detect_topic, is_follow_up_question


def test_detect_phishing_topic():
    question = "comment reconnaître un mail de phishing"
    assert detect_topic(question) == "phishing"


def test_detect_wifi_topic():
    question = "comment sécuriser mon wifi"
    assert detect_topic(question) == "wifi"


def test_detect_vpn_topic():
    question = "pourquoi utiliser un vpn"
    assert detect_topic(question) == "vpn"


def test_follow_up_question():
    question = "comment l’installer ?"
    assert is_follow_up_question(question) is True