import re
import json


# ----------------------------
# EXPERIENCE PARSER
# ----------------------------
def extract_experience(resume_text):
    experiences = []

    pattern = r"(.*?) at (.*?) from (\d{4}) to (\d{4})"
    matches = re.findall(pattern, resume_text)

    for match in matches:
        designation, company, start_year, end_year = match

        duration = int(end_year) - int(start_year)

        experience_object = {
            "experience_id": f"EXP{len(experiences)+1:03}",
            "company_name": company.strip(),
            "job_title": designation.strip(),
            "employment_type": "Full-Time",
            "start_year": int(start_year),
            "end_year": int(end_year),
            "duration_years": duration,
            "is_current_job": False,
            "skills_used": [],
            "job_level": "Mid-Level",
            "domain": "IT Services",
            "is_relevant": False,
            "relevance_score": 0
        }

        experiences.append(experience_object)

    return experiences


# ----------------------------
# EXPERIENCE RELEVANCE ENGINE
# ----------------------------
def calculate_experience_relevance(experiences, target_role):
    total_experience = 0
    relevant_experience = 0

    role_keywords = {
        "backend developer": ["software engineer", "backend developer", "python developer"],
        "data analyst": ["data analyst", "business analyst", "data scientist"],
        "hr manager": ["hr executive", "recruiter", "hr manager"]
    }

    target_role = target_role.lower()

    for exp in experiences:
        duration = exp["duration_years"]
        total_experience += duration

        if target_role in role_keywords:
            if exp["job_title"].lower() in role_keywords[target_role]:
                relevant_experience += duration
                exp["is_relevant"] = True
                exp["relevance_score"] = duration
            else:
                exp["is_relevant"] = False
                exp["relevance_score"] = 0
        else:
            exp["is_relevant"] = False
            exp["relevance_score"] = 0

    if total_experience == 0:
        relevance_score = 0
    else:
        relevance_score = (relevant_experience / total_experience) * 100

    return {
        "total_experience_years": total_experience,
        "relevant_experience_years": relevant_experience,
        "experience_relevance_score": round(relevance_score, 2),
        "experience_details": experiences
    }


# ----------------------------
# TEST BLOCK
# ----------------------------
if __name__ == "__main__":
    sample_resume = """
    Software Engineer at Infosys from 2022 to 2024
    Data Analyst at TCS from 2020 to 2022
    """

    experiences = extract_experience(sample_resume)

    target_role = "Backend Developer"

    result = calculate_experience_relevance(experiences, target_role)

    print("\nExperience Relevance Result:\n")
    print(json.dumps(result, indent=4))