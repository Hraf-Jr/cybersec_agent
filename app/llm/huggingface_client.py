from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


_model = None
_tokenizer = None


def get_model():
    """
    Charge le modèle Hugging Face une seule fois.
    """

    global _model, _tokenizer

    if _model is None or _tokenizer is None:
        model_name = "google/mt5-small"  # Modèle de paraphrase en français

        _tokenizer = AutoTokenizer.from_pretrained(model_name)
        _model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    return _tokenizer, _model


def improve_response_with_huggingface(user_question, base_response):
    """
    Reformule une réponse de base avec Hugging Face.
    """

    tokenizer, model = get_model()

    prompt = (
        "reformuler en français : "
        f"{base_response}"
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=180,
        min_new_tokens=20,
        do_sample=False,
        num_beams=4
    )

    improved_response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    ).strip()

    print(">>> RÉPONSE HF :", improved_response)

    # Nettoyage si le modèle recopie des morceaux du prompt
    bad_markers = [
        "French paraphrase:",
        "Original answer:",
        "User question:",
        "Question utilisateur:",
        "Réponse de base:"
    ]

    for marker in bad_markers:
        improved_response = improved_response.replace(marker, "").strip()

    if improved_response:
        return "Réponse reformulée avec Hugging Face :\n\n" + improved_response

    return (
        "Réponse analysée par Hugging Face, mais reformulation vide. "
        "Réponse contrôlée utilisée :\n\n" + base_response
    )