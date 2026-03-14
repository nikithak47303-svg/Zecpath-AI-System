import json

# Load structured resumes
with open("data/structured_resume.json", "r") as f:
    resumes = json.load(f)

# Load structured job descriptions
with open("data/structured_jds.json", "r") as f:
    jobs = json.load(f)

# Combine into one JSON
combined_data = {
    "candidates": resumes,
    "jobs": jobs
}

# Save combined data
with open("data/combined_data.json", "w") as f:
    json.dump(combined_data, f, indent=4)

print("✅ Combined data saved in data/combined_data.json")