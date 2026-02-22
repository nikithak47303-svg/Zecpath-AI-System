# Section heading keywords
SECTION_KEYWORDS = {
    "skills": ["skills", "technical skills", "core competencies", "expertise"],
    "experience": ["experience", "work experience", "employment history", "professional experience"],
    "education": ["education", "academic background", "qualifications"],
    "certifications": ["certifications", "licenses", "professional certifications"],
    "projects": ["projects", "academic projects", "personal projects"]
}


def classify_sections(resume_text):

    sections = {
        "skills": "",
        "experience": "",
        "education": "",
        "certifications": "",
        "projects": ""
    }

    current_section = None
    lines = resume_text.split("\n")

    for line in lines:
        clean_line = line.strip().lower()

        # Check if line matches a heading
        found_heading = False

        for section, keywords in SECTION_KEYWORDS.items():
            if clean_line in keywords:
                current_section = section
                found_heading = True
                break

        # If not a heading and inside a section
        if not found_heading and current_section:
            sections[current_section] += line.strip() + "\n"

    return sections