from screening_scoring_engine import evaluate_candidate, final_decision
from behavioral_analysis import analyze_candidate_behavior
from answer_understanding_engine import build_structured_answer


# ==============================
# EXTRACT KEY INFORMATION
# ==============================

def extract_key_info(answers):

    skills = set()
    experience = 0
    salary = None
    availability = None

    for ans in answers:
        data = build_structured_answer(ans)

        for skill in data["key_data"]["skills"]:
            skills.add(skill)

        if data["key_data"]["experience_years"] > experience:
            experience = data["key_data"]["experience_years"]

        if data["intent"] == "salary":
            salary = ans

        if data["intent"] == "availability":
            availability = ans

    return {
        "skills": list(skills),
        "experience_years": experience,
        "salary_expectation": salary,
        "availability": availability
    }


# ==============================
# GENERATE REPORT
# ==============================

def generate_screening_report(answers):

    evaluation = evaluate_candidate(answers)
    decision = final_decision(evaluation)
    behavior = analyze_candidate_behavior(answers)
    key_info = extract_key_info(answers)

    summary = f"Candidate scored {evaluation['overall_score']} with a {decision['decision']} status."

    strengths = []
    risks = []

    if evaluation["overall_score"] >= 7:
        strengths.append("Strong technical responses")

    if behavior["final_behavior_label"] == "Strong Candidate":
        strengths.append("Confident communication")

    if evaluation["overall_score"] < 5:
        risks.append("Low answer quality")

    if behavior["final_behavior_label"] == "Weak Candidate":
        risks.append("Poor communication or confidence")

    return {
        "summary": summary,
        "overall_score": evaluation["overall_score"],
        "decision": decision["decision"],
        "behavior_label": behavior["final_behavior_label"],
        "key_information": key_info,
        "strengths": strengths,
        "risks": risks
    }


# ==============================
# FORMAT REPORT FOR RECRUITERS
# ==============================

def format_report(report):

    formatted = f"""
========================================
        AI SCREENING REPORT
========================================

SUMMARY:
{report['summary']}

----------------------------------------
OVERALL EVALUATION
----------------------------------------
Score: {report['overall_score']}
Decision: {report['decision']}
Behavior: {report['behavior_label']}

----------------------------------------
KEY INFORMATION
----------------------------------------
Skills: {', '.join(report['key_information']['skills'])}
Experience: {report['key_information']['experience_years']} years
Salary Expectation: {report['key_information']['salary_expectation']}
Availability: {report['key_information']['availability']}

----------------------------------------
STRENGTHS
----------------------------------------
{chr(10).join(['- ' + s for s in report['strengths']]) if report['strengths'] else "None"}

----------------------------------------
RISKS
----------------------------------------
{chr(10).join(['- ' + r for r in report['risks']]) if report['risks'] else "None"}

========================================
"""

    return formatted


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":

    sample_answers = [
        "I have 2 years of experience in audit and excel",
        "I know python and sql",
        "Maybe I can join after one month",
        "My expected salary is 5 LPA",
        "I am confident and ready to work"
    ]

    report = generate_screening_report(sample_answers)

    formatted = format_report(report)

    print(formatted)