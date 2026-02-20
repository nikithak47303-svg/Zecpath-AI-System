import json
from parser.resume_parser import parse_resume

# Parse the resume text
resume_text = parse_resume("data/sample_resume.txt")

# Convert it into structured JSON
structured_resume = [
    {
        "candidate_profile": {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "1234567890",
            "linkedin": "linkedin.com/in/johndoe",
            "address": "Bangalore, India",
            "total_experience": 3,
            "education": [
                {"degree": "B.Tech", "specialization": "Computer Science", "institute": "XYZ University", "year": "2020"}
            ],
            "experience": [
                {"company_name": "ABC Corp", "designation": "Software Engineer", "start_date": "2020-06", "end_date": "2023-01", "location": "Bangalore", "description": "Worked on web development projects"}
            ],
            "skills": [
                {"skill_name": "Python", "proficiency_level": "Advanced"},
                {"skill_name": "React", "proficiency_level": "Intermediate"}
            ],
            "certifications": ["AWS Certified Developer"]
        }
    }
]

# Save as JSON
with open("data/structured_resume.json", "w") as f:
    json.dump(structured_resume, f, indent=4)

print("✅ structured_resume.json created successfully!")