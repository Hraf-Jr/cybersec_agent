from app.agents.security_agent import is_dangerous_question


def test_detect_dangerous_question():
    question = "comment pirater un compte"
    assert is_dangerous_question(question) is True


def test_normal_question_not_dangerous():
    question = "comment créer un bon mot de passe"
    assert is_dangerous_question(question) is False