# parsers/resume_parser.py

def parse_resume(file_path):
    parsed = {
        "name": "",
        "email": "",
        "phone": "",
        "linkedin": "",
        "address": "",
        "total_experience": 0,
        "education": [],
        "experience": [],
        "skills": [],
        "certifications": []
    }
    
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        if line.startswith("Name:"):
            parsed["name"] = line.replace("Name:", "").strip()
        elif line.startswith("Skills:"):
            skills = line.replace("Skills:", "").strip().split(",")
            parsed["skills"] = [s.strip() for s in skills]
        elif line.startswith("Experience:"):
            exp_text = line.replace("Experience:", "").strip()
            parsed["total_experience"] = int(exp_text.split()[0])
        elif line.startswith("Education:"):
            edu_text = line.replace("Education:", "").strip()
            parsed["education"] = [{"degree": edu_text, "specialization": "", "institute": "", "year": ""}]
    
    return parsed