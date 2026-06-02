import requests

API_BASE_URL = "http://127.0.0.1:8000"


def fetch_jobs(limit: int = 500) -> list[dict]:
    try:
        resp = requests.get(f"{API_BASE_URL}/jobs/", params={"limit": limit}, timeout=5)
        resp.raise_for_status()
        return resp.json()["items"]
    except requests.exceptions.ConnectionError:
        raise ConnectionError(
            "FastAPI サーバーに接続できません。\n"
            "先に `uvicorn backend.app.main:app --reload` を実行してください。"
        )
    except Exception as e:
        raise RuntimeError(f"API からのデータ取得に失敗しました: {e}")


def fetch_job(job_id: int) -> dict:
    try:
        resp = requests.get(f"{API_BASE_URL}/jobs/{job_id}", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.ConnectionError:
        raise ConnectionError(
            "FastAPI サーバーに接続できません。\n"
            "先に `uvicorn backend.app.main:app --reload` を実行してください。"
        )
    except requests.exceptions.HTTPError:
        if resp.status_code == 404:
            raise ValueError(f"求人ID {job_id} が見つかりません。")
        raise RuntimeError(f"API エラー: {resp.status_code}")
    except Exception as e:
        raise RuntimeError(f"API からのデータ取得に失敗しました: {e}")
