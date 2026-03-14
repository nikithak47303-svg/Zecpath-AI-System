# Zecpath AI Hiring System – Test Result Log

## Test Case 1 – Resume Reader

- Module: parsers/resume_reader.py
- Test Description: Extract skills from sample resume
- Input: sample_resume.txt
- Expected Output: List of skills
- Actual Output: Skills extracted successfully
- Status: PASS
- Date: 20-02-2026

---

## Test Case 2 – JD Reader

- Module: parsers/jd_reader.py
- Test Description: Extract required skills from JD
- Input: sample_jd.txt
- Expected Output: Required skills list
- Actual Output: Extracted correctly
- Status: PASS
- Date: 20-02-2026

---

## Test Case 3 – ATS Matcher

- Module: ats_engine/ats_matcher.py
- Test Description: Match resume skills with JD skills
- Input: Resume skills + JD skills
- Expected Output: Matching percentage
- Actual Output: 75% match
- Status: PASS
- Date: 20-02-2026