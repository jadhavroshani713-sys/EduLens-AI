import time
import random
import ollama

# Configuration
DEFAULT_MODEL = "gemma2:2b"  # Smaller model for better compatibility

def is_ollama_running():
    """Checks if the Ollama service is reachable."""
    try:
        ollama.list()
        return True
    except Exception:
        return False

def ask_ai(question, level="beginner", language="English"):
    """
    Solves doubts using local Gemma 2 model via Ollama.
    """
    if not is_ollama_running():
        return "⚠️ **Ollama is not running.** Please start Ollama on your machine to use the AI features."

    prompt = f"Explain this to a {level} student in {language}: {question}"
    
    system_prompt = (
        "You are EduLens AI, a friendly and patient teacher. "
        "Break down complex topics into simple, relatable examples. "
        "Use step-by-step logic. If the level is 'beginner', use very simple words. "
        "Always respond in the requested language."
    )

    try:
        response = ollama.chat(model=DEFAULT_MODEL, messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt},
        ])
        return response['message']['content']
    except Exception as e:
        return f"❌ **Error connecting to AI model**: {str(e)}\n\nMake sure you have run `ollama pull {DEFAULT_MODEL}`"

def ask_ai_stream(question, level="beginner", language="English"):
    """
    Solves doubts using local Gemma 2 model via Ollama with streaming.
    """
    if not is_ollama_running():
        yield "⚠️ **Ollama is not running.** Please start Ollama on your machine."
        return

    prompt = f"Explain this to a {level} student in {language}: {question}"
    
    system_prompt = (
        "You are EduLens AI, a friendly and patient teacher. "
        "Break down complex topics into simple, relatable examples. "
        "Use step-by-step logic. If the level is 'beginner', use very simple words. "
        "Always respond in the requested language."
    )

    try:
        stream = ollama.chat(
            model=DEFAULT_MODEL,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': prompt},
            ],
            stream=True,
        )
        for chunk in stream:
            yield chunk['message']['content']
    except Exception as e:
        yield f"❌ **Error connecting to AI model**: {str(e)}"

def summarize_notes(text):
    """
    Summarizes educational notes using local AI.
    """
    if not is_ollama_running():
        return {"summary": "Ollama not running.", "key_points": [], "important_questions": []}

    prompt = f"Summarize the following educational text. Provide a summary, 4 key points, and 3 important study questions. Return the response in a structured format.\n\nText: {text}"

    try:
        response = ollama.chat(model=DEFAULT_MODEL, messages=[
            {'role': 'system', 'content': "You are an expert academic summarizer. Always provide clear, concise summaries."},
            {'role': 'user', 'content': prompt},
        ])
        content = response['message']['content']
        
        # Simple parsing logic (AI might not always return clean JSON without specific prompting)
        # For now, we'll return a structured-looking string or try to parse if we used a tool-call style
        # But to keep it simple and robust for local LLMs:
        return {
            "summary": content,
            "key_points": ["See AI response above for details"],
            "important_questions": ["Check the AI summary for generated questions"]
        }
    except Exception as e:
        return {"summary": f"Error: {str(e)}", "key_points": [], "important_questions": []}

def generate_quiz(text, num_questions=3):
    """
    Generates a quiz from text using local AI.
    """
    if not is_ollama_running():
        return []

    prompt = (
        f"Generate {num_questions} multiple-choice questions from this text. "
        "For each question, provide 4 options and the correct answer. "
        "Format your response as a simple list of questions."
        f"\n\nText: {text}"
    )

    try:
        response = ollama.chat(model=DEFAULT_MODEL, messages=[
            {'role': 'system', 'content': "You are a quiz generator. Create educational MCQs."},
            {'role': 'user', 'content': prompt},
        ])
        # In a real app, we'd parse this into a list of dicts. 
        # For this demo, we'll return a formatted string or a mock that indicates real AI was used.
        content = response['message']['content']
        
        # Placeholder for parsing logic - returning a formatted string as a "mock" item for the UI to display
        return [
            {
                "question": "AI Generated Quiz (Raw Output)",
                "options": ["Check response below"],
                "answer": content
            }
        ]
    except Exception:
        return []
