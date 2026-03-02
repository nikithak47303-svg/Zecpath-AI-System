import os
import json
from candidate_score_generator import generate_candidate_score

JOB_FILE = "data/jobs/software_engineer.json"
RESUME_FOLDER = "data/labeled"


def auto_rank_candidates():

    results = []

    for file in os.listdir(RESUME_FOLDER):

        resume_path = os.path.join(RESUME_FOLDER, file)

        # Skip folders
        if not os.path.isfile(resume_path):
            continue

        if file.endswith(".json"):

            with open(resume_path, "r") as f:
                resume_data = json.load(f)

            # Handle list-based JSON
            if isinstance(resume_data, list):
                resume_data = resume_data[0]

            candidate_name = resume_data.get("name", "Unknown")

            score = generate_candidate_score(
                resume_path,
                JOB_FILE,
                semantic_score=80
            )

            results.append({
                "name": candidate_name,
                "score": score
            })

    # ===== SORT =====
    results.sort(key=lambda x: x["score"], reverse=True)

    # ===== SHORTLIST LOGIC =====
    SHORTLIST_THRESHOLD = 70
    REVIEW_THRESHOLD = 50

    for candidate in results:
        score = candidate["score"]

        if score >= SHORTLIST_THRESHOLD:
            candidate["status"] = "Shortlisted"
        elif score >= REVIEW_THRESHOLD:
            candidate["status"] = "Under Review"
        else:
            candidate["status"] = "Rejected"

    # ===== PRINT OUTPUT =====
    print("\n===== SHORTLISTING RESULTS =====\n")

    for i, candidate in enumerate(results, start=1):
        print(f"{i}. {candidate['name']} – {round(candidate['score'],2)}% – {candidate['status']}")

    return results


if __name__ == "__main__":
    auto_rank_candidates()