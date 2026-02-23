import re
import json


def extract_experience(resume_text):
    experiences = []

    # Simple pattern: Designation at Company from Year to Year
    pattern = r"(.*?) at (.*?) from (\d{4}) to (\d{4})"

    matches = re.findall(pattern, resume_text)

    for match in matches:
        designation, company, start_year, end_year = match

        experience_object = {
            "designation": designation.strip(),
            "company": company.strip(),
            "start_year": start_year,
            "end_year": end_year,
            "description": "Not Provided"
        }

        experiences.append(experience_object)

    return experiences


# ✅ Example Test
if __name__ == "__main__":
    sample_resume = """
    Software Engineer at Infosys from 2022 to 2024
    Data Analyst at TCS from 2020 to 2022
    """

    result = extract_experience(sample_resume)

    print("\nStructured Experience Object:\n")
    print(json.dumps(result, indent=4))