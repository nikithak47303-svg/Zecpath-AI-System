import json

with open("data/hr/hr_screening_questions.json", "r") as f:
    data = json.load(f)

print("Loaded successfully!\n")

for q in data["questions"]:
    print(q["question"])