import json
import os
from clean_transcript_processor import process_transcript


# ==============================
# PATH CONFIG
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FILE = os.path.join(BASE_DIR, "data", "transcripts", "sample_transcript.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "transcripts", "normalized_transcript.json")


# ==============================
# NORMALIZATION FUNCTION
# ==============================

def normalize_transcript():

    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    # ✅ FIX: Handle both dict and list
    if isinstance(data, dict):
        data = [data]

    normalized_data = []

    for entry in data:

        # Safety check (skip invalid entries)
        if not isinstance(entry, dict):
            continue

        raw_text = entry.get("answer", "")

        # 🔹 Clean text
        cleaned_text = process_transcript(raw_text)

        normalized_entry = {
            "candidate_id": entry.get("candidate_id", "UNKNOWN"),
            "job_id": entry.get("job_id", "UNKNOWN"),
            "question_id": entry.get("question_id", "UNKNOWN"),
            "timestamp": entry.get("timestamp", ""),
            "cleaned_answer": cleaned_text
        }

        normalized_data.append(normalized_entry)

    # ==============================
    # SAVE OUTPUT
    # ==============================

    with open(OUTPUT_FILE, "w") as f:
        json.dump(normalized_data, f, indent=4)

    print("✅ Normalized transcript saved successfully!")


# ==============================
# RUN
# ==============================

if __name__ == "__main__":
    normalize_transcript()