from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.crud import jobs as crud_jobs
from backend.app.database import get_db
from backend.app.schemas import JobDetailResponse, JobListResponse

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/", response_model=JobListResponse)
def list_jobs(
    limit: int = 20,
    offset: int = 0,
    category: str | None = None,
    work_style: str | None = None,
    db: Session = Depends(get_db),
):
    items, total = crud_jobs.get_jobs(
        db, limit=limit, offset=offset, category=category, work_style=work_style
    )
    return {"count": len(items), "total": total, "items": items}


@router.get("/{job_id}", response_model=JobDetailResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = crud_jobs.get_job_by_id(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
