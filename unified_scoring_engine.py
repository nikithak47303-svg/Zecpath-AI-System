# ==========================================
# UNIFIED SCORING ENGINE (REFINED VERSION)
# ==========================================

import json
import os


# ------------------------------------------
# 1. CALCULATE UNIFIED SCORE (REFINED)
# ------------------------------------------

def calculate_unified_score(ats, screening, hr, confidence=0.9, role="default"):

    # 🔹 Role-based weight system
    weights = {
        "default": {"ats": 0.3, "screening": 0.4, "hr": 0.3},
        "technical": {"ats": 0.4, "screening": 0.4, "hr": 0.2},
        "managerial": {"ats": 0.2, "screening": 0.3, "hr": 0.5}
    }

    selected_weights = weights.get(role, weights["default"])

    # --------------------------------------
    # 🔹 INTELLIGENT ADJUSTMENTS
    # --------------------------------------

    # Penalize low confidence
    if confidence < 0.6:
        screening *= 0.8

    # Boost strong candidates
    if screening > 85 and hr > 80:
        screening += 2

    # Cap score to avoid overflow
    screening = min(screening, 100)

    # --------------------------------------
    # 🔹 FINAL SCORE
    # --------------------------------------

    final_score = (
        ats * selected_weights["ats"] +
        screening * selected_weights["screening"] +
        hr * selected_weights["hr"]
    )

    return round(final_score, 2), selected_weights


# ------------------------------------------
# 2. REFINED HIRING FIT CALCULATOR
# ------------------------------------------

def calculate_hiring_fit(score, confidence=0.9):

    if score >= 85 and confidence > 0.85:
        return "Strong Hire"

    elif score >= 70:
        return "Hire"

    elif score >= 55:
        return "Review"

    else:
        return "Reject"


# ------------------------------------------
# 3. GENERATE FINAL RESULT OBJECT
# ------------------------------------------

def generate_final_result(candidate_id, job_id, ats, screening, hr, confidence=0.9, role="default"):

    final_score, weights = calculate_unified_score(
        ats, screening, hr, confidence, role
    )

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

        "remarks": generate_remarks(final_score, confidence)
    }

    return result


# ------------------------------------------
# 4. GENERATE SMART REMARKS (NEW)
# ------------------------------------------

def generate_remarks(score, confidence):

    if score >= 85:
        return "Excellent candidate with strong overall performance."

    elif score >= 70:
        return "Good candidate with consistent performance across rounds."

    elif score >= 55:
        return "Average candidate. Needs further evaluation."

    else:
        return "Candidate does not meet hiring criteria."


# ------------------------------------------
# 5. SAVE FINAL RESULT TO JSON
# ------------------------------------------

def save_final_result(result):

    output_dir = os.path.join("data", "final")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, "unified_candidate_score.json")

    with open(output_path, "w") as f:
        json.dump(result, f, indent=4)

    print("\n✅ Final result saved to:", output_path)


# ------------------------------------------
# 6. MAIN EXECUTION (TEST)
# ------------------------------------------

if __name__ == "__main__":

    # 🔹 Sample inputs
    candidate_id = "CAND102"
    job_id = "AUD020"

    ats_score = 72
    screening_score = 80
    hr_score = 75
    confidence = 0.92

    # 🔹 Generate result
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

    print("\nRemarks:", final_result["remarks"])

    # 🔹 Save output
    save_final_result(final_result)