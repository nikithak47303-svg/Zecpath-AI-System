# Optimized ATS Engine

## Overview

The ATS engine was optimized to improve performance, reduce processing time, and ensure stable execution when handling multiple resumes. The optimization focused on improving file handling, reducing redundant computations, and improving the overall ranking pipeline.

---

# Key Optimizations Implemented

## 1. Efficient Resume Processing

Previously, resumes were processed without checking file validity. The optimized system now:

* Skips non-JSON files
* Skips folders automatically
* Handles list-based resume structures safely

Example logic:

```python
for file in os.listdir(RESUME_FOLDER):

    resume_path = os.path.join(RESUME_FOLDER, file)

    if not os.path.isfile(resume_path):
        continue

    if file.endswith(".json"):
```

This ensures the system processes only valid resume files.

---

# 2. Single Job Loading Optimization

Previously, the job description could be loaded repeatedly.

Now the ATS loads the job **once** and reuses it for all resumes.

```python
selected_job = get_job_from_master(SELECTED_JOB_ID)
```

Benefits:

* Reduces disk reads
* Improves ranking speed
* Reduces memory usage

---

# 3. Faster Scoring Pipeline

The candidate scoring system was optimized by:

* Passing job data directly instead of repeatedly loading job files.
* Reducing unnecessary conversions.
* Using normalized data before scoring.

```python
score = generate_candidate_score(
    resume_path,
    selected_job
)
```

This reduces repeated I/O operations.

---

# 4. Improved Data Normalization

Normalization ensures consistent comparison between resumes and job descriptions.

Key improvements:

* Convert skills to lowercase
* Remove whitespace
* Convert experience to numeric values
* Handle multiple education formats

Example:

```python
normalized_skills.append(str(skill).strip().lower())
```

Benefits:

* More accurate scoring
* Reduced data inconsistency

---

# 5. Optimized Ranking Algorithm

Candidates are ranked using Python's efficient sorting algorithm.

```python
results.sort(key=lambda x: x["score"], reverse=True)
```

Benefits:

* Fast ranking even with large candidate lists
* O(n log n) performance

---

# 6. Smart Shortlisting Logic

Candidates are automatically classified using threshold-based filtering.

```python
if score >= SHORTLIST_THRESHOLD:
    candidate["status"] = "Shortlisted"
elif score >= REVIEW_THRESHOLD:
    candidate["status"] = "Under Review"
else:
    candidate["status"] = "Rejected"
```

Benefits:

* Automated decision support
* Faster recruiter workflow

---

# 7. Error Handling Improvements

The system now handles multiple runtime issues such as:

* Missing job IDs
* Invalid JSON formats
* Folder paths instead of files
* Missing resume fields

Example:

```python
if not selected_job:
    print("Invalid Job ID")
    return
```

This improves system reliability.

---

# Result

After optimization, the ATS engine now:

* Processes resumes faster
* Uses fewer system resources
* Handles noisy or inconsistent data better
* Provides stable ranking results

The system is now suitable for integration with backend services and scalable ATS pipelines.
