import streamlit as st
import time
from utils.ai_engine import ask_ai, ask_ai_stream
from utils.translator import get_text

# Page Config
st.set_page_config(page_title="Ask Doubt - EduLens AI", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Get current language from session state
language = st.session_state.get('language', 'English')

st.markdown(f"<h1 class='hero-title'>{get_text('ask_doubt', language)}</h1>", unsafe_allow_html=True)
st.markdown("---")

# Layout
col1, col2 = st.columns([2, 1])

with col2:
    st.markdown("### ⚙️ Settings")
    level = st.select_slider("Select Explanation Level", options=["beginner", "intermediate", "expert"], value="beginner")
    st.info("💡 **Beginner Mode**: Uses simple analogies and easy words.\n\n**Expert Mode**: Provides technical depth and academic terminology.")
    
    st.markdown("### 📚 Demo Questions")
    demo_q = [
        "What is Photosynthesis?",
        "Explain Pass by Reference in C++",
        "How do black holes form?",
        "What is the Pythagorean Theorem?"
    ]
    for q in demo_q:
        if st.button(q, use_container_width=True):
            st.session_state['current_q'] = q

with col1:
    question = st.text_area("What would you like to learn today?", 
                            value=st.session_state.get('current_q', ''),
                            placeholder=get_text('placeholder_question', language),
                            height=150)
    
    if st.button(get_text('btn_ask', language)):
        if question:
            st.markdown("### 🎓 AI Explanation")
            with st.container():
                # Use a placeholder for the glass-card style but we'll stream into it
                # Streamlit's write_stream doesn't easily nest in a custom HTML div while streaming
                # So we'll use a container and style it if possible or just use standard write
                response_placeholder = st.empty()
                full_response = ""
                
                # Streaming with a nice container
                with st.chat_message("assistant", avatar="🎓"):
                    full_response = st.write_stream(ask_ai_stream(question, level=level, language=language))
            
            # Success notification
            st.toast("I hope this helps! Feel free to ask follow-up questions.", icon='🎓')
        else:
            st.warning("Please enter a question first!")

# Offline Note
st.markdown("---")
st.caption("🛡️ **Privacy Guard**: All processing happens locally on your machine via Ollama. No data is sent to the cloud.")
