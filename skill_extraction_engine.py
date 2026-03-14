# -------------------------------
import json

# ✅ Master Skill Dictionary
MASTER_SKILLS = {
    "technical": [
        "python", "django", "sql", "aws", "rest api",
        "power bi", "excel", "html", "css", "javascript",
        "react", "mongodb", "express", "node",
        "autocad", "solidworks", "machine learning"
    ],
    "business": [
        "recruitment", "payroll management",
        "hr analytics", "leadership",
        "communication", "project management"
    ],
    "creative": [
        "graphic design", "content writing",
        "ui/ux design", "video editing"
    ]
}

# ✅ Skill Synonyms
SKILL_SYNONYMS = {
    "js": "javascript",
    "ml": "machine learning",
    "reactjs": "react"
}

# ✅ Skill Stacks
SKILL_STACKS = {
    "mern": ["mongodb", "express", "react", "node"],
    "mean": ["mongodb", "express", "angular", "node"]
}


def extract_skills_with_confidence(resume_text):
    text = resume_text.lower()
    extracted_skills = {}

    # 1️⃣ Direct Skill Matching
    for category, skills in MASTER_SKILLS.items():
        for skill in skills:
            count = text.count(skill)

            if count > 0:
                # ✅ Confidence Scoring Logic:
                # Base score = 0.8
                # +0.05 for each occurrence
                # Maximum score = 1.0
                confidence = min(0.8 + (0.05 * count), 1.0)

                extracted_skills[skill] = {
                    "category": category,
                    "confidence_score": round(confidence, 2)
                }

    # 2️⃣ Synonym Handling
    for synonym, original in SKILL_SYNONYMS.items():
        if synonym in text:
            extracted_skills[original] = {
                "category": "technical",
                "confidence_score": 0.85
            }

    # 3️⃣ Skill Stack Handling
    for stack, components in SKILL_STACKS.items():
        if stack in text:
            for comp in components:
                extracted_skills[comp] = {
                    "category": "technical",
                    "confidence_score": 0.9
                }

    return extracted_skills


# ✅ Example Test
if __name__ == "__main__":
    sample_resume = """
    Experienced Software Engineer skilled in Python, Django and ReactJS.
    Worked on MERN stack projects and deployed applications on AWS.
    Strong leadership and communication skills.
    """

    skills = extract_skills_with_confidence(sample_resume)

    print("\nExtracted Skills:\n")
    print(json.dumps(skills, indent=4))