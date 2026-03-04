# ATS Input & Output Schemas
## Day 16 – Deliverable 2

---

# 1. Overview

This document defines the structured JSON schemas used in the ATS AI system for:

- Resume Upload
- Resume Parsing
- Candidate Scoring
- Shortlisting & Ranking
- Job Description Structure

These schemas act as formal contracts between backend systems and the ATS AI service.

---

# 2. Resume Upload Schema

## 2.1 Upload Request (Multipart Form)

| Field         | Type   | Required | Description |
|--------------|--------|----------|-------------|
| file         | file   | Yes      | Resume file (PDF/DOCX) |
| candidate_id | string | Yes      | Unique candidate identifier |

---

## 2.2 Upload Response Schema

```json
{
  "status": "string",
  "resume_id": "string",
  "message": "string"
}
```

### Example

```json
{
  "status": "success",
  "resume_id": "RES12345",
  "message": "Resume uploaded successfully"
}
```

---

# 3. Structured Resume Schema

This schema represents parsed resume data used by the scoring engine.

```json
{
  "resume_id": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "skills": ["string"],
  "experience_years": "number",
  "education": ["string"],
  "certifications": ["string"],
  "previous_roles": ["string"]
}
```

### Field Definitions

| Field              | Type      | Description |
|-------------------|----------|-------------|
| resume_id         | string   | Unique resume identifier |
| name              | string   | Candidate full name |
| email             | string   | Candidate email |
| phone             | string   | Candidate phone number |
| skills            | array    | Extracted technical and domain skills |
| experience_years  | number   | Total years of experience |
| education         | array    | Academic qualifications |
| certifications    | array    | Professional certifications |
| previous_roles    | array    | Past job titles |

---

# 4. Job Description Schema

This schema defines structured job data stored in the master job file.

```json
{
  "job_id": "string",
  "role": "string",
  "domain": "string",
  "category": "string",
  "required_skills": ["string"],
  "required_experience_years": "number",
  "required_education": ["string"],
  "certifications": ["string"],
  "reporting_to": "string"
}
```

### Field Definitions

| Field                     | Type    | Description |
|--------------------------|--------|-------------|
| job_id                   | string | Unique job identifier |
| role                     | string | Job title |
| domain                   | string | Functional area |
| category                 | string | Level (Entry/Mid/Senior) |
| required_skills          | array  | Required technical skills |
| required_experience_years| number | Minimum required experience |
| required_education       | array  | Required qualifications |
| certifications           | array  | Required certifications |
| reporting_to             | string | Reporting authority |

---

# 5. Candidate Scoring API Schemas

## 5.1 Scoring Request Schema

```json
{
  "resume_id": "string",
  "job_id": "string"
}
```

---

## 5.2 Scoring Response Schema

```json
{
  "status": "string",
  "score": "number",
  "breakdown": {
    "skill_score": "number",
    "experience_score": "number",
    "education_score": "number"
  }
}
```

### Example

```json
{
  "status": "success",
  "score": 72.5,
  "breakdown": {
    "skill_score": 80,
    "experience_score": 65,
    "education_score": 70
  }
}
```

---

# 6. Shortlisting API Schemas

## 6.1 Shortlist Request Schema

```json
{
  "job_id": "string",
  "resume_ids": ["string"]
}
```

---

## 6.2 Shortlist Response Schema

```json
{
  "status": "string",
  "ranking": [
    {
      "resume_id": "string",
      "score": "number",
      "status": "string"
    }
  ]
}
```

### Status Values

| Status         | Condition |
|---------------|----------|
| Shortlisted   | Score ≥ 70 |
| Under Review  | 50 ≤ Score < 70 |
| Rejected      | Score < 50 |

---

# 7. Async Job Status Schema

## 7.1 Status Response (Processing)

```json
{
  "job_token": "string",
  "status": "processing"
}
```

## 7.2 Status Response (Completed)

```json
{
  "job_token": "string",
  "status": "completed",
  "result": {}
}
```

---

# 8. Standard Error Response Schema

All API errors follow this unified structure:

```json
{
  "status": "error",
  "error_code": "string",
  "message": "string"
}
```

### Example

```json
{
  "status": "error",
  "error_code": "JOB_NOT_FOUND",
  "message": "Invalid Job ID"
}
```

---

# Conclusion

These schemas define the formal request and response contracts of the ATS AI system.  
They ensure structured communication between backend services and the AI-based resume parsing and scoring engine.

---