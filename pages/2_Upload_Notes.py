import streamlit as st
import time
from utils.pdf_reader import handle_upload
from utils.ai_engine import summarize_notes
from utils.translator import get_text

# Page Config
st.set_page_config(page_title="Upload Notes - EduLens AI", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

language = st.session_state.get('language', 'English')

st.markdown(f"<h1 class='hero-title'>{get_text('upload_notes', language)}</h1>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📁 Upload Section")
    uploaded_file = st.file_uploader("Drop your PDF or Image notes here", type=["pdf", "png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        
        if st.button(get_text('btn_summarize', language)):
            with st.spinner("Extracting text and generating summary..."):
                # Extract Text
                extracted_text = handle_upload(uploaded_file)
                
                # Store in session state for other pages (like quiz)
                st.session_state['last_extracted_text'] = extracted_text
                
                # Summarize
                result = summarize_notes(extracted_text)
                
                st.session_state['current_summary'] = result
                st.balloons()

with col2:
    st.markdown("### 📝 Analysis Results")
    if 'current_summary' in st.session_state:
        res = st.session_state['current_summary']
        
        tab1, tab2, tab3 = st.tabs(["Summary", "Key Points", "Important Qs"])
        
        with tab1:
            st.markdown(f"<div class='glass-card'>{res['summary']}</div>", unsafe_allow_html=True)
            
        with tab2:
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            for point in res['key_points']:
                st.write(f"- {point}")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with tab3:
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            for q in res['important_questions']:
                st.write(f"❓ {q}")
            st.markdown("</div>", unsafe_allow_html=True)
            
        if st.button("Download Summary as Text"):
            st.download_button("Click to Download", res['summary'], file_name="summary.txt")
    else:
        st.info("Upload a file and click 'Summarize' to see results here.")

# OCR Placeholder Note
st.markdown("---")
st.info("🎨 **OCR Feature**: Currently simulating image-to-text. Tesseract OCR can be integrated for full support.")
