# semantic_matching_engine.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# -------------------------------------
# SEMANTIC MATCHING ENGINE
# -------------------------------------

def generate_embedding(text):
    return model.encode(text)


def calculate_similarity(resume_text, jd_text):
    resume_embedding = generate_embedding(resume_text)
    jd_embedding = generate_embedding(jd_text)

    similarity = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return round(float(similarity) * 100, 2)

# -------------------------------------
# SECTION-WISE SIMILARITY SCORER
# -------------------------------------

def section_similarity(resume_section, jd_section):
    if not resume_section or not jd_section:
        return 0.0

    resume_embedding = generate_embedding(resume_section)
    jd_embedding = generate_embedding(jd_section)

    similarity = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return float(similarity)


def calculate_detailed_match(resume_data, jd_data):

    skills_score = section_similarity(
        resume_data.get("skills", ""),
        jd_data.get("skills", "")
    )

    experience_score = section_similarity(
        resume_data.get("experience", ""),
        jd_data.get("experience", "")
    )

    projects_score = section_similarity(
        resume_data.get("projects", ""),
        jd_data.get("projects", "")
    )

    final_score = (
        skills_score * 0.4 +
        experience_score * 0.4 +
        projects_score * 0.2
    )

    return {
        "skills_similarity": round(skills_score * 100, 2),
        "experience_similarity": round(experience_score * 100, 2),
        "projects_similarity": round(projects_score * 100, 2),
        "final_match_score": round(final_score * 100, 2)
    }


# -------------------------------------
# TEST BLOCK
# -------------------------------------

if __name__ == "__main__":

    resume_data = {
        "skills": "Python, REST APIs, MySQL, AWS",
        "experience": "3 years backend development experience building scalable APIs",
        "projects": "Built cloud-based inventory management system"
    }

    jd_data = {
        "skills": "Looking for Python backend developer with API development skills",
        "experience": "Experience in backend system design and scalable applications",
        "projects": "Experience building cloud-based systems preferred"
    }

    result = calculate_detailed_match(resume_data, jd_data)

    print("\nDetailed Resume ↔ JD Similarity:\n")
    print(result)