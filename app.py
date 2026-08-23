import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
from utils.translator import get_text
from utils.ai_engine import is_ollama_running, DEFAULT_MODEL

# Page Configuration
st.set_page_config(
    page_title="EduLens AI - Offline Smart Education",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

# Lottie Animation Loader
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

lottie_edu = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_DMg9z1.json") # Education animation

# Sidebar Settings
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3449/3449692.png", width=100)
    st.title("EduLens AI")
    st.markdown("---")
    
    # AI Status Indicator
    st.subheader("🤖 AI Status")
    if is_ollama_running():
        st.success(f"**Connected to {DEFAULT_MODEL}**")
        st.caption("✅ Processing is 100% Local & Private")
    else:
        st.error("**Ollama Offline**")
        st.warning("Please start Ollama to use AI features.")
    
    st.markdown("---")
    language = st.selectbox("🌐 Select Language", ["English", "Hindi", "Marathi"])
    st.session_state['language'] = language
    
    st.markdown("---")
    st.info("💡 **Tip**: EduLens AI works completely without internet once the model is downloaded!")
    
    st.sidebar.markdown("---")
    st.sidebar.write("v1.1.0-offline | Privacy First")

# Home Page Content
def main():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"<h1 class='hero-title'>{get_text('welcome', language)}</h1>", unsafe_allow_html=True)
        st.markdown(f"<p class='hero-subtitle'>{get_text('subtitle', language)}</p>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='glass-card'>
            <h3>🛡️ Privacy-First, Fully Offline Learning</h3>
            <p>EduLens AI is your personal academic companion that runs <b>entirely on your machine</b>. 
            No data leaves your device, making it the most secure and private way to learn with AI.
            Powered by local LLMs via Ollama.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        if lottie_edu:
            st_lottie(lottie_edu, height=300, key="edu_anim")
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/3449/3449692.png")

    st.markdown("## 🛠️ Offline Features")
    
    # Feature Cards Grid
    f_col1, f_col2, f_col3 = st.columns(3)
    
    with f_col1:
        st.markdown(f"""
        <div class='feature-item'>
            <span class='feature-icon'>🤔</span>
            <h4>{get_text('ask_doubt', language)}</h4>
            <p>Get instant, simple explanations from your local AI.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with f_col2:
        st.markdown(f"""
        <div class='feature-item'>
            <span class='feature-icon'>📝</span>
            <h4>{get_text('upload_notes', language)}</h4>
            <p>Local OCR and summarization for your PDFs.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with f_col3:
        st.markdown(f"""
        <div class='feature-item'>
            <span class='feature-icon'>🎯</span>
            <h4>{get_text('generate_quiz', language)}</h4>
            <p>Test yourself with locally generated MCQs.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Why this project matters
    st.markdown("### 🌍 Why Offline AI Matters")
    st.write("""
    Many students lack consistent internet access or worry about data privacy. 
    By bringing AI directly to the user's device, EduLens AI ensures that high-quality 
    educational assistance is available anywhere, anytime, to everyone—regardless of 
    connectivity or privacy concerns.
    """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #94a3b8;'>"
        "© 2026 EduLens AI | Offline Edition | Powered by Local Gemma 2"
        "</div>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
