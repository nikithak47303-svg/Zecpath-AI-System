import json
import os
from candidate_score_generator import generate_candidate_score


# ==============================
# CONFIG
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RESUME_FOLDER = os.path.join(BASE_DIR, "data", "labeled")
MASTER_JOB_FILE = os.path.join(BASE_DIR, "data", "jobs", "auditor_roles_master.json")

SELECTED_JOB_ID = "AUD064"


# ==============================
# LOAD JOB FROM MASTER FILE
# ==============================

def get_job_from_master(job_id):
    with open(MASTER_JOB_FILE, "r") as f:
        jobs = json.load(f)

    for job in jobs:
        if job["job_id"] == job_id:
            return job

    return None


# ==============================
# AUTO RANKING FUNCTION
# ==============================

def auto_rank_candidates():

    results = []

    # 🔹 Load selected job
    selected_job = get_job_from_master(SELECTED_JOB_ID)

    if not selected_job:
        print("Invalid Job ID")
        return

    print(f"\n🔎 Ranking for Role: {selected_job['role']}\n")

    # 🔹 Loop through resumes
    for file in os.listdir(RESUME_FOLDER):

        resume_path = os.path.join(RESUME_FOLDER, file)

        if not os.path.isfile(resume_path):
            continue

        if file.endswith(".json"):

            with open(resume_path, "r") as f:
                resume_data = json.load(f)

            # If resume is list format
            if isinstance(resume_data, list):
                resume_data = resume_data[0]

            candidate_name = resume_data.get("name", "Unknown")

            # 🔹 Generate candidate score
            score = generate_candidate_score(
                resume_path,
                selected_job
            )

            results.append({
                "name": candidate_name,
                "score": score
            })

    # ==============================
    # SORT RESULTS
    # ==============================

    results.sort(key=lambda x: x["score"], reverse=True)

    # ==============================
    # SHORTLIST LOGIC
    # ==============================

    SHORTLIST_THRESHOLD = 40
    REVIEW_THRESHOLD = 30

    for candidate in results:
        score = candidate["score"]

        if score >= SHORTLIST_THRESHOLD:
            candidate["status"] = "Shortlisted"
        elif score >= REVIEW_THRESHOLD:
            candidate["status"] = "Under Review"
        else:
            candidate["status"] = "Rejected"

    # ==============================
    # PRINT OUTPUT
    # ==============================

    print("===== SHORTLISTING RESULTS =====\n")

    for i, candidate in enumerate(results, start=1):
        print(f"{i}. {candidate['name']} – {round(candidate['score'], 2)}% – {candidate['status']}")

    return results


# ==============================
# MAIN
# ==============================

if __name__ == "__main__":
    auto_rank_candidates()