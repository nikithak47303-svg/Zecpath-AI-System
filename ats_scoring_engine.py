import json

with open("config/role_weights.json", "r") as f:
    ROLE_WEIGHTS = json.load(f)
def calculate_ats_score(role, skill_score, exp_score, edu_score, semantic_score):

    weights = ROLE_WEIGHTS.get(role)

    final_score = (
        skill_score * weights["skill"] +
        exp_score * weights["experience"] +
        edu_score * weights["education"] +
        semantic_score * weights["semantic"]
    )

    return round(final_score, 2)
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

    if final_score >= 80:
        print("Decision: Strong Match")
    elif final_score >= 60:
        print("Decision: Moderate Match")
    else:
        print("Decision: Weak Match")
        # STEP 5 – Test the ATS Engine
if __name__ == "__main__":
    generate_candidate_report(
        name="Rahul Sharma",
        role="software_engineer",
        skill=85,
        exp=78,
        edu=90,
        semantic=80
    )