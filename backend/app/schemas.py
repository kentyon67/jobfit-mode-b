from pydantic import BaseModel


class JobResponse(BaseModel):
    id: int
    job_key: str
    company_name: str
    url: str
    title: str
    location: str
    ai_summary: str | None = None
    title_ja: str | None = None
    job_category: str | None = None
    work_style: str | None = None
    employment_type: str | None = None
    experience_level_hint: str | None = None
    job_score: float | None = None

    model_config = {"from_attributes": True}


class JobDetailResponse(JobResponse):
    description: str | None = None
    qualifications: str | None = None
    working_condition: str | None = None
    description_ja: str | None = None
    qualifications_ja: str | None = None
    working_condition_ja: str | None = None
    language_tags: str | None = None
    ai_related: str | None = None
    global_related: str | None = None
    tech_keywords: str | None = None
    job_reason: str | None = None


class JobListResponse(BaseModel):
    count: int
    total: int
    items: list[JobResponse]
