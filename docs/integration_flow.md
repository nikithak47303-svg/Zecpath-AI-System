# ATS Integration Flow Document
## Day 16 – Deliverable 3

---

# 1. Overview

This document explains how backend systems integrate with the ATS AI microservice.

The ATS is designed as a REST-based AI engine responsible for:

- Resume Upload
- Resume Parsing
- Candidate Scoring
- Shortlisting & Ranking
- Async Job Handling

The system follows a modular microservice architecture.

---

# 2. High-Level Architecture

HR Portal / Admin Dashboard  
        ↓  
Backend Server (Application Layer)  
        ↓  
ATS API Service  
        ↓  
Resume Parser Engine  
Scoring Engine  
Ranking Engine  
        ↓  
Database / File Storage  

---

# 3. End-to-End Resume Processing Flow

## Step 1: Resume Upload

1. HR uploads resume through HR Portal.
2. Backend sends request to:

```
POST /api/v1/ats/resume/upload
```

3. ATS stores file in storage system.
4. ATS returns:

```json
{
  "status": "success",
  "resume_id": "RES12345"
}
```

The resume_id is stored in backend database.

---

## Step 2: Resume Parsing Flow

1. Backend calls:

```
POST /api/v1/ats/resume/parse
```

2. ATS:
   - Retrieves raw resume
   - Runs parsing engine
   - Extracts structured fields
   - Stores structured JSON

3. ATS returns structured resume data.

If parsing is heavy, ATS may respond with:

```json
{
  "job_token": "JOB789",
  "status": "processing"
}
```

Backend then checks:

```
GET /api/v1/ats/status/JOB789
```

Until status becomes:

```json
{
  "status": "completed"
}
```

---

# 4. Candidate Scoring Flow

## Step 1: Backend Request

Backend sends:

```json
{
  "resume_id": "RES12345",
  "job_id": "AUD020"
}
```

To:

```
POST /api/v1/ats/score
```

## Step 2: ATS Internal Processing

ATS performs:

1. Fetch structured resume
2. Fetch job description from master file
3. Calculate:
   - Skill match score
   - Experience match score
   - Education match score
4. Compute final weighted score

## Step 3: Response

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

Backend stores score in database.

---

# 5. Shortlisting & Ranking Flow

## Step 1: Backend Sends Bulk Request

```json
{
  "job_id": "AUD020",
  "resume_ids": ["RES123", "RES456", "RES789"]
}
```

To:

```
POST /api/v1/ats/shortlist
```

## Step 2: ATS Processing

For each resume:

1. Retrieve structured resume
2. Compute score
3. Sort by descending score
4. Apply threshold logic:

- Score ≥ 70 → Shortlisted
- 50 ≤ Score < 70 → Under Review
- Score < 50 → Rejected

## Step 3: Response

```json
{
  "status": "success",
  "ranking": [
    {
      "resume_id": "RES123",
      "score": 82,
      "status": "Shortlisted"
    },
    {
      "resume_id": "RES456",
      "score": 55,
      "status": "Under Review"
    }
  ]
}
```

Backend displays results on HR dashboard.

---

# 6. Async Job Handling Flow

Certain operations (semantic scoring, large file parsing) may take time.

Instead of blocking request:

1. ATS immediately returns:

```json
{
  "job_token": "JOB123",
  "status": "processing"
}
```

2. Backend periodically checks:

```
GET /api/v1/ats/status/JOB123
```

3. When complete:

```json
{
  "status": "completed",
  "result": {...}
}
```

This ensures:

- Non-blocking APIs
- Scalability
- Better user experience

---

# 7. Error Handling Flow

If invalid data is sent:

```json
{
  "status": "error",
  "error_code": "JOB_NOT_FOUND",
  "message": "Invalid Job ID"
}
```

Backend should:

- Log the error
- Display meaningful message to HR
- Avoid system crash

---

# 8. Logging & Monitoring Integration

Each API call generates structured logs:

```json
{
  "timestamp": "2026-03-03T18:22:00Z",
  "endpoint": "/score",
  "processing_time_ms": 120,
  "status": "success"
}
```

Logs are stored for:

- Audit trail
- Performance monitoring
- Debugging
- Compliance

---

# 9. Data Flow Summary

Resume Upload → Resume Parse → Score Calculation → Ranking → Status Classification → Dashboard Display

All communication happens via REST APIs using JSON format.

---

# Conclusion

The ATS AI system is designed as a scalable, modular microservice that integrates seamlessly with backend systems.

It supports:

- Structured request/response contracts
- Async job handling
- Error standardization
- Logging & monitoring
- Bulk shortlisting

This architecture ensures production-level readiness and enterprise integration capability.

---