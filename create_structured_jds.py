import json
from parser.jd_parser import parse_jd  # make sure your jd_parser has a parse_jd function

# Parse each JD file
jd1 = parse_jd("data/job_descriptions/jd1.txt")
jd2 = parse_jd("data/job_descriptions/jd2.txt")
jd3 = parse_jd("data/job_descriptions/jd3.txt")

# Wrap them in a list of job profiles
structured_jds = [
    {"job_profile": jd1},
    {"job_profile": jd2},
    {"job_profile": jd3}
]

# Save structured JSON
with open("data/structured_jds.json", "w") as f:
    json.dump(structured_jds, f, indent=4)

print("✅ structured_jds.json created successfully!")