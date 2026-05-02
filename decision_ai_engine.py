# ==========================================
# DECISION AI ENGINE
# ==========================================


# ------------------------------------------
# CALCULATE CONFIDENCE SCORE
# ------------------------------------------

def calculate_confidence(final_score, behavior_score, integrity_risk):

    confidence = (
        final_score * 0.6 +
        behavior_score * 0.3 +
        (100 - integrity_risk) * 0.1
    )

    return round(confidence, 2)


# ------------------------------------------
# DECISION LOGIC
# ------------------------------------------

def generate_decision(final_score, confidence, integrity_risk):

    # High integrity risk overrides score
    if integrity_risk >= 70:
        return "Rejected"

    if final_score >= 85 and confidence >= 80:
        return "Selected"

    elif final_score >= 65:
        return "Hold / Review"

    else:
        return "Rejected"


# ------------------------------------------
# MAIN ENGINE
# ------------------------------------------

def decision_ai_engine(
    candidate_id,
    job_id,
    final_score,
    behavior_score,
    integrity_risk
):

    confidence = calculate_confidence(
        final_score,
        behavior_score,
        integrity_risk
    )

    decision = generate_decision(
        final_score,
        confidence,
        integrity_risk
    )

    return {
        "candidate_id": candidate_id,
        "job_id": job_id,

        "scores": {
            "final_score": final_score,
            "behavior_score": behavior_score,
            "integrity_risk": integrity_risk
        },

        "confidence_score": confidence,
        "final_decision": decision,

        "explanation": "Decision generated using hybrid score + rule-based logic."
    }


# ------------------------------------------
# TEST RUN
# ------------------------------------------

if __name__ == "__main__":

    result = decision_ai_engine(
        candidate_id="CAND801",
        job_id="DEV301",
        final_score=82,
        behavior_score=78,
        integrity_risk=20
    )

    print("\n===== FINAL DECISION RESULT =====\n")

    print("Candidate ID:", result["candidate_id"])
    print("Decision:", result["final_decision"])
    print("Confidence:", result["confidence_score"])

    print("\nFull Output:\n", result)