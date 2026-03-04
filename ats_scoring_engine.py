import json


# ==============================
# LOAD ROLE WEIGHTS
# ==============================

with open("config/role_weights.json", "r") as f:
    ROLE_WEIGHTS = json.load(f)


# ==============================
# VALIDATE WEIGHTS
# ==============================

def validate_weights(weights):
    """
    Ensure weights exist and sum to 1.
    Prevents biased scoring.
    """

    required_keys = ["skill", "experience", "education", "semantic"]

    # If missing keys, return default balanced weights
    for key in required_keys:
        if key not in weights:
            return {
                "skill": 0.4,
                "experience": 0.2,
                "education": 0.2,
                "semantic": 0.2
            }

    total = sum(weights.values())

    # Normalize automatically if not equal to 1
    if total != 1:
        weights = {k: v / total for k, v in weights.items()}

    return weights


# ==============================
# ATS SCORE CALCULATION
# ==============================

def calculate_ats_score(role, skill_score, exp_score, edu_score, semantic_score):

    # Get weights safely
    weights = ROLE_WEIGHTS.get(role)

    if not weights:
        # Default balanced weights (bias-safe fallback)
        weights = {
            "skill": 0.4,
            "experience": 0.2,
            "education": 0.2,
            "semantic": 0.2
        }

    weights = validate_weights(weights)

    # Ensure scores are within 0–100
    skill_score = min(max(skill_score, 0), 100)
    exp_score = min(max(exp_score, 0), 100)
    edu_score = min(max(edu_score, 0), 100)
    semantic_score = min(max(semantic_score, 0), 100)

    final_score = (
        skill_score * weights["skill"] +
        exp_score * weights["experience"] +
        edu_score * weights["education"] +
        semantic_score * weights["semantic"]
    )

    return round(final_score, 2)


# ==============================
# CANDIDATE REPORT
# ==============================

def generate_candidate_report(name, role, skill, exp, edu, semantic):

    final_score = calculate_ats_score(role, skill, exp, edu, semantic)

    print("\n----- ATS Score Report -----")
    print(f"Candidate: {name}")
    print(f"Role Applied: {role}")
    print(f"Skill Score: {skill}")
    print(f"Experience Score: {exp}")
    print(f"Education Score: {edu}")
    print(f"Semantic Score: {semantic}")
    print(f"\nFinal ATS Score: {final_score}%")

    # Fair threshold decisions
    if final_score >= 80:
        print("Decision: Strong Match")
    elif final_score >= 60:
        print("Decision: Moderate Match")
    else:
        print("Decision: Weak Match")

# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":
    generate_candidate_report(
        name="Rahul Sharma",
        role="software_engineer",
        skill=85,
        exp=78,
        edu=90,
        semantic=80
    )