from parser.jd_parser import parse_jd
import os
import json

jd_folder = "data/job_descriptions/"
structured_jds = []

for file in os.listdir(jd_folder):
    if file.endswith(".txt"):
        file_path = os.path.join(jd_folder, file)
        parsed_jd = parse_jd(file_path)
        structured_jds.append(parsed_jd)

# Save all structured JDs in one JSON
with open("data/structured_jds.json", "w") as f:
    json.dump(structured_jds, f, indent=4)

print("✅ All job descriptions structured and saved in data/structured_jds.json")