def calculate_ats_score(resume_text):
    keywords = ["Python", "FastAPI", "React", "Node.js"]

    score = 0
    for word in keywords:
        if word.lower() in resume_text.lower():
            score += 25

    return score
