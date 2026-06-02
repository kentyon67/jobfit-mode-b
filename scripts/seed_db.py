"""
CSVデータをSQLiteにインポートするスクリプト。
実行方法: python scripts/seed_db.py
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd

from backend.app.database import SessionLocal, engine
from backend.app import models


def to_str(val) -> str:
    if val is None or (isinstance(val, float) and math.isnan(val)):
        return ""
    return str(val)


def to_float(val) -> float | None:
    if val is None or (isinstance(val, float) and math.isnan(val)):
        return None
    try:
        return float(val)
    except (ValueError, TypeError):
        return None


def seed():
    models.Base.metadata.create_all(bind=engine)

    csv_path = Path(__file__).resolve().parents[1] / "data" / "output" / "jobs_classified.csv"
    if not csv_path.exists():
        print(f"CSV not found: {csv_path}")
        sys.exit(1)

    df = pd.read_csv(csv_path)

    db = SessionLocal()
    try:
        existing_count = db.query(models.Job).count()
        if existing_count > 0:
            print(f"DBにすでに {existing_count} 件あります。スキップします。")
            return

        jobs = [
            models.Job(
                id=int(row["job_id"]),
                job_key=to_str(row["job_key"]),
                company_name=to_str(row["company_name"]),
                url=to_str(row["url"]),
                title=to_str(row["title"]),
                location=to_str(row["location"]),
                description=to_str(row["description"]),
                qualifications=to_str(row["qualifications"]),
                working_condition=to_str(row["working_condition"]),
                ai_summary=to_str(row["ai_summary"]),
                title_ja=to_str(row["title_ja"]),
                description_ja=to_str(row["description_ja"]),
                qualifications_ja=to_str(row["qualifications_ja"]),
                working_condition_ja=to_str(row["working_condition_ja"]),
                job_category=to_str(row["job_category"]),
                language_tags=to_str(row["language_tags"]),
                ai_related=to_str(row["ai_related"]),
                work_style=to_str(row["work_style"]),
                employment_type=to_str(row["employment_type"]),
                experience_level_hint=to_str(row["experience_level_hint"]),
                global_related=to_str(row["global_related"]),
                tech_keywords=to_str(row["tech_keywords"]),
                job_score=to_float(row["job_score"]),
                job_reason=to_str(row["job_reason"]),
            )
            for _, row in df.iterrows()
        ]

        db.add_all(jobs)
        db.commit()
        print(f"{len(jobs)} 件のジョブをDBに登録しました。")

    finally:
        db.close()


if __name__ == "__main__":
    seed()
