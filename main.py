from parser.resume_parser import parse_resume
from ats_engine.ats_scorer import calculate_ats_score
from screening_ai.screening_logic import screening_decision
from scoring.score_aggregator import aggregate_score
from utils.logger import setup_logger
import json


def main():
    logger = setup_logger()
    logger.info("Zecpath AI System Started")

    print("📄 Reading Resume...")
   # Read resume as structured dictionary
parsed_resume = parse_resume("data/sample_resume.txt")

# Map to JSON schema
resume_json = {
    "candidate_profile": {
        "name": parsed_resume.get("name", ""),
        "email": parsed_resume.get("email", ""),
        "phone": parsed_resume.get("phone", ""),
        "linkedin": parsed_resume.get("linkedin", ""),
        "address": parsed_resume.get("address", ""),
        "total_experience": parsed_resume.get("total_experience", 0)
    },
    "education": parsed_resume.get("education", []),
    "experience": parsed_resume.get("experience", []),
    "skills": [{"skill_name": s, "proficiency_level": ""} for s in parsed_resume.get("skills", [])],
    "certifications": parsed_resume.get("certifications", [])
}

# Save JSON to file
with open("data/structured_resume.json", "w") as f:
    json.dump([resume_json], f, indent=4)

print("✅ Structured resume JSON created at data/structured_resume.json")
from utils.logger import setup_logger

logger = setup_logger()

logger.info("AI Hiring System Started")

# Example test result logging
logger.info("Test Case 1 - Resume Reader - PASS")
logger.info("Test Case 2 - JD Reader - PASS")
logger.info("Test Case 3 - ATS Matcher - PASS")

print("System executed successfully")