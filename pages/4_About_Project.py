import streamlit as st
from utils.translator import get_text

# Page Config
st.set_page_config(page_title="About - EduLens AI", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

language = st.session_state.get('language', 'English')

st.markdown(f"<h1 class='hero-title'>{get_text('about', language)}</h1>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<div class='glass-card'>
    <h2>🎓 EduLens AI: Your Offline-First AI Teacher</h2>
    <p>EduLens AI was built with a single mission: <b>To make high-quality education accessible to every student, regardless of their background or complexity of the subject matter.</b></p>
    
    <h3>🌟 Core Philosophy</h3>
    <ul>
        <li><b>Simplicity:</b> Turning complex academic jargon into simple, relatable analogies.</li>
        <li><b>Accessibility:</b> Multi-language support to ensure language isn't a barrier to learning.</li>
        <li><b>Efficiency:</b> Quick summaries and instant quizzes to optimize study time.</li>
    </ul>

    <h3>🛠️ Tech Stack</h3>
    <ul>
        <li><b>Frontend & UI:</b> Python + Streamlit</li>
        <li><b>Styling:</b> Custom Glassmorphism CSS</li>
        <li><b>AI Engine:</b> Ready for Gemma 4 (Integration Placeholder)</li>
        <li><b>File Processing:</b> PyPDF2 & PIL</li>
    </ul>

    <h3>🚀 Future Scope</h3>
    <ul>
        <li><b>Voice Assistant:</b> Hands-free learning for visually impaired students.</li>
        <li><b>Full Offline Mode:</b> Local LLM integration for zero-internet learning.</li>
        <li><b>OCR Support:</b> Better handwriting recognition for scanned notes.</li>
        <li><b>Progress Tracking:</b> Gamified learning with badges and certificates.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("### 👨‍💻 Developed for Gemma 4 Good Hackathon")
st.write("Ensuring that AI serves the goal of universal education accessibility.")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("⭐ Hackathon Ready")
with col2:
    st.info("🌐 Multi-language")
with col3:
    st.info("📱 Responsive UI")
