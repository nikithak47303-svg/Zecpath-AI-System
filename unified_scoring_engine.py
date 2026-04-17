# ==========================================
# UNIFIED SCORING ENGINE
# ==========================================

import json
import os


# ------------------------------------------
# 1. CALCULATE UNIFIED SCORE
# ------------------------------------------

def calculate_unified_score(ats_score, screening_score, hr_score, role="default"):

    # 🔹 Role-based weight system
    weights = {
        "default": {
            "ats": 0.3,
            "screening": 0.4,
            "hr": 0.3
        },
        "technical": {
            "ats": 0.4,
            "screening": 0.4,
            "hr": 0.2
        },
        "managerial": {
            "ats": 0.2,
            "screening": 0.3,
            "hr": 0.5
        }
    }

    selected_weights = weights.get(role, weights["default"])

    final_score = (
        ats_score * selected_weights["ats"] +
        screening_score * selected_weights["screening"] +
        hr_score * selected_weights["hr"]
    )

    return round(final_score, 2), selected_weights


# ------------------------------------------
# 2. HIRING FIT CALCULATOR
# ------------------------------------------

def calculate_hiring_fit(score, confidence=0.9):

    if score >= 80 and confidence > 0.8:
        return "Strong Hire"

    elif score >= 65:
        return "Hire"

    elif score >= 50:
        return "Borderline"

    else:
        return "Reject"


# ------------------------------------------
# 3. GENERATE FINAL RESULT OBJECT
# ------------------------------------------

def generate_final_result(candidate_id, job_id, ats, screening, hr, confidence=0.9, role="default"):

    final_score, weights = calculate_unified_score(ats, screening, hr, role)
    decision = calculate_hiring_fit(final_score, confidence)

    result = {
        "candidate_id": candidate_id,
        "job_id": job_id,

        "scores": {
            "ats_score": ats,
            "ai_screening_score": screening,
            "hr_interview_score": hr
        },

        "weights": weights,

        "final_score": final_score,
        "confidence": confidence,
        "hiring_decision": decision,

        "remarks": "Auto-generated hiring decision based on multi-stage evaluation."
    }

    return result


# ------------------------------------------
# 4. SAVE FINAL RESULT TO JSON (STEP 4)
# ------------------------------------------

def save_final_result(result):

    output_dir = os.path.join("data", "final")

    # Create folder if not exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, "unified_candidate_score.json")

    with open(output_path, "w") as f:
        json.dump(result, f, indent=4)

    print("\n✅ Final result saved to:", output_path)


# ------------------------------------------
# 5. MAIN EXECUTION (TEST RUN)
# ------------------------------------------

if __name__ == "__main__":

    # 🔹 Sample inputs (replace later with real pipeline data)
    candidate_id = "CAND102"
    job_id = "AUD020"

    ats_score = 72
    screening_score = 80
    hr_score = 75
    confidence = 0.92

    # 🔹 Generate final result
    final_result = generate_final_result(
        candidate_id,
        job_id,
        ats_score,
        screening_score,
        hr_score,
        confidence
    )

    # 🔹 Print output
    print("\n===== FINAL HIRING RESULT =====\n")

    print("Candidate ID:", final_result["candidate_id"])
    print("Job ID:", final_result["job_id"])

    print("\nScores:")
    print("ATS:", final_result["scores"]["ats_score"])
    print("Screening:", final_result["scores"]["ai_screening_score"])
    print("HR:", final_result["scores"]["hr_interview_score"])

    print("\nFinal Score:", final_result["final_score"])
    print("Confidence:", final_result["confidence"])
    print("Decision:", final_result["hiring_decision"])

    # 🔹 SAVE TO FILE (IMPORTANT STEP)
    save_final_result(final_result)