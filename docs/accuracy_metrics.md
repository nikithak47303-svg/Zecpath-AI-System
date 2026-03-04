# ATS Accuracy Metrics Report
## Day 17 – Deliverable 2

---

# 1. Objective

The objective of this document is to evaluate the quantitative performance of the ATS system using:

- Accuracy
- Precision
- Recall
- Mismatch analysis

The evaluation compares AI shortlisting decisions with manual HR review decisions.

---

# 2. Testing Dataset

Total Resumes Tested: 20  
Roles Covered:
- Technical Roles
- Non-Technical Roles
- Fresher Profiles
- Senior Profiles

Manual HR decision was treated as the ground truth.

---

# 3. Confusion Matrix (Shortlisted vs Not Shortlisted)

For evaluation, we simplified classification:

Positive = Shortlisted  
Negative = Not Shortlisted (Under Review + Rejected)

|                      | Manual Shortlisted | Manual Not Shortlisted |
|----------------------|-------------------|------------------------|
| AI Shortlisted       | 8 (True Positive) | 1 (False Positive)     |
| AI Not Shortlisted   | 2 (False Negative)| 9 (True Negative)      |

Where:

TP = 8  
FP = 1  
FN = 2  
TN = 9  

Total = 20

---

# 4. Accuracy Calculation

Accuracy measures overall correctness.

Formula:

Accuracy = (TP + TN) / Total

= (8 + 9) / 20  
= 17 / 20  
= 85%

Accuracy = 85%

---

# 5. Precision Calculation

Precision measures how many AI shortlisted candidates were actually correct.

Formula:

Precision = TP / (TP + FP)

= 8 / (8 + 1)  
= 8 / 9  
= 88.8%

Precision ≈ 89%

Interpretation:
When the AI shortlists a candidate, it is correct 89% of the time.

---

# 6. Recall Calculation

Recall measures how many truly good candidates the AI successfully identified.

Formula:

Recall = TP / (TP + FN)

= 8 / (8 + 2)  
= 8 / 10  
= 80%

Recall = 80%

Interpretation:
The AI successfully identifies 80% of genuinely suitable candidates.

---

# 7. F1 Score

F1 Score balances Precision and Recall.

Formula:

F1 = 2 × (Precision × Recall) / (Precision + Recall)

= 2 × (0.89 × 0.80) / (0.89 + 0.80)  
= 0.84 (approx)

F1 Score ≈ 84%

---

# 8. Category-Wise Performance

## 8.1 Technical Roles

Accuracy: 90%  
Observation:
- Strong performance due to clear skill keyword matching.
- Certifications positively influenced score.

---

## 8.2 Non-Technical Roles

Accuracy: 80%  
Observation:
- Minor mismatches in roles involving soft skills.
- Experience weighting affected borderline cases.

---

## 8.3 Fresher Profiles

Accuracy: 85%  
Observation:
- System handled entry-level JDs correctly.
- Experience score did not heavily penalize freshers when JD required 0 years.

---

## 8.4 Senior Profiles

Accuracy: 80%  
Observation:
- Senior domain expertise sometimes under-scored if keywords did not exactly match JD terms.

---

# 9. Mismatch Analysis

## False Positive Case (1)

AI Shortlisted but Manual Rejected:
- Candidate had matching keywords but lacked depth of domain experience.
- Indicates need for contextual semantic analysis.

## False Negative Cases (2)

Manual Shortlisted but AI Under Review:
- Senior profile with broad experience but limited keyword overlap.
- Suggests improvement needed in synonym detection and domain mapping.

---

# 10. Overall Performance Summary

Metric Summary:

Accuracy: 85%  
Precision: 89%  
Recall: 80%  
F1 Score: 84%

The ATS system demonstrates strong precision and reliable decision-making, with room for improvement in recall and semantic intelligence.

---

# 11. Conclusion

The ATS AI system provides high reliability in structured resume evaluation with:

- Strong precision in shortlisting decisions
- Acceptable recall across role types
- Balanced F1 performance

Future improvements can enhance semantic matching and contextual experience evaluation to further increase recall and reduce mismatch cases.

---