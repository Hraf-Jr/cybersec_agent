import json
from pathlib import Path
import streamlit as st


def load_quiz_questions():
    """
    Charge les questions du quiz depuis un fichier JSON.
    """

    quiz_path = Path(__file__).parent / "data" / "quiz_questions.json"

    with open(quiz_path, "r", encoding="utf-8") as file:
        return json.load(file)


def display_quiz():
    """
    Affiche un mini quiz cybersécurité dans l'interface Streamlit.
    """

    questions = load_quiz_questions()
    total_questions = len(questions)

    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0

    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0

    if "quiz_answered" not in st.session_state:
        st.session_state.quiz_answered = False

    if "quiz_last_correct" not in st.session_state:
        st.session_state.quiz_last_correct = None

    if "quiz_completed_questions" not in st.session_state:
        st.session_state.quiz_completed_questions = set()

    current_index = st.session_state.quiz_index
    current_question = questions[current_index]

    st.markdown("### 🎯 Quiz cybersécurité")
    st.markdown(f"**Question {current_index + 1} / {total_questions}**")
    st.markdown(current_question["question"])

    # Si la question n'est pas encore répondue
    if not st.session_state.quiz_answered:
        with st.form(key=f"quiz_form_{current_index}"):
            selected_answer = st.radio(
                "Choisissez une réponse :",
                current_question["options"],
                key=f"quiz_radio_{current_index}"
            )

            submitted = st.form_submit_button("Valider la réponse")

            if submitted:
                st.session_state.quiz_answered = True

                is_correct = selected_answer == current_question["answer"]
                st.session_state.quiz_last_correct = is_correct

                if is_correct and current_index not in st.session_state.quiz_completed_questions:
                    st.session_state.quiz_score += 1
                    st.session_state.quiz_completed_questions.add(current_index)

                st.rerun()

    # Si la question est déjà répondue
    else:
        if st.session_state.quiz_last_correct:
            st.success("Bonne réponse ✅")
        else:
            st.error("Mauvaise réponse ❌")

        st.info(current_question["explanation"])

        if st.button("Question suivante", key=f"next_{current_index}"):
            st.session_state.quiz_index = (current_index + 1) % total_questions
            st.session_state.quiz_answered = False
            st.session_state.quiz_last_correct = None
            st.rerun()

    st.markdown(f"Score : **{st.session_state.quiz_score}** / **{total_questions}**")

    if st.button("Réinitialiser le quiz"):
        st.session_state.quiz_index = 0
        st.session_state.quiz_score = 0
        st.session_state.quiz_answered = False
        st.session_state.quiz_last_correct = None
        st.session_state.quiz_completed_questions = set()
        st.rerun()