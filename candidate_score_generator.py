import json
import re

# ==============================
# HELPER FUNCTIONS
# ==============================

def normalize_text(text):
    """Lowercase and convert list/dict items into a single string for comparison."""
    if not text:
        return ""
    
    if isinstance(text, list):
        new_list = []
        for item in text:
            if isinstance(item, str):
                new_list.append(item)
            elif isinstance(item, dict):
                new_list.append(" ".join(str(v) for v in item.values()))
        text = " ".join(new_list)
    
    elif isinstance(text, dict):
        text = " ".join(str(v) for v in text.values())
    
    # Remove extra spaces and lowercase
    return str(text).strip().lower()


def match_skills(candidate_skills, required_skills):
    """Return skill match percentage (0-100) with partial matching."""
    if not candidate_skills or not required_skills:
        return 0

    candidate_skills_text = " ".join([normalize_text(s) for s in candidate_skills])
    required_skills = [normalize_text(s) for s in required_skills]

    matched_count = 0
    for skill in required_skills:
        # Partial match: check if skill is contained in candidate text
        if re.search(r'\b' + re.escape(skill) + r'\b', candidate_skills_text):
            matched_count += 1

    return (matched_count / len(required_skills)) * 100


def match_experience(candidate_exp_years, min_exp_required):
    """Return experience match percentage (0-100)."""
    if candidate_exp_years is None or min_exp_required is None:
        return 0

    if candidate_exp_years >= min_exp_required:
        return 100

    return (candidate_exp_years / min_exp_required) * 100


def match_education(candidate_edu, required_edu):
    """Return education match percentage (0-100) with partial matching."""
    if not candidate_edu or not required_edu:
        return 0

    candidate_edu = normalize_text(candidate_edu)
    required_edu = normalize_text(required_edu)

    # Partial match: split required education into words
    req_words = required_edu.split()
    matched_words = sum(1 for w in req_words if w in candidate_edu)

    return (matched_words / len(req_words)) * 100 if req_words else 0


# ==============================
# MAIN SCORE FUNCTION
# ==============================

def generate_candidate_score(resume_path, job_data):
    """
    Calculate candidate score (0-100%) based on:
    - Skills (50%)
    - Experience (30%)
    - Education (20%)
    """
    with open(resume_path, "r") as f:
        resume_data = json.load(f)

    if isinstance(resume_data, list):
        resume_data = resume_data[0]

    # Candidate info
    candidate_skills = resume_data.get("skills", [])
    candidate_exp_years = resume_data.get("total_experience_years", 0)
    candidate_education = resume_data.get("education", "")

    # Job info
    required_skills = job_data.get("required_skills", [])
    min_experience = job_data.get("min_experience_years", 0)
    required_education = job_data.get("required_education", "")

    # Compute partial scores
    skill_score = match_skills(candidate_skills, required_skills)
    exp_score = match_experience(candidate_exp_years, min_experience)
    edu_score = match_education(candidate_education, required_education)

    # Weighted total
    total_score = (0.5 * skill_score) + (0.3 * exp_score) + (0.2 * edu_score)

    return round(total_score, 2)