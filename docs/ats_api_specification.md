# ATS API Specification
## Day 16 – ATS API Design & Integration Planning

---

# 1. Overview

The ATS (Applicant Tracking System) AI is designed as a RESTful microservice that allows backend systems such as HR portals, admin dashboards, or job platforms to interact with AI-based resume parsing and scoring services.

The ATS exposes APIs for:

- Resume Upload
- Resume Parsing
- Candidate Scoring
- Shortlisting & Ranking
- Job Listing
- Async Job Status Tracking

---

# 2. Base Configuration

Base URL:
```
/api/v1/ats
```

Content-Type:
```
application/json
```

Authentication:
```
Bearer Token (JWT)
```

---

# 3. API Endpoints

---

## 3.1 Resume Upload API

### Endpoint
```
POST /api/v1/ats/resume/upload
```

### Description
Uploads resume file to system storage.

### Request (Multipart Form Data)

| Field         | Type   | Required |
|--------------|--------|----------|
| file         | file   | Yes      |
| candidate_id | string | Yes      |

### Response

```json
{
  "status": "success",
  "resume_id": "RES12345",
  "message": "Resume uploaded successfully"
}
```

### Error Responses

| Code | Description |
|------|------------|
| 400  | Invalid file |
| 413  | File too large |
| 500  | Storage failure |

---

## 3.2 Resume Parsing API

### Endpoint
```
POST /api/v1/ats/resume/parse
```

### Description
Converts raw resume into structured JSON schema.

### Request

```json
{
  "resume_id": "RES12345"
}
```

### Response

```json
{
  "status": "success",
  "structured_resume": {
    "name": "Arjun Menon",
    "skills": ["accounting", "ms excel"],
    "experience_years": 2,
    "education": ["b.com"],
    "certifications": []
  }
}
```

### Error Responses

| Code | Description |
|------|------------|
| 404  | Resume not found |
| 422  | Parsing failed |

---

## 3.3 Candidate Scoring API

### Endpoint
```
POST /api/v1/ats/score
```

### Description
Scores a candidate against selected Job Description.

### Request

```json
{
  "resume_id": "RES12345",
  "job_id": "AUD020"
}
```

### Response

```json
{
  "status": "success",
  "score": 68.5,
  "breakdown": {
    "skill_score": 70,
    "experience_score": 60,
    "education_score": 75
  }
}
```

### Error Responses

| Code | Description |
|------|------------|
| 404  | Job not found |
| 404  | Resume not found |
| 500  | Scoring failure |

---

## 3.4 Shortlisting API

### Endpoint
```
POST /api/v1/ats/shortlist
```

### Description
Ranks multiple candidates and classifies them based on predefined thresholds.

### Request

```json
{
  "job_id": "AUD020",
  "resume_ids": ["RES123", "RES456", "RES789"]
}
```

### Response

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
    },
    {
      "resume_id": "RES789",
      "score": 32,
      "status": "Rejected"
    }
  ]
}
```

---

## 3.5 Job Listing API

### Endpoint
```
GET /api/v1/ats/jobs
```

### Description
Returns all available job roles from master job repository.

### Response

```json
{
  "jobs": [
    {
      "job_id": "AUD020",
      "role": "Internal Auditor"
    },
    {
      "job_id": "AUD041",
      "role": "Financial Auditor"
    }
  ]
}
```

---

## 3.6 Async Job Status API

### Endpoint
```
GET /api/v1/ats/status/{job_token}
```

### Description
Used for checking status of long-running tasks such as resume parsing or semantic scoring.

### Example Response (Processing)

```json
{
  "job_token": "JOB789",
  "status": "processing"
}
```

### Example Response (Completed)

```json
{
  "job_token": "JOB789",
  "status": "completed",
  "result": {
    "score": 75
  }
}
```

---

# 4. Error Handling Standard

All error responses follow a uniform structure:

```json
{
  "status": "error",
  "error_code": "JOB_NOT_FOUND",
  "message": "Invalid Job ID"
}
```

---

# 5. Logging Standard

All API interactions are logged in structured JSON format.

Example log:

```json
{
  "timestamp": "2026-03-03T18:22:00Z",
  "level": "INFO",
  "endpoint": "/score",
  "job_id": "AUD020",
  "processing_time_ms": 120
}
```

---

# 6. Architecture Overview

High-Level Flow:

HR Portal  
→ Backend Server  
→ ATS API  
→ Resume Parser Engine  
→ Scoring Engine  
→ Ranking Engine  
→ Database / Storage  

---

# Conclusion

The ATS API is designed as a scalable, modular, RESTful microservice enabling backend systems to consume AI-powered resume parsing, scoring, and shortlisting functionalities efficiently.

---