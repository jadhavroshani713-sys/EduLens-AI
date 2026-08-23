import streamlit as st
import time
from utils.quiz_generator import create_mcqs
from utils.translator import get_text

# Page Config
st.set_page_config(page_title="Generate Quiz - EduLens AI", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

language = st.session_state.get('language', 'English')

st.markdown(f"<h1 class='hero-title'>{get_text('generate_quiz', language)}</h1>", unsafe_allow_html=True)
st.markdown("---")

# Source Selection
source = st.radio("Choose Quiz Source", ["Use Recently Uploaded Notes", "Enter a Specific Topic"])

if source == "Use Recently Uploaded Notes":
    text_source = st.session_state.get('last_extracted_text', None)
    if not text_source:
        st.warning("No notes found. Please upload notes first in the 'Upload Notes' section.")
else:
    text_source = st.text_input("Enter Topic (e.g. 'Human Digestive System')")

num_q = st.number_input("Number of Questions", min_value=1, max_value=10, value=3)

if st.button(get_text('btn_quiz', language)):
    if text_source:
        with st.spinner("Generating MCQs..."):
            st.session_state['quiz_data'] = create_mcqs(text_source, num_q)
            st.session_state['quiz_score'] = 0
            st.session_state['answers_submitted'] = False
    else:
        st.error("Please provide a topic or upload notes!")

# Display Quiz
if 'quiz_data' in st.session_state:
    st.markdown("### 📝 Your Quiz")
    
    quiz_form = st.form(key='quiz_form')
    user_answers = {}
    
    for i, q in enumerate(st.session_state['quiz_data']):
        quiz_form.markdown(f"**Q{i+1}: {q['question']}**")
        user_answers[i] = quiz_form.radio(f"Select option for Q{i+1}", q['options'], key=f"q_{i}")
        quiz_form.markdown("---")
        
    submit = quiz_form.form_submit_button("Submit Answers")
    
    if submit:
        score = 0
        st.session_state['answers_submitted'] = True
        for i, q in enumerate(st.session_state['quiz_data']):
            if user_answers[i] == q['answer']:
                score += 1
        
        st.session_state['quiz_score'] = score
        
    if st.session_state.get('answers_submitted', False):
        st.markdown(f"<div class='glass-card'><h3>Your Score: {st.session_state['quiz_score']} / {len(st.session_state['quiz_data'])}</h3></div>", unsafe_allow_html=True)
        
        if st.session_state['quiz_score'] == len(st.session_state['quiz_data']):
            st.balloons()
            st.success("Perfect! You're a master of this topic!")
        elif st.session_state['quiz_score'] > len(st.session_state['quiz_data']) / 2:
            st.info("Good job! Keep practicing.")
        else:
            st.warning("Need more study. Try summarizing your notes again!")
            
        if st.button("Generate More Questions"):
            # This will refresh and allow new generation
            del st.session_state['quiz_data']
            st.rerun()

# Footer Note
st.markdown("---")
st.caption("🎯 Tip: Re-taking quizzes helps in better memory retention.")
