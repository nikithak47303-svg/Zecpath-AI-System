from parser.resume_text_extractor import extract_text
from parser.section_classifier import classify_sections
import json
import os


def parse_resume(file_path):
    """
    Main resume parsing function.
    1. Extracts raw text
    2. Classifies sections
    3. Returns structured resume dictionary
    """

    # 1️⃣ Extract full resume text
    resume_text = extract_text(file_path)

    # 2️⃣ Classify sections
    sections = classify_sections(resume_text)

    # 3️⃣ Build structured parsed object
    parsed = {
        "name": "",
        "email": "",
        "phone": "",
        "linkedin": "",
        "address": "",
        "total_experience": 0,
        "skills": sections.get("skills", "").strip(),
        "experience": sections.get("experience", "").strip(),
        "education": sections.get("education", "").strip(),
        "certifications": sections.get("certifications", "").strip(),
        "projects": sections.get("projects", "").strip()
    }

    return parsed


def save_parsed_resume(parsed_data, output_path):
    """
    Saves parsed resume data as JSON file
    """

    # Create folder if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(parsed_data, f, indent=4)


if __name__ == "__main__":

    input_file = "data/resumes_raw/resume.docx"
    output_file = "data/resumes/parsed/sample_resume.json"

    parsed_resume = parse_resume(input_file)
    save_parsed_resume(parsed_resume, output_file)

    print("Resume parsed and saved successfully.")
