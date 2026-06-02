from sqlalchemy.orm import Session

from backend.app.models import Job


def get_jobs(
    db: Session,
    limit: int = 20,
    offset: int = 0,
    category: str | None = None,
    work_style: str | None = None,
) -> tuple[list[Job], int]:
    query = db.query(Job)

    if category:
        query = query.filter(Job.job_category == category)
    if work_style:
        query = query.filter(Job.work_style == work_style)

    total = query.count()
    items = query.offset(offset).limit(limit).all()
    return items, total


def get_job_by_id(db: Session, job_id: int) -> Job | None:
    return db.query(Job).filter(Job.id == job_id).first()
