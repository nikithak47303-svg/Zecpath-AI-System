import docx
import re

# ------------------------
# DOCX Reader
# ------------------------
def extract_text_from_docx(file_path):
    text = ""

    doc = docx.Document(file_path)
    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


# ------------------------
# Main Extract Function
# ------------------------
def extract_resume_text(file_path):
    if file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        return "Unsupported file format"
    import re


# ------------------------
# Clean Resume Text
# ------------------------
def clean_resume_text(text):

    # Remove extra spaces and line breaks
    text = re.sub(r'\s+', ' ', text)

    # Remove unwanted special characters
    text = re.sub(r'[^a-zA-Z0-9.,@+\-\s]', '', text)

    # Convert to lowercase
    text = text.lower()

    return text.strip()