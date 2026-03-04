# ==============================
# NORMALIZATION ENGINE
# ==============================

# ---------------------------------
# RESUME NORMALIZATION
# ---------------------------------
def normalize_resume_data(resume_data):
    """Normalize resume data into standard structured format."""

    # Normalize Skills
    skills = resume_data.get("skills", [])
    if isinstance(skills, str):
        skills = skills.split(",")

    normalized_skills = []
    for skill in skills:
        if skill:
            normalized_skills.append(str(skill).strip().lower())

    # Normalize Experience
    exp = resume_data.get("experience_years", 0)
    try:
        exp = float(exp)
    except:
        exp = 0

    # Normalize Education
    education = resume_data.get("education", [])
    normalized_education = []

    if isinstance(education, str):
        normalized_education.append(education.strip().lower())

    elif isinstance(education, list):
        for edu in education:
            if isinstance(edu, dict):
                degree = edu.get("degree", "")
                if degree:
                    normalized_education.append(str(degree).strip().lower())
            elif isinstance(edu, str):
                normalized_education.append(edu.strip().lower())

    return {
        "skills": normalized_skills,
        "experience_years": exp,
        "education": normalized_education
    }


# ---------------------------------
# JOB NORMALIZATION
# ---------------------------------
def normalize_job_data(job_data):
    """Normalize job description data."""

    # Normalize Required Skills
    required_skills = job_data.get("required_skills", [])
    if isinstance(required_skills, str):
        required_skills = required_skills.split(",")

    normalized_skills = []
    for skill in required_skills:
        if skill:
            normalized_skills.append(str(skill).strip().lower())

    # Normalize Required Experience
    required_exp = job_data.get("required_experience_years", 0)
    try:
        required_exp = float(required_exp)
    except:
        required_exp = 0

    # Normalize Required Education
    required_education = job_data.get("required_education", [])
    normalized_education = []

    if isinstance(required_education, str):
        normalized_education.append(required_education.strip().lower())

    elif isinstance(required_education, list):
        for edu in required_education:
            if isinstance(edu, dict):
                degree = edu.get("degree", "")
                if degree:
                    normalized_education.append(str(degree).strip().lower())
            elif isinstance(edu, str):
                normalized_education.append(edu.strip().lower())

    return {
        "role": job_data.get("role", "default"),
        "required_skills": normalized_skills,
        "required_experience_years": required_exp,
        "required_education": normalized_education
    }