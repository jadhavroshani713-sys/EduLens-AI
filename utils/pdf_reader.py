import PyPDF2
from PIL import Image
import io
# pyrefly: ignore [missing-import]
import pytesseract # Offline OCR library

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file using PyPDF2.
    """
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text.strip()
    except Exception as e:
        return f"Error extracting PDF: {str(e)}"

def extract_text_from_image(image_file):
    """
    Extracts text from an image using pytesseract (Offline OCR).
    Note: Requires Tesseract-OCR engine installed on the system.
    """
    try:
        img = Image.open(image_file)
        text = pytesseract.image_to_string(img)
        if not text.strip():
            return "⚠️ No text detected in image. Please ensure the image is clear."
        return text.strip()
    except Exception as e:
        return (
            f"❌ OCR Error: {str(e)}\n\n"
            "**Note**: Make sure Tesseract-OCR is installed on your system. "
            "Download it from: https://github.com/UB-Mannheim/tesseract/wiki"
        )

def handle_upload(uploaded_file):
    """
    Directs the file to the correct extractor based on type.
    """
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type in ["image/png", "image/jpeg", "image/jpg"]:
        return extract_text_from_image(uploaded_file)
    else:
        return "Unsupported file type."
