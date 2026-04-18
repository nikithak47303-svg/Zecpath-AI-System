import re

# ==============================
# SAFE CLEANING FUNCTION
# ==============================

def clean_answer(answer):
    if not answer or len(answer.strip()) == 0:
        return "no valid response"
    return answer.strip().lower()


def safe_process_answer(answer):
    try:
        return clean_answer(answer)
    except Exception:
        return "processing error"


# ==============================
# CONFIDENCE NORMALIZATION
# ==============================

def normalize_confidence(score):
    if score < 0.5:
        return 0.5
    elif score > 0.95:
        return 0.95
    return round(score, 2)


# ==============================
# KEYWORD DEFINITIONS
# ==============================

SKILL_KEYWORDS = ["python", "java", "excel", "sql", "audit", "finance"]

EXPERIENCE_KEYWORDS = ["year", "years", "experience"]

AVAILABILITY_KEYWORDS = [
    "immediately", "notice period", "available",
    "join", "joining", "month", "weeks"
]

SALARY_KEYWORDS = ["salary", "ctc", "lpa", "expected"]


# ==============================
# ADVANCED INTENT CLASSIFIER
# ==============================

def classify_intent(answer):

    scores = {
        "experience": 0,
        "skill": 0,
        "availability": 0,
        "salary": 0
    }

    for word in EXPERIENCE_KEYWORDS:
        if word in answer:
            scores["experience"] += 2

    for word in SKILL_KEYWORDS:
        if word in answer:
            scores["skill"] += 1

    for word in AVAILABILITY_KEYWORDS:
        if word in answer:
            scores["availability"] += 1

    for word in SALARY_KEYWORDS:
        if word in answer:
            scores["salary"] += 1

    best_intent = max(scores, key=scores.get)

    if scores[best_intent] == 0:
        return "general"

    return best_intent


# ==============================
# SKILL EXTRACTION
# ==============================

def extract_skills(answer):

    return [skill for skill in SKILL_KEYWORDS if skill in answer]


# ==============================
# EXPERIENCE EXTRACTION
# ==============================

def extract_experience(answer):

    match = re.search(r'(\d+)\s*(year|years)', answer)

    if match:
        return int(match.group(1))

    return 0


# ==============================
# QUALITY CHECKS
# ==============================

def is_off_topic(answer):
    return len(answer.split()) < 3


def is_vague(answer):
    vague_words = ["maybe", "not sure", "don't know", "some"]
    return any(word in answer for word in vague_words)


# ==============================
# FOLLOW-UP LOGIC
# ==============================

def should_ask_followup(answer):
    return len(answer.split()) < 3


# ==============================
# MAIN UNDERSTANDING FUNCTION
# ==============================

def understand_answer(answer):

    answer = safe_process_answer(answer)

    return {
        "cleaned_answer": answer,
        "intent": classify_intent(answer),
        "skills": extract_skills(answer),
        "experience_years": extract_experience(answer),
        "is_off_topic": is_off_topic(answer),
        "is_vague": is_vague(answer),
        "needs_followup": should_ask_followup(answer)
    }


# ==============================
# CONFIDENCE CALCULATION (NEW)
# ==============================

def calculate_confidence(analysis):

    score = 0.9

    if analysis["is_off_topic"]:
        score -= 0.3

    if analysis["is_vague"]:
        score -= 0.2

    if analysis["experience_years"] > 0:
        score += 0.05

    return normalize_confidence(score)


# ==============================
# STRUCTURED ANSWER FORMAT
# ==============================

def build_structured_answer(answer):

    analysis = understand_answer(answer)
    confidence = calculate_confidence(analysis)

    structured = {
        "intent": analysis["intent"],

        "key_data": {
            "skills": analysis["skills"],
            "experience_years": analysis["experience_years"]
        },

        "quality": {
            "is_off_topic": analysis["is_off_topic"],
            "is_vague": analysis["is_vague"],
            "needs_followup": analysis["needs_followup"]
        },

        "confidence_score": confidence,

        "final_status": "valid"
    }

    # 🔹 Decision logic
    if analysis["is_off_topic"]:
        structured["final_status"] = "reject"

    elif analysis["is_vague"]:
        structured["final_status"] = "review"

    return structured


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":

    sample_answers = [
        "I have 2 years of experience in audit and excel",
        "I know python and sql",
        "Maybe I can join after one month",
        "yes",
        "",
        "My expected salary is 5 LPA"
    ]

    for ans in sample_answers:
        result = build_structured_answer(ans)

        print("\nAnswer:", ans)
        print("Structured Output:", result)