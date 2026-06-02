from sqlalchemy import Column, Integer, String, Float

from backend.app.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_key = Column(String, unique=True, index=True)
    company_name = Column(String, index=True)
    url = Column(String)
    title = Column(String, index=True)
    location = Column(String)
    description = Column(String)
    qualifications = Column(String)
    working_condition = Column(String)
    ai_summary = Column(String)
    title_ja = Column(String)
    description_ja = Column(String)
    qualifications_ja = Column(String)
    working_condition_ja = Column(String)
    job_category = Column(String, index=True)
    language_tags = Column(String)
    ai_related = Column(String)
    work_style = Column(String, index=True)
    employment_type = Column(String, index=True)
    experience_level_hint = Column(String)
    global_related = Column(String)
    tech_keywords = Column(String)
    job_score = Column(Float)
    job_reason = Column(String)
