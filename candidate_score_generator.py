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
    if candidate_exp >= required_exp:
        return 100
    else:
        return (candidate_exp / required_exp) * 100


def calculate_education_score(candidate_degree, required_degree):
    if candidate_degree.lower() == required_degree.lower():
        return 100
    elif candidate_degree.lower() in required_degree.lower():
        return 80
    else:
        return 50


def generate_candidate_score(resume_path, job_path, semantic_score):

    resume = load_json(resume_path)
    job = load_json(job_path)

    skill_score = calculate_skill_score(
        resume["skills"],
        job["required_skills"]
    )

    exp_score = calculate_experience_score(
        resume["experience_years"],
        job["required_experience"]
    )

    edu_score = calculate_education_score(
        resume["education"],
        job["required_education"]
    )

    final_score = calculate_ats_score(
        job["role"],
        skill_score,
        exp_score,
        edu_score,
        semantic_score
    )

    print("\n===== Candidate Final ATS Report =====")
    print(f"Candidate: {resume['name']}")
    print(f"Role: {job['role']}")
    print(f"Skill Score: {round(skill_score, 2)}")
    print(f"Experience Score: {round(exp_score, 2)}")
    print(f"Education Score: {round(edu_score, 2)}")
    print(f"Semantic Score: {semantic_score}")
    print(f"\nFinal ATS Score: {final_score}%")


if __name__ == "__main__":
 generate_candidate_score(
    "data/sample_resume.json",
    "data/jobs/software_engineer.json",
    semantic_score=82
)