import re
import json


# ----------------------------
# EDUCATION EXTRACTION
# ----------------------------
def extract_education(resume_text):
    education_list = []

    education_pattern = r"(B\.?Tech|M\.?Tech|B\.?Sc|M\.?Sc|MBA|BCA|MCA)\s*(in\s*(.*?))?\s*(from\s*(.*?))?\s*(\d{4})"

    matches = re.findall(education_pattern, resume_text, re.IGNORECASE)

    for index, match in enumerate(matches):
        degree = match[0]
        field = match[2] if match[2] else "Not Specified"
        institution = match[4] if match[4] else "Not Specified"
        graduation_year = match[5]

        education_object = {
            "education_id": f"EDU{index+1:03}",
            "degree_type": degree.upper(),
            "field_of_study": field.title(),
            "institution": institution.title(),
            "graduation_year": int(graduation_year)
        }

        education_list.append(education_object)

    return education_list


# ----------------------------
# CERTIFICATION EXTRACTION
# ----------------------------
def extract_certifications(resume_text):
    certifications = []

    certification_keywords = [
        "AWS Certified",
        "Azure Certified",
        "Google Cloud",
        "PMP",
        "Certified Data Analyst",
        "Cisco Certified",
        "Scrum Master"
    ]

    for keyword in certification_keywords:
        if keyword.lower() in resume_text.lower():
            certification_object = {
                "certification_name": keyword,
                "issuing_body": "Not Specified",
                "relevance_category": "Technical"
            }
            certifications.append(certification_object)

    return certifications


# ----------------------------
# STRUCTURED ACADEMIC PROFILE
# ----------------------------
def build_academic_profile(resume_text):
    education = extract_education(resume_text)
    certifications = extract_certifications(resume_text)

    total_degrees = len(education)
    total_certifications = len(certifications)

    if education:
        highest_degree = education[-1]["degree_type"]
    else:
        highest_degree = "Not Available"

    academic_profile = {
        "academic_summary": {
            "total_degrees": total_degrees,
            "highest_degree": highest_degree,
            "total_certifications": total_certifications
        },
        "education_details": education,
        "certification_details": certifications
    }

    return academic_profile
# ----------------------------
# EDUCATION RELEVANCE LOGIC
# ----------------------------
def calculate_education_relevance(resume_text, target_role):
    profile = build_academic_profile(resume_text)

    education = profile["education_details"]
    certifications = profile["certification_details"]

    relevance_score = 0
    max_score = 100

    target_role = target_role.lower()

    # Role based education relevance mapping
    role_education_map = {
        "backend developer": ["computer science", "information technology", "software engineering"],
        "data analyst": ["data science", "statistics", "computer science"],
        "hr manager": ["human resources", "business administration", "mba"]
    }

    # Check degree relevance
    for edu in education:
        field = edu["field_of_study"].lower()
        degree = edu["degree_type"].lower()

        if target_role in role_education_map:
            for valid_field in role_education_map[target_role]:
                if valid_field in field or valid_field in degree:
                    relevance_score += 30
                    break

    # Certification relevance
    for cert in certifications:
        if target_role in cert["certification_name"].lower():
            relevance_score += 20

    # Limit score to 100
    relevance_score = min(relevance_score, max_score)

    profile["education_relevance_score"] = relevance_score

    return profile


# ----------------------------
# TEST BLOCK
# ----------------------------
if __name__ == "__main__":
    sample_resume = """
    B.Tech in Computer Science from Calicut University 2021
    MBA in Finance from Anna University 2019
    AWS Certified Solutions Architect
    Certified Data Analyst
    """

    target_role = "Backend Developer"

    result = calculate_education_relevance(sample_resume, target_role)

    print("\nEducation Relevance Result:\n")
    print(json.dumps(result, indent=4))