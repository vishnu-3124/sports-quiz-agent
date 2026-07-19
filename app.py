import streamlit as st
from src.generator import compile_quiz_data
from src.database import setup_and_populate_db

# 1. Cache the knowledge base setup so it only populates ChromaDB once on startup
@st.cache_resource
def prepare_knowledge_base():
    setup_and_populate_db()

prepare_knowledge_base()

# 2. Page configurations
st.set_page_config(page_title="Sports Quiz Agent", page_icon="🏆", layout="centered")

st.title("🏆 AI-Powered Sports Quiz Generator")
st.write("Challenge yourself or generate engaging social media content! Powered by RAG (ChromaDB + Web Search).")

# 3. Sidebar inputs
st.sidebar.header("Quiz Settings")
sport_choice = st.sidebar.selectbox("Select Sport", ["Cricket", "Football", "Badminton"])
difficulty = st.sidebar.select_slider("Select Difficulty", options=["Easy", "Medium", "Hard"])

# 4. Initialize session state to lock the quiz text so it doesn't vanish on hot-reloads
if "quiz_output" not in st.session_state:
    st.session_state.quiz_output = None
    st.session_state.quiz_context = None

# Button to trigger compilation pipeline
if st.sidebar.button("Generate Fresh Quiz", use_container_width=True):
    with st.spinner("Fetching historical facts & scouring the live web..."):
        try:
            quiz_text, context_used = compile_quiz_data(sport_choice, difficulty)
            st.session_state.quiz_output = quiz_text
            st.session_state.quiz_context = context_used
            st.success("Quiz created successfully!")
        except Exception as e:
            st.error(f"Failed to generate quiz: {e}")

# 5. Display the generated output
if st.session_state.quiz_output:
    st.subheader(f"Current Quiz: {sport_choice} ({difficulty})")
    st.text_area("Generated Quiz Output (Ready to share!)",
                 value=st.session_state.quiz_output,
                 height=350)

    # Expandable window showcasing the "ground truth context" for audit purposes
    with st.expander("🔍 Inspect Ground Truth (RAG Context Used)"):
        st.code(st.session_state.quiz_context, language="markdown")