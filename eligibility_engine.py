# eligibility_engine.py
import json
from datetime import datetime

# ==============================
# Sample Candidates (You can replace this with real parsed resumes)
# ==============================
sample_candidates = [
    {"name": "Arjun Menon", "skills": ["Python", "SQL"], "experience": 3},
    {"name": "Rahul Nair", "skills": ["Java", "HTML"], "experience": 2},
    {"name": "Neha Pillai", "skills": ["Excel", "Power BI"], "experience": 1}
]

# ==============================
# Sample Job Requirements
# ==============================
job_requirements = {
    "job_id": "AUD020",
    "required_skills": ["Python", "SQL", "Data Analysis"],
    "min_experience": 2
}

# ==============================
# Function: Calculate ATS Score
# ==============================
def calculate_ats_score(candidate, required_skills, min_experience):
    # Simple scoring: 50 base score
    score = 50
    
    # Skill matching (10 points per match)
    matched_skills = set(skill.lower() for skill in candidate["skills"]) & set(skill.lower() for skill in required_skills)
    score += len(matched_skills) * 10
    
    # Experience bonus
    if candidate["experience"] >= min_experience:
        score += 10
    else:
        score -= 10
    
    # Ensure score is between 0-100
    score = max(0, min(score, 100))
    return score

# ==============================
# Function: Determine Eligibility Status
# ==============================
def determine_eligibility_status(score):
    if score >= 70:
        return "Eligible"
    elif score >= 50:
        return "Review"
    else:
        return "Rejected"

# ==============================
# Eligibility Engine
# ==============================
def run_eligibility_engine(candidates, job):
    results = []
    for c in candidates:
        score = calculate_ats_score(c, job["required_skills"], job["min_experience"])
        status = determine_eligibility_status(score)
        results.append({
            "name": c["name"],
            "score": score,
            "eligibility_status": status
        })
    return results

# ==============================
# Generate Structured Result
# ==============================
def generate_result_structure(job_id, candidates):
    result = {
        "job_id": job_id,
        "evaluation_date": datetime.now().strftime("%Y-%m-%d"),
        "candidates": []
    }

    for c in candidates:
        candidate_data = {
            "candidate_name": c["name"],
            "ats_score": c["score"],
            "eligibility_status": c["eligibility_status"]
        }
        result["candidates"].append(candidate_data)

    return result

# ==============================
# Main Execution
# ==============================
if __name__ == "__main__":
    job_id = job_requirements["job_id"]
    results = run_eligibility_engine(sample_candidates, job_requirements)
    
    structured_output = generate_result_structure(job_id, results)

    # Print to console
    print("\nEligibility Result Structure\n")
    print(json.dumps(structured_output, indent=4))

    # Save to JSON file
    with open("eligibility_results.json", "w") as f:
        json.dump(structured_output, f, indent=4)