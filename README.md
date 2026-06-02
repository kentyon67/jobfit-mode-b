# JobFit

AI-powered job analysis web application built with Python and Streamlit.

求人情報をAIで分析・可視化するWebアプリです。

---

# Live Demo

https://jobfit-n3etsba4vo9mw8nxplxbmd.streamlit.app/

---

# Screenshots

## Job List

![img_1.png](images/img_1.png)

![img_3.png](images/img_3.png)

## Job Detail

![img_4.png](images/img_4.png)

## Profile Settings

![img_5.png](images/img_5.png)

---

# Features

- Job scraping
- AI summarization
- AI translation
- Job classification
- Technology tag extraction
- Profile-based rescoring
- Keyword search
- Job filtering
- Streamlit web UI

求人情報を収集し、
AIによる分析・分類・スコアリングを行います。

---

# Tech Stack

## Frontend

- Streamlit
- HTML/CSS

## Backend / Data Processing

- Python
- pandas
- requests
- BeautifulSoup

## AI

- OpenAI API

## Infrastructure

- Streamlit Community Cloud

---

# System Architecture

```text
fetch_list
    ↓
fetch_detail
    ↓
build_dataset
    ↓
summarize
    ↓
translate
    ↓
classify
    ↓
score
    ↓
Streamlit UI
```

スクレイピングからAI分析、
UI表示までをパイプライン化しています。

---

# Project Structure

```text
job_scraper/
├── streamlit_app.py
├── src/
│   ├── app.py
│   ├── cli.py
│   ├── user_profile.py
│   ├── analysis/
│   │   └── ai/
│   │       ├── summarize.py
│   │       ├── translate.py
│   │       ├── classify.py
│   │       └── score.py
│   ├── pages/
│   │   ├── job_detail.py
│   │   └── profile_settings.py
│   └── pipeline/
│
├── data/
│   └── output/
│
├── images/
└── README.md
```

---

# Key Design Decisions

## 1. Separation of Responsibilities

Each processing stage is separated into independent modules:

- collection
- analysis
- classification
- scoring
- UI

This structure improves maintainability and extensibility.

責務分離を意識して設計しています。

---

## 2. Dynamic Profile-Based Rescoring

JobFit dynamically recalculates fit scores
based on user profile settings.

This enables lightweight personalization
without rebuilding datasets.

プロフィール変更時に、
UI側で再スコアリングを行います。

---

## 3. Preprocessed Dataset Architecture (Mode A)

Mode A focuses on:

- preprocessed datasets
- fast filtering
- lightweight deployment
- responsive UI

instead of realtime scraping.

事前生成済みデータを利用することで、
高速な検索体験を実現しています。

---

# Supported Data Source

Currently optimized for:

- Greenhouse job boards

Example:

```text
https://job-boards.greenhouse.io/paypay
```

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/kentyon67/jobfit.git
cd job_scraper
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Set OpenAI API Key

```bash
OPENAI_API_KEY=your_api_key
```

## Run Pipeline

```bash
python -m src.cli pipeline --mode full
```

## Run App

```bash
streamlit run streamlit_app.py
```

---

# Future Improvements (Mode B)

Planned extensions:

- FastAPI backend
- Database integration
- Realtime job search
- Automatic scheduled updates
- Multi-source job board support
- API-based search architecture

将来的には、
リアルタイム検索型アプリへの拡張を予定しています。

---

---

# Mode B — FastAPI Backend

JobFit Mode B is a backend-focused rebuild using FastAPI and SQLite.

This version is designed as a portfolio project demonstrating production-style backend engineering.

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite（→ PostgreSQL予定）
- Pydantic v2
- uvicorn

## Setup

### 1. Clone & Install

```bash
git clone https://github.com/kentyon67/jobfit-Mode-B.git
cd jobfit-Mode-B
pip install -r requirements.txt
```

### 2. Seed Database

CSVデータをSQLiteにインポートします。初回のみ実行します。

```bash
python scripts/seed_db.py
```

### 3. Start API Server（ターミナル1）

```bash
uvicorn backend.app.main:app --reload
```

API docs: http://localhost:8000/docs

### 4. Start Streamlit（ターミナル2）

```bash
streamlit run streamlit_app.py
```

App: http://localhost:8501

> FastAPI が起動していない状態で Streamlit を開くと、接続エラーとコマンド案内が表示されます。

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | ヘルスチェック（メッセージ） |
| GET | `/health` | ヘルスチェック（status: ok） |
| GET | `/jobs/` | 求人一覧（ページネーション・フィルタ対応） |
| GET | `/jobs/{job_id}` | 求人詳細 |

### Query Parameters（`GET /jobs/`）

| Parameter | Type | Description |
|---|---|---|
| `limit` | int | 取得件数（デフォルト: 20） |
| `offset` | int | 取得開始位置（デフォルト: 0） |
| `category` | str | カテゴリでフィルタ（例: `AI/ML`） |
| `work_style` | str | 勤務スタイルでフィルタ（例: `Remote`） |

## Project Structure

```text
jobfit-Mode-B/
├── backend/
│   └── app/
│       ├── main.py        # FastAPIアプリ本体
│       ├── database.py    # DBエンジン・セッション
│       ├── models.py      # SQLAlchemy モデル
│       ├── schemas.py     # Pydantic スキーマ
│       ├── crud/
│       │   └── jobs.py    # DB検索ロジック
│       └── routers/
│           └── jobs.py    # APIルーター
├── scripts/
│   └── seed_db.py         # CSVデータ投入スクリプト
├── data/
│   └── output/
│       └── jobs_classified.csv
├── requirements.txt       # ModeB依存関係
└── requirements_modea.txt # ModeA依存関係（参照用）
```

---

# Author

Kensei Ogura

GitHub:
https://github.com/kentyon67