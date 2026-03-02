import json
from ats_scoring_engine import calculate_ats_score


def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def calculate_skill_score(candidate_skills, required_skills):
    matched = set(candidate_skills).intersection(set(required_skills))

    if len(required_skills) == 0:
        return 0

    return (len(matched) / len(required_skills)) * 100


def calculate_experience_score(candidate_exp, required_exp):
    if required_exp == 0:
        return 100

    if candidate_exp >= required_exp:
        return 100
    else:
        return (candidate_exp / required_exp) * 100


def calculate_education_score(candidate_degree, required_degree):

    # Convert candidate_degree safely to string
    if isinstance(candidate_degree, list):
        temp = []
        for item in candidate_degree:
            if isinstance(item, str):
                temp.append(item)
            elif isinstance(item, dict):
                for v in item.values():
                    temp.append(str(v))
        candidate_degree = " ".join(temp)

    elif isinstance(candidate_degree, dict):
        candidate_degree = " ".join(str(v) for v in candidate_degree.values())

    elif not isinstance(candidate_degree, str):
        candidate_degree = str(candidate_degree)

    # Convert required_degree safely
    if not isinstance(required_degree, str):
        required_degree = str(required_degree)

    if not candidate_degree or not required_degree:
        return 50

    candidate_degree = candidate_degree.lower()
    required_degree = required_degree.lower()

    if candidate_degree == required_degree:
        return 100
    elif required_degree in candidate_degree:
        return 80
    else:
        return 50


def generate_candidate_score(resume_path, job_path, semantic_score):

    resume = load_json(resume_path)
    job = load_json(job_path)

    # ✅ HANDLE LIST-BASED JSON
    if isinstance(resume, list):
        resume = resume[0]

    if isinstance(job, list):
        job = job[0]

    # ===== SAFE DATA EXTRACTION =====
    candidate_name = resume.get("name", "Unknown")

    # ===== SKILLS HANDLING =====
    skills_data = resume.get("skills", [])
    candidate_skills = []

    # If skills is a list
    if isinstance(skills_data, list):
        for skill in skills_data:
            if isinstance(skill, str):
                candidate_skills.append(skill.strip())

    # If skills is a comma-separated string
    elif isinstance(skills_data, str):
        candidate_skills = [
            skill.strip() for skill in skills_data.split(",") if skill.strip()
        ]

    # If skills is a dictionary
    elif isinstance(skills_data, dict):
        for value in skills_data.values():
            if isinstance(value, list):
                for skill in value:
                    if isinstance(skill, str):
                        candidate_skills.append(skill.strip())

    # ===== OTHER DATA =====
    candidate_exp = resume.get("total_experience", 0)
    candidate_degree = resume.get("education", "")

    required_skills = job.get("required_skills", [])
    required_exp = job.get("required_experience", 0)
    required_degree = job.get("required_education", "")
    job_role = job.get("role", "Unknown Role")

    # ===== CALCULATE SCORES =====
    skill_score = calculate_skill_score(candidate_skills, required_skills)
    exp_score = calculate_experience_score(candidate_exp, required_exp)
    edu_score = calculate_education_score(candidate_degree, required_degree)

    final_score = calculate_ats_score(
        job_role,
        skill_score,
        exp_score,
        edu_score,
        semantic_score
    )

    print("\n===== Candidate Final ATS Report =====")
    print(f"Candidate: {candidate_name}")
    print(f"Role: {job_role}")
    print(f"Skill Score: {round(skill_score, 2)}")
    print(f"Experience Score: {round(exp_score, 2)}")
    print(f"Education Score: {round(edu_score, 2)}")
    print(f"Semantic Score: {semantic_score}")
    print(f"\nFinal ATS Score: {round(final_score, 2)}%")

    return final_score