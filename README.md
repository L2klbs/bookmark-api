# 📚 Bookmark API

A lightweight API for tracking your personal progress across media — including books, manga, anime, movies, and more.

This service stores media entries with rich metadata such as title, genre, media type, image, and the last viewed URL. Designed for self-hosting and integrates easily into a GitOps-based deployment workflow.

---

## 🚀 Features

- Store and update entries with:
  - Title
  - Current progress (e.g. chapter or episode)
  - Media type (e.g. book, comic, movie)
  - Genre
  - Last viewed URL
  - Cover image (upload supported)
- REST API for CRUD operations
- Dockerized for consistent deployment
- Built for observability and CI/CD integration

---

## 📦 Project Structure

| Folder         | Description                          |
|----------------|--------------------------------------|
| `app/`         | FastAPI application code             |
| `tests/`       | Unit and integration tests           |
| `scripts/`     | Utility scripts (e.g., init_db.py)   |
| `Dockerfile`   | Container setup                      |
| `.github/`     | GitHub Actions workflows             |

---

## 🧪 Running Locally

### Prerequisites

- Python 3.12+
- PostgreSQL (or use Docker)
- virtualenv

### Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start database and run DB init
python scripts/init_db.py

# Run API
uvicorn app.main:app --reload

## Test
pytest

## Docker
docker build -t bookmark-api .
docker run -p 8000:8000 bookmark-api
```