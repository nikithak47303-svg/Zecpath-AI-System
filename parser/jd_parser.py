def parse_jd(file_path):
    """
    Parse a job description text file into a structured dictionary.
    """
    parsed = {
        "job_title": "",
        "department": "",
        "skills_required": [],
        "experience_required": 0,
        "education_required": "",
        "certifications_required": [],
        "location": "",
        "job_type": ""
    }
    
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        if line.startswith("Job Title:"):
            parsed["job_title"] = line.replace("Job Title:", "").strip()
        elif line.startswith("Department:"):
            parsed["department"] = line.replace("Department:", "").strip()
        elif line.startswith("Skills:"):
            skills = line.replace("Skills:", "").strip().split(",")
            parsed["skills_required"] = [s.strip() for s in skills]
        elif line.startswith("Experience:"):
            exp_text = line.replace("Experience:", "").strip()
            parsed["experience_required"] = int(exp_text.split()[0])
        elif line.startswith("Education:"):
            parsed["education_required"] = line.replace("Education:", "").strip()
        elif line.startswith("Certifications:"):
            certs = line.replace("Certifications:", "").strip().split(",")
            parsed["certifications_required"] = [c.strip() for c in certs if c.strip().lower() != "none"]
        elif line.startswith("Location:"):
            parsed["location"] = line.replace("Location:", "").strip()
        elif line.startswith("Job Type:"):
            parsed["job_type"] = line.replace("Job Type:", "").strip()
    
    return parsed