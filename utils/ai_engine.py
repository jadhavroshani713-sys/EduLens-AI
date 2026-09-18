import os
import streamlit as st
import ollama
from google import genai

# Configuration
LOCAL_MODEL = "gemma2:2b"
ONLINE_MODEL = "gemini-3.6-flash"

def get_gemini_client():
    """Configures and returns the Gemini client if API key is available, else None."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        try:
            api_key = st.secrets.get("GEMINI_API_KEY")
        except FileNotFoundError:
            pass
    
    if api_key:
        return genai.Client(api_key=api_key)
    return None

def is_ollama_running():
    """Checks if the local Ollama service is reachable."""
    try:
        ollama.list()
        return True
    except Exception:
        return False

def ask_ai(question, level="beginner", language="English"):
    """
    Solves doubts. Uses Gemini API if online, else local Ollama.
    """
    prompt = f"Explain this to a {level} student in {language}: {question}"
    system_prompt = (
        "You are EduLens AI, a friendly and patient teacher. "
        "Break down complex topics into simple, relatable examples. "
        "Use step-by-step logic. If the level is 'beginner', use very simple words. "
        "Always respond in the requested language."
    )
    
    client = get_gemini_client()

    if client:
        try:
            response = client.models.generate_content(
                model=ONLINE_MODEL,
                contents=f"{system_prompt}\n\nUser Question: {prompt}"
            )
            return response.text
        except Exception as e:
            return f"❌ **Online API Error**: {str(e)}"
    else:
        if not is_ollama_running():
            return "⚠️ **AI Engine Unavailable.** Please provide a `GEMINI_API_KEY` for online use, or start Ollama for offline use."
        try:
            response = ollama.chat(model=LOCAL_MODEL, messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': prompt},
            ])
            return response['message']['content']
        except Exception as e:
            return f"❌ **Local API Error**: {str(e)}\n\nMake sure you have run `ollama pull {LOCAL_MODEL}`"

def ask_ai_stream(question, level="beginner", language="English"):
    """
    Solves doubts with streaming. Uses Gemini API if online, else local Ollama.
    """
    prompt = f"Explain this to a {level} student in {language}: {question}"
    system_prompt = (
        "You are EduLens AI, a friendly and patient teacher. "
        "Break down complex topics into simple, relatable examples. "
        "Use step-by-step logic. If the level is 'beginner', use very simple words. "
        "Always respond in the requested language."
    )
    
    client = get_gemini_client()

    if client:
        try:
            response = client.models.generate_content_stream(
                model=ONLINE_MODEL,
                contents=f"{system_prompt}\n\nUser Question: {prompt}"
            )
            for chunk in response:
                if chunk.text:
                    yield chunk.text
        except Exception as e:
            yield f"❌ **Online API Error**: {str(e)}"
    else:
        if not is_ollama_running():
            yield "⚠️ **AI Engine Unavailable.** Please provide a `GEMINI_API_KEY` for online use, or start Ollama for offline use."
            return
        try:
            stream = ollama.chat(
                model=LOCAL_MODEL,
                messages=[
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': prompt},
                ],
                stream=True,
            )
            for chunk in stream:
                yield chunk['message']['content']
        except Exception as e:
            yield f"❌ **Local API Error**: {str(e)}"

def summarize_notes(text):
    """
    Summarizes educational notes.
    """
    prompt = f"Summarize the following educational text. Provide a concise summary. Format it nicely.\n\nText: {text}"
    system_prompt = "You are an expert academic summarizer. Always provide clear, concise summaries."
    
    client = get_gemini_client()

    if client:
        try:
            response = client.models.generate_content(
                model=ONLINE_MODEL,
                contents=f"{system_prompt}\n\n{prompt}"
            )
            content = response.text
        except Exception as e:
            content = f"Error: {str(e)}"
    else:
        if not is_ollama_running():
            return {"summary": "AI Engine not configured.", "key_points": [], "important_questions": []}
        try:
            response = ollama.chat(model=LOCAL_MODEL, messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': prompt},
            ])
            content = response['message']['content']
        except Exception as e:
            content = f"Error: {str(e)}"
            
    return {
        "summary": content,
        "key_points": ["See AI response above for details"],
        "important_questions": ["Check the AI summary for generated questions"]
    }

def generate_quiz(text, num_questions=3):
    """
    Generates a quiz from text.
    """
    prompt = (
        f"Generate {num_questions} multiple-choice questions from this text. "
        "For each question, provide 4 options and the correct answer. "
        "Format your response as a simple list of questions."
        f"\n\nText: {text}"
    )
    system_prompt = "You are a quiz generator. Create educational MCQs."
    
    client = get_gemini_client()

    if client:
        try:
            response = client.models.generate_content(
                model=ONLINE_MODEL,
                contents=f"{system_prompt}\n\n{prompt}"
            )
            content = response.text
        except Exception:
            content = "Error generating quiz."
    else:
        if not is_ollama_running():
            return []
        try:
            response = ollama.chat(model=LOCAL_MODEL, messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': prompt},
            ])
            content = response['message']['content']
        except Exception:
            content = "Error generating quiz."

    return [
        {
            "question": "AI Generated Quiz (Raw Output)",
            "options": ["Check response below"],
            "answer": content
        }
    ]
