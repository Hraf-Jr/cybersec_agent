from app.llm.huggingface_client import improve_response_with_huggingface

question = "Comment reconnaître un mail de phishing ?"
base_response = (
    "Pour reconnaître une tentative de phishing, il faut vérifier l’adresse de l’expéditeur, "
    "les fautes d’orthographe, les liens suspects et les pièces jointes inattendues."
)

print(improve_response_with_huggingface(question, base_response))