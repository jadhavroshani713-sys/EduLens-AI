# pyrefly: ignore [missing-import]
import ollama
import sys
import io

# Set encoding for Windows terminals to handle emojis if possible, or skip them
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_setup():
    print("--- EduLens AI Offline Verification ---", flush=True)
    
    # 1. Check Ollama Connection
    print("\n1. Checking Ollama connection...", flush=True)
    try:
        models = ollama.list()
        print("✅ Ollama is running.", flush=True)
    except Exception as e:
        print("❌ Ollama is NOT running or not reachable.", flush=True)
        print(f"   Error: {e}", flush=True)
        print("   Action: Please start the Ollama application on your machine.", flush=True)
        return

    # 2. Check for Gemma 2 model
    target_model = "gemma2:2b"
    print(f"\n2. Checking for model: {target_model}...", flush=True)
    
    found = False
    # ollama.list() returns a ModelResponse object in newer versions
    # We should handle both older and newer return types
    try:
        # Newer ollama-python versions return a ListResponse or similar
        model_list = models.models if hasattr(models, 'models') else models.get('models', [])
        for m in model_list:
            # Newer ollama-python uses .model
            name = getattr(m, 'model', '') if not isinstance(m, dict) else m.get('model', m.get('name', ''))
            if target_model in name:
                found = True
                break
    except Exception as e:
        print(f"   Warning: Error parsing model list: {e}", flush=True)
    
    if found:
        print(f"✅ Model '{target_model}' is installed.", flush=True)
    else:
        print(f"⚠️ Model '{target_model}' not found.", flush=True)
        print(f"   Action: Run 'ollama pull {target_model}' in your terminal.", flush=True)

    # 3. Check for Tesseract
    print("\n3. Checking for Tesseract OCR...", flush=True)
    try:
        # pyrefly: ignore [missing-import]
        import pytesseract
        print("✅ pytesseract library is installed.", flush=True)
        # Try to check if tesseract engine is available
        try:
            version = pytesseract.get_tesseract_version()
            print(f"✅ Tesseract Engine version: {version}", flush=True)
        except Exception:
            print("⚠️ Tesseract Engine not found in PATH. OCR features might not work.", flush=True)
            print("   Action: Install Tesseract OCR and add it to your PATH.", flush=True)
    except ImportError:
        print("❌ pytesseract library is NOT installed.", flush=True)

    print("\n--- Verification Complete ---", flush=True)

if __name__ == "__main__":
    check_setup()
