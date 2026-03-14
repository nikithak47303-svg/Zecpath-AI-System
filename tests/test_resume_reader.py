from parser.resume_reader import extract_resume_text, clean_resume_text

file_path = "data/resumes_raw/resume.docx"

raw_text = extract_resume_text(file_path)
cleaned_text = clean_resume_text(raw_text)

# Save cleaned output
output_path = "data/resumes_cleaned/resume_cleaned.txt"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Cleaned resume saved successfully!")