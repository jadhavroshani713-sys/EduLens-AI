import random
import time

def create_mcqs(text, num=5):
    """
    Parses extracted text and generates MCQs.
    Currently uses placeholder logic.
    """
    time.sleep(1)
    
    # Simple logic to generate "Topic" based questions if text is short
    topic = text[:30] + "..." if len(text) > 30 else text
    
    questions = [
        {
            "id": 1,
            "question": f"Based on the content about '{topic}', what is the primary objective?",
            "options": ["To inform", "To entertain", "To persuade", "To analyze"],
            "answer": "To inform"
        },
        {
            "id": 2,
            "question": "Which of the following is a key component mentioned in the text?",
            "options": ["Standard Procedure", "Random Variable", "Hypothetical Scenario", "None of the above"],
            "answer": "Standard Procedure"
        },
        {
            "id": 3,
            "question": "How does the author suggest approaching the problem?",
            "options": ["Systematically", "Instinctively", "By ignoring it", "With external help"],
            "answer": "Systematically"
        },
        {
            "id": 4,
            "question": "What is the expected outcome of following the guidelines?",
            "options": ["Failure", "Success", "Ambiguity", "More questions"],
            "answer": "Success"
        },
        {
            "id": 5,
            "question": "Who is the intended audience for this information?",
            "options": ["Students", "Experts", "General Public", "All of the above"],
            "answer": "Students"
        }
    ]
    
    return random.sample(questions, min(num, len(questions)))
