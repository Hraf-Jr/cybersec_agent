import streamlit as st
import uuid
from database import save_conversation
from memory.conversation_memory import detect_topic
from orchestrator import generate_response
from quiz import display_quiz

st.set_page_config(
    page_title="CyberSec Agent",
    page_icon="🜁",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================
# STYLE GLOBAL
# =========================

st.markdown(
    """
    <style>
    /* Fond global */
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(0, 255, 170, 0.10), transparent 30%),
            radial-gradient(circle at bottom right, rgba(120, 0, 255, 0.10), transparent 30%),
            linear-gradient(135deg, #050807 0%, #0b0f0e 45%, #050505 100%);
        color: #d8f3dc;
    }

    /* Masquer menu Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    

    /* Bloc principal */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1100px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #050807 0%, #08110f 100%);
        border-right: 1px solid rgba(0, 255, 170, 0.25);
    }

    section[data-testid="stSidebar"] * {
        color: #d8f3dc;
    }

    /* Titre principal */
    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        letter-spacing: 3px;
        color: #9fffd0;
        text-shadow: 0 0 10px rgba(0, 255, 170, 0.45);
        margin-bottom: 0px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #8fa99b;
        letter-spacing: 1px;
        margin-bottom: 30px;
    }

    .terminal-box {
        background: rgba(2, 8, 7, 0.78);
        border: 1px solid rgba(0, 255, 170, 0.22);
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 0 25px rgba(0, 255, 170, 0.08);
        margin-bottom: 20px;
    }

    .terminal-line {
        font-family: Consolas, monospace;
        font-size: 15px;
        color: #9fffd0;
    }

    .muted {
        color: #8fa99b;
        font-size: 14px;
    }

    .status-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-bottom: 25px;
    }

    .status-card {
        background: rgba(8, 18, 16, 0.85);
        border: 1px solid rgba(0, 255, 170, 0.18);
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        box-shadow: inset 0 0 18px rgba(0, 255, 170, 0.03);
    }

    .status-title {
        color: #9fffd0;
        font-size: 13px;
        font-weight: bold;
        letter-spacing: 1px;
    }

    .status-value {
        color: #b7c9c0;
        font-size: 12px;
        margin-top: 4px;
    }

    /* Messages du chat */
    div[data-testid="stChatMessage"] {
        background: rgba(5, 12, 11, 0.75);
        border: 1px solid rgba(0, 255, 170, 0.12);
        border-radius: 14px;
        padding: 8px;
        margin-bottom: 12px;
    }

    /* Input */
    textarea {
        background-color: #050807 !important;
        color: #d8f3dc !important;
        border: 1px solid rgba(0, 255, 170, 0.35) !important;
        border-radius: 10px !important;
    }

    textarea:focus {
        border-color: #9fffd0 !important;
        box-shadow: 0 0 10px rgba(0, 255, 170, 0.25) !important;
    }

    /* Boutons */
    .stButton > button {
        background: rgba(0, 255, 170, 0.08);
        color: #9fffd0;
        border: 1px solid rgba(0, 255, 170, 0.35);
        border-radius: 10px;
        transition: 0.2s ease-in-out;
    }

    .stButton > button:hover {
        background: rgba(0, 255, 170, 0.18);
        color: #ffffff;
        border-color: #9fffd0;
        box-shadow: 0 0 12px rgba(0, 255, 170, 0.25);
    }

    .sidebar-title {
        font-size: 25px;
        font-weight: 800;
        color: #9fffd0;
        text-shadow: 0 0 8px rgba(0, 255, 170, 0.4);
        margin-bottom: 12px;
    }

    .sidebar-section {
        color: #9fffd0;
        font-size: 14px;
        font-weight: bold;
        margin-top: 15px;
        letter-spacing: 1px;
    }

    .question-chip {
        background: rgba(0, 255, 170, 0.06);
        border: 1px solid rgba(0, 255, 170, 0.16);
        border-radius: 10px;
        padding: 9px 10px;
        margin: 7px 0;
        font-size: 13px;
        color: #cde8dc;
    }

    .footer {
        text-align: center;
        font-size: 12px;
        color: #65756d;
        margin-top: 35px;
        letter-spacing: 1px;
    }

    @media (max-width: 900px) {
        .status-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .main-title {
            font-size: 36px;
        }
    }

    /* Zone globale du chat input */
    div[data-testid="stChatInput"] {
        background: transparent !important;
        border-top: 1px solid rgba(0, 255, 170, 0.08);
        padding-top: 12px;
    }

    /* Conteneur de la barre de saisie */
    div[data-testid="stChatInput"] > div {
        background: rgba(3, 12, 10, 0.92) !important;
        border: 1px solid rgba(0, 255, 170, 0.28) !important;
        border-radius: 18px !important;
        box-shadow: 0 0 22px rgba(0, 255, 170, 0.08) !important;
    }

    /* Champ de saisie */
    div[data-testid="stChatInput"] textarea {
        background: transparent !important;
        color: #d8f3dc !important;
        border: none !important;
        box-shadow: none !important;
        font-family: Consolas, monospace !important;
        font-size: 14px !important;
    }

    /* Placeholder */
    div[data-testid="stChatInput"] textarea::placeholder {
        color: #6f8f80 !important;
        font-style: italic;
    }

    /* Bouton envoyer */
    div[data-testid="stChatInput"] button {
        background: rgba(0, 255, 170, 0.12) !important;
        border: 1px solid rgba(0, 255, 170, 0.25) !important;
        border-radius: 12px !important;
        color: #9fffd0 !important;
        transition: 0.2s ease-in-out;
    }

    /* Bouton envoyer au survol */
    div[data-testid="stChatInput"] button:hover {
        background: rgba(0, 255, 170, 0.25) !important;
        box-shadow: 0 0 12px rgba(0, 255, 170, 0.35) !important;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)


# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.markdown('<div class="sidebar-title">🜁 CYBERSEC AGENT</div>', unsafe_allow_html=True)
    st.markdown('<span class="muted">Interface de sensibilisation cybersécurité</span>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section">QUESTIONS RAPIDES</div>', unsafe_allow_html=True)

    example_questions = [
        "Comment reconnaître un mail de phishing ?",
        "Comment sécuriser mon Wi-Fi ?",
        "Pourquoi utiliser un VPN ?",
        "Comment créer un bon mot de passe ?",
        "Que faire si j’ai cliqué sur un lien suspect ?",
        "Comment protéger mon compte universitaire ?"
    ]

    for question in example_questions:
        st.markdown(f'<div class="question-chip">{question}</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.markdown('<div class="sidebar-section">MODULES ACTIFS</div>', unsafe_allow_html=True)
    st.markdown(
        """
        - Orchestrateur agentique  
        - Base JSON contrôlée  
        - Mémoire multi-tours  
        - Filtrage défensif  
        - Ollama / Mistral  
        - Docker + Pytest  
        """
    )

    st.markdown("---")
    display_quiz()

    st.markdown("---")

    if st.button("🧹 Réinitialiser la session"):
        st.session_state.messages = []
        st.rerun()


# =========================
# HEADER
# =========================

st.markdown('<div class="main-title">CYBERSEC AGENT</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">assistant agentique · cybersécurité défensive · IA locale</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="terminal-box">
        <div class="terminal-line">> Initialisation du module de sensibilisation...</div>
        <div class="terminal-line">> Agents spécialisés : actifs</div>
        <div class="terminal-line">> Filtre sécurité : activé</div>
        <div class="terminal-line">> Couche IA locale : Ollama / Mistral</div>
        <br>
        <div class="muted">
        Posez une question sur le phishing, les mots de passe, le Wi-Fi, les VPN ou les bonnes pratiques numériques.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="status-grid">
        <div class="status-card">
            <div class="status-title">AGENTS</div>
            <div class="status-value">spécialisés</div>
        </div>
        <div class="status-card">
            <div class="status-title">MÉMOIRE</div>
            <div class="status-value">multi-tours</div>
        </div>
        <div class="status-card">
            <div class="status-title">IA</div>
            <div class="status-value">Ollama/Mistral</div>
        </div>
        <div class="status-card">
            <div class="status-title">SÉCURITÉ</div>
            <div class="status-value">mode défensif</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# CONVERSATION
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_id" not in st.session_state:
    st.session_state.user_id = "user_" + uuid.uuid4().hex[:8]


if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        st.write(
            "Connexion établie. Je suis CyberSec Agent. "
            "Je peux vous aider à comprendre les risques numériques et à appliquer de bonnes pratiques de cybersécurité."
        )


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_question = st.chat_input("Entrez une requête cybersécurité...")

if user_question:
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message("user"):
        st.write(user_question)

    with st.spinner("Analyse de la requête..."):
        conversation_before_question = st.session_state.messages[:-1]
        response = generate_response(user_question, conversation_before_question)
    theme = detect_topic(user_question) or "follow_up"

    save_conversation(
        user_id=st.session_state.user_id,
        question=user_question,
        response=response,
        theme=theme
    )

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)


st.markdown(
    """
    <div class="footer">
    ICy S8 · projet agent de sécurité · version démonstration
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(f"**Session ID :** `{st.session_state.user_id}`")