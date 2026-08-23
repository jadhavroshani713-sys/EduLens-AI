UI_TEXT = {
    "English": {
        "welcome": "Welcome to EduLens AI",
        "subtitle": "Offline AI Teacher for Every Student",
        "ask_doubt": "Ask a Doubt",
        "upload_notes": "Upload Notes",
        "generate_quiz": "Generate Quiz",
        "about": "About Project",
        "placeholder_question": "What is pass by reference in C++?",
        "btn_ask": "Ask AI Teacher",
        "btn_summarize": "Summarize My Notes",
        "btn_quiz": "Generate Quiz Questions"
    },
    "Hindi": {
        "welcome": "EduLens AI में आपका स्वागत है",
        "subtitle": "हर छात्र के लिए ऑफलाइन एआई शिक्षक",
        "ask_doubt": "सवाल पूछें",
        "upload_notes": "नोट्स अपलोड करें",
        "generate_quiz": "क्विज बनाएं",
        "about": "परियोजना के बारे में",
        "placeholder_question": "C++ में 'pass by reference' क्या है?",
        "btn_ask": "एआई शिक्षक से पूछें",
        "btn_summarize": "मेरे नोट्स का सारांश दें",
        "btn_quiz": "क्विज प्रश्न तैयार करें"
    },
    "Marathi": {
        "welcome": "EduLens AI मध्ये आपले स्वागत आहे",
        "subtitle": "प्रत्येक विद्यार्थ्यासाठी ऑफलाइन AI शिक्षक",
        "ask_doubt": "शंका विचारा",
        "upload_notes": "नोट्स अपलोड करा",
        "generate_quiz": "क्विझ तयार करा",
        "about": "प्रकल्पाबद्दल",
        "placeholder_question": "C++ मध्ये 'pass by reference' म्हणजे काय?",
        "btn_ask": "AI शिक्षकाला विचारा",
        "btn_summarize": "माझ्या नोट्सचा सारांश द्या",
        "btn_quiz": "क्विझ प्रश्न तयार करा"
    }
}

def get_text(key, lang="English"):
    """
    Returns the translated string for a given key and language.
    """
    return UI_TEXT.get(lang, UI_TEXT["English"]).get(key, UI_TEXT["English"][key])
