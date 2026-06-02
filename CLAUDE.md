# JobFit ModeB

## Overview

JobFit is a job analysis and recommendation platform.

The original ModeA version collects job postings from company career pages, summarizes them with AI, classifies them, scores them, and helps users compare opportunities.

ModeB is a backend-focused rebuild of JobFit.

## Long-term Vision

The goal is to evolve JobFit into a production-style backend service that demonstrates:

* FastAPI
* SQLAlchemy
* PostgreSQL
* Docker
* AWS
* CI/CD
* API design
* Backend architecture

This project is primarily a portfolio project for backend engineering internships and future employment.

## Target User

Students and early-career engineers looking for technology-related jobs.

## Current Stage

Current implementation:

* FastAPI
* CSV-based data source
* GET /jobs/
* GET /jobs/{job_id}

Next milestones:

1. SQLite migration
2. SQLAlchemy integration
3. PostgreSQL migration
4. Dockerization
5. AWS deployment

## Development Rules

* Explain plans before modifying files.
* Prefer small incremental changes.
* Explain all changes in beginner-friendly Japanese.
* Do not perform large architectural refactors without approval.
* Prioritize backend engineering best practices.
