from answer_understanding_engine import build_structured_answer


# ==============================
# SCORING PARAMETERS (0–10 each)
# ==============================

def score_clarity(answer_obj):

    if answer_obj["quality"]["is_off_topic"]:
        return 0

    if answer_obj["quality"]["is_vague"]:
        return 4

    return 8


def score_relevance(answer_obj):

    intent = answer_obj["intent"]

    if intent == "general":
        return 3

    return 8


def score_completeness(answer_obj):

    skills = answer_obj["key_data"]["skills"]
    exp = answer_obj["key_data"]["experience_years"]

    if skills or exp > 0:
        return 8

    return 4


def score_consistency(answer_obj):

    if answer_obj["quality"]["is_vague"]:
        return 5

    return 8


# ==============================
# TOTAL SCORE FOR ONE ANSWER
# ==============================

def score_answer(answer):

    structured = build_structured_answer(answer)

    clarity = score_clarity(structured)
    relevance = score_relevance(structured)
    completeness = score_completeness(structured)
    consistency = score_consistency(structured)

    total = (clarity + relevance + completeness + consistency) / 4

    return {
        "answer": answer,
        "intent": structured["intent"],
        "status": structured["final_status"],
        "scores": {
            "clarity": clarity,
            "relevance": relevance,
            "completeness": completeness,
            "consistency": consistency
        },
        "final_score": round(total, 2)
    }


# ==============================
# AGGREGATE MULTIPLE ANSWERS
# ==============================

def evaluate_candidate(answers):

    results = []
    total_score = 0

    for ans in answers:
        result = score_answer(ans)
        results.append(result)
        total_score += result["final_score"]

    avg_score = total_score / len(answers)

    return {
        "per_answer_scores": results,
        "overall_score": round(avg_score, 2)
    }


# ==============================
# FINAL DECISION ENGINE
# ==============================

def final_decision(result):

    score = result["overall_score"]

    if score >= 7.5:
        decision = "Shortlisted"

    elif score >= 5:
        decision = "Review"

    else:
        decision = "Rejected"

    return {
        "overall_score": score,
        "decision": decision
    }


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":

    sample_answers = [
        "I have 2 years of experience in audit and excel",
        "I know python and sql",
        "Maybe I can join after one month",
        "yes",
        "My expected salary is 5 LPA"
    ]

    # Step 1: Evaluate answers
    evaluation = evaluate_candidate(sample_answers)

    # Step 2: Final decision
    decision = final_decision(evaluation)

    print("\nPer Answer Breakdown:\n")
    print(evaluation)

    print("\nFinal Decision:\n")
    print(decision)