# 🎓 EduLens AI - Offline-Friendly AI Teacher Assistant

EduLens AI is a modern, student-focused web application designed to simplify learning. Built for the **Gemma 4 Good Hackathon**, it leverages AI to help students understand complex topics, summarize academic notes, and test their knowledge—all within a premium, multi-language interface.

![EduLens AI Banner](https://img.shields.io/badge/Education-AI-blueviolet?style=for-the-badge&logo=google-cloud)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🚀 Features

### 1. 🤔 AI Doubt Solver
- Ask any academic question and get instant, simplified explanations.
- **Beginner Mode**: Automatically simplifies complex jargon into easy-to-understand analogies.
- **Step-by-Step Logic**: Breaks down answers into logical chunks.

### 2. 📝 Notes Summarizer
- Upload PDF files or images of your handwritten/printed notes.
- Extract key points, short summaries, and potential exam questions automatically.

### 3. 🎯 Quiz Generator
- Instantly generate Multiple Choice Questions (MCQs) from your uploaded notes or a specific topic.
- Interactive scoring system to track your understanding.

### 4. 🌐 Multi-language Support
- Supports **English, Hindi, and Marathi** to make education accessible to a wider audience.

### 5. 💎 Premium UI/UX
- **Glassmorphism Design**: Sleek, modern interface with backdrop-filters and smooth transitions.
- **Responsive Dashboard**: Works seamlessly across desktops and tablets.
- **Dark-themed Aesthetic**: Student-friendly professional dark mode for late-night study sessions.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jadhavroshani713-sys/EduLens-AI.git
   cd edulens-ai
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Configure Online Mode:**
   To host this app online (e.g., Streamlit Cloud) where local Ollama isn't available, the app uses the Google Gemini API to access advanced AI models in the cloud.
   - Create a `.streamlit/secrets.toml` file in the project root.
   - Add your Gemini API Key:
     ```toml
     GEMINI_API_KEY = "your-gemini-api-key-here"
     ```
   *(If you run this locally with Ollama installed, you can skip this step and the app will run 100% offline).*

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

---

## 📂 Project Structure

```text
edulens-ai/
├── app.py                  # Main entry point (Home Page)
├── requirements.txt        # Project dependencies
├── README.md               # Documentation
├── assets/                 # CSS & Styling
├── utils/                  # Core modules
│   ├── ai_engine.py        # Logic for AI processing
│   ├── pdf_reader.py       # PDF/Image extraction
│   ├── quiz_generator.py   # MCQ generation logic
│   └── translator.py       # UI Translation strings
└── pages/                  # Multi-page routing
    ├── 1_Ask_Doubt.py
    ├── 2_Upload_Notes.py
    ├── 3_Generate_Quiz.py
    └── 4_About_Project.py
```

---

## 🔮 Future Scope
- **Voice-to-Text**: Ask doubts using voice commands.
- **OCR Integration**: Full support for handwriting recognition via Tesseract or Google Lens API.
- **Offline LLM**: Run local models (like Gemma 2b) for 100% offline usage.
- **Analytics Dashboard**: Track student progress over time.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License
This project is licensed under the MIT License.

---
**EduLens AI** - *Empowering every student with the lens of AI.*
